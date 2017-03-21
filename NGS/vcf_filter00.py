#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
from itertools import chain
from os.path import normpath, basename

VCF_FILE = "/home/benflies/NGS_Data/Norlux/186PDX_S4_snps.vcf"
BED_FILE = "/home/benflies/Desktop/NPHD_NorLux_Covered_fixed.bed"

#BED_FILE = sys.argv[1]

#VCF_FILE = "/home/benflies/Desktop/15001181_S1_surecall_duplicates.vcf"
#BED_FILE = "/home/benflies/NGS_Data/00100-1407755742_Regions.bed"

COVERAGE_THRESHOLD = 40
VAR_FREQ_THRESHOLD = 0.1
VAR_QUAL_THRESHOLD = 99
STRAND_BIAS_THRESHOLD = 0.1

def vcf_converter(vcf_filename):
    """
    Bring VCF in a more easy format for certain applications
    """
    lines = []
    variant_counter = 0
    meta = []
    header = []
    variants = []
    with open(vcf_filename, "r") as fin:
        for line in fin.readlines():
            line = line.rstrip('\n')
            line = re.split(r'\t+', line.rstrip('\t'))
            lines.append(line)
    for line in lines:
        if line[0].startswith("##"):
            meta.append(line)
        elif line[0].startswith("#CHROM"):
            header.append(line)
        else:
            variants.append(line)
            variant_counter += 1
    print("Total Variants in VCF File: %s") %(variant_counter)
    return variants
    return variant_counter

def bed_converter(bed_filename):
    chr_dict = {
        "chr1": [],
        "chr2": [],
        "chr3": [],
        "chr4": [],
        "chr5": [],
        "chr6": [],
        "chr7": [],
        "chr8": [],
        "chr9": [],
        "chr10": [],
        "chr11": [],
        "chr12": [],
        "chr13": [],
        "chr14": [],
        "chr15": [],
        "chr16": [],
        "chr17": [],
        "chr18": [],
        "chr19": [],
        "chr20": [],
        "chr21": [],
        "chr22": [],
        "chrX": [],
        "chrY": [],
        "chrM": [],
    }
    bedlines = []
    bedline_counter = 0
    with open(bed_filename, "r") as bed:
        for bedline in bed.readlines():
            bedline = bedline.rstrip('\n')
            bedline = re.split(r'\t+', bedline.rstrip('\t'))
            bedline_counter +=1
            line_range = range(int(bedline[1]),int(bedline[2]))
            for key, value in chr_dict.items():
                if key == bedline[0]:
                    for i in line_range:
                        chr_dict[key].append(i)
    print("Total Regions in BED File: %s") %(bedline_counter)
    return chr_dict

def region_filter(vcf, bed):
    counter = 0
    variants = vcf_converter(vcf)
    regions = bed_converter(bed)
    for variant in variants:
        for key, value in regions.items():
            if variant[0] == key and int(variant[1]) in value :
                counter += 1
                print '\t'.join(line)
    print("Variants Inside of Regions Defined in BED File: %s") %(counter)

def VCF_Info_filter(vcf, info_field, threshold):
    with open(vcf, "r") as inVCF:
        for line in inVCF:
            variant_frequency = 0
            line = line.rstrip('\n')
            line = re.split(r'\t+', line.rstrip('\t'))
            if line[0].startswith("##"):
                print "\t".join(line)
            elif line[0] == '#CHROM':
                print '\t'.join(line)
            elif re.search(r'^(\d+|X|Y)|^chr(\d+|X|Y)', line[0]):
                flag = 0
                for k,x in enumerate(line[7].split(';')):
                    if info_field == "DP4_freq":
                        summ = 0
                        if x.split('=')[0] == info_field.split('_freq')[0]:
                            l = x.split('=')[1]
                            reference = float(l.split(",")[0]) + float(l.split(",")[1])
                            alternate = float(l.split(",")[2]) + float(l.split(",")[3])
                            summ = float(reference) + float(alternate)
                            variant_frequency = float(alternate) / summ
                            if variant_frequency > threshold:
                                flag = 1
                                break
                    elif info_field == "DP4_SB":
                        SB = 0
                        if x.split('=')[0] == info_field.split('_SB')[0]:
                            l = x.split('=')[1]
                            forward = float(l.split(",")[2])
                            reverse = float(l.split(",")[3])
                            if forward > 0 and reverse > 0:
                                SB = float(forward) / float(reverse)
                            elif forward == 0:
                                SB = 0
                            elif reverse == 0:
                                SB = 1
                            if SB > threshold:
                                flag = 1
                                break
                    else:
                        if x.split('=')[0] == info_field:
                            if float(x.split('=')[1]) > threshold:
                                flag = 1
                                break
                if flag == 1 :
                    print '\t'.join(line)
            else:
                continue
                #print '\t'.join(line)

counter = 0

base = basename(normpath(VCF_FILE))
base = base.rsplit(".vcf")[0]

open("/home/benflies/Desktop/"+base+"_filtered_"+str(counter)+".vcf", "w").writelines([l for l in open(VCF_FILE).readlines()])

region_filter(VCF_FILE, BED_FILE)

if ".bed" in sys.argv[1]:
    region_filter(VCF_FILE, BED_FILE)

for arg in sys.argv[2:]:
    l = arg.split('=')
    info = str(l[0])
    val = float(l[1])
    counter += 1
    counter_1 = counter - 1
    sys.stdout = open("/home/benflies/Desktop/"+base+"_filtered_"+str(counter)+".vcf", "w")
    VCF_Info_filter("/home/benflies/Desktop/"+base+"_filtered_"+str(counter_1)+".vcf", info, val)
    sys.stdout.close()
    os.remove("/home/benflies/Desktop/"+base+"_filtered_"+str(counter_1)+".vcf")
