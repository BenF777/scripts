#!usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys

dbsnp_vcf = "/home/benflies/NGS_Data/hg19/dbsnp_138.hg19.excluding_sites_after_129_copy.vcf"

with open(dbsnp_vcf, "r") as dbsnp:
    sys.stdout = open("/home/benflies/Desktop/dbsnp_chr22.vcf", "w")
    for dbline in dbsnp.readlines():
        line = dbline
        line = line.rstrip('\n')
        line = re.split(r'\t+', line.rstrip('\t'))
        if "chr22" == str(line[0]):
            sys.stdout.write(dbline)
    sys.stdout.close()
