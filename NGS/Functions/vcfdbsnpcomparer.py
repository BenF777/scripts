#!usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

def vcf_dbsnp_comparer(input_vcf, dbsnp_vcf):
    chromosomes = ["chrY", "chrX", "chrM", "chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10", "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19", "chr20", "chr21", "chr22"]

    vcf_lines = []

    with open(input_vcf, "r") as vcf:
        for vcfline in vcf.readlines():
            vcfline = vcfline.rstrip('\n')
            vcfline = re.split(r'\t+', vcfline.rstrip('\t'))
            vcf_lines.append(vcfline)

    for line in vcf_lines:
        if line[0].startswith("##"):
            print "\t".join(line)
        elif line[0] == '#CHROM':
            print '\t'.join(line)
        else:
            continue

    for chromo in chromosomes:
        with open("/home/benflies/Desktop/dbsnp_"+chromo+".vcf", "r") as dbsnp:
            db_lines = set(dbsnp)
            for line in vcf_lines:
                if line[0].startswith("##"):
                    continue
                elif line[0] == '#CHROM':
                    continue
                elif line[0] == chromo:
                    for dline in db_lines:
                        if line[1] in dline:
                            dline = dline.rstrip('\n')
                            dline = re.split(r'\t+', dline.rstrip('\t'))
                            line[2] = dline[2]
                else:
                    continue
                print '\t'.join(line)


sys.stdout = open("/home/benflies/Desktop/186PDX_S4_snps_filtered_with_rs.vcf", "w")
vcf_dbsnp_comparer("/home/benflies/Desktop/186PDX_S4_snps_filtered_4.vcf", "/home/benflies/NGS_Data/hg19/dbsnp_138.hg19_copy.vcf")
sys.stdout.close()
