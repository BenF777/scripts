#!usr/bin/env python
# -*- coding: utf-8 -*-

import re

VCF_FILE = "/home/benflies/NGS_Data/Norlux/186PDX_S4_dedup.var.raw.vcf"

COVERAGE_THRESHOLD = 40
VAR_FREQ_THRESHOLD = 0.1
VAR_QUAL_THRESHOLD = 99
STRAND_BIAS_THRESHOLD = 0.1

lines = []
header = []

line_counter = 0
if VCF_FILE:
    with open(VCF_FILE, "r") as fin:
        for line in fin.readlines():
            line = line.rstrip('\n')
            line = re.split(r'\t+', line.rstrip('\t'))
            lines.append(line)
            line_counter += 1
print("Total Variants: %s") %(line_counter)

collected = {}

for line in lines:
    if line[0].startswith("##"):
        print line
        header.append(line)
    else:
        variant_ID = line[0]+'_'+line[1]+'_'+line[3]+'_'+line[4]
        if variant_ID not in collected:
            collected[variant_ID] = {
                "#CHROM" : line[0],
                "POS" : line[1],
                "ID" : line[2],
                "REF" : line[3],
                "ALT" : line[4],
                "QUAL" : line[5],
                "FILTER" : line[6],
                "DP" : 0,
                "VDB" : 0,
                "RPB" : 0,
                "MQB" : 0,
                "BQB" : 0,
                "MQOF" : 0,
                "AF1" : 0,
                "AC1" : 0,
                "DP4" : 0,
                "MQ" : 0,
                "MQSB" : 0,
                "FQ" : 0,
                "PV4" : 0,
                "FORMAT" : line[8],
                "SAMPLE" : line[9]
                }

            INFO = line[7].split(";")

            for item in INFO:
                if item.split("=")[0] == "DP":
                    collected[variant_ID]["DP"] = item.split("=")[1]
                if item.split("=")[0] == "VDB":
                    collected[variant_ID]["VDB"] = item.split("=")[1]
                if item.split("=")[0] == "RPB":
                    collected[variant_ID]["RPB"] = item.split("=")[1]
                if item.split("=")[0] == "MQB":
                    collected[variant_ID]["MQB"] = item.split("=")[1]
                if item.split("=")[0] == "BQB":
                    collected[variant_ID]["BQB"] = item.split("=")[1]
                if item.split("=")[0] == "MQOF":
                    collected[variant_ID]["MQOF"] = item.split("=")[1]
                if item.split("=")[0] == "AF1":
                    collected[variant_ID]["AF1"] = item.split("=")[1]
                if item.split("=")[0] == "AC1":
                    collected[variant_ID]["AC1"] = item.split("=")[1]
                if item.split("=")[0] == "DP4":
                    collected[variant_ID]["DP4"] = item.split("=")[1]
                if item.split("=")[0] == "MQ":
                    collected[variant_ID]["MQ"] = item.split("=")[1]
                if item.split("=")[0] == "MQSB":
                    collected[variant_ID]["MQSB"] = item.split("=")[1]
                if item.split("=")[0] == "FQ":
                    collected[variant_ID]["FQ"] = item.split("=")[1]
                if item.split("=")[0] == "PV4":
                    collected[variant_ID]["PV4"] = item.split("=")[1]

f = open("outfile.txt", "w")

for line in header:
    f.write("\n".join(map(lambda x: str(x), line)))
collected_filtered = collected

counter = 0

for variant,factor in collected.items():
    if float(factor["DP"]) >= COVERAGE_THRESHOLD:
        if float(factor["AF1"]) >= VAR_FREQ_THRESHOLD:
            if float(factor["QUAL"]) >= VAR_QUAL_THRESHOLD:
                counter += 1
                f.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (factor["#CHROM"],factor["POS"],factor["ID"], factor["REF"], factor["ALT"], factor["QUAL"], factor["FILTER"]))

f.close()
print("Variants Left After Filtering: %s") %(counter)
