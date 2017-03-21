#!usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
sys.path.append("/home/benflies/Bioinformatics/Scripts/NGS/Functions")
from vcfconverter import vcf_converter
from bedconverter import bed_converter

def region_filter(vcf, bed):
    counter = 0
    variants = vcf_converter(vcf)
    regions = bed_converter(bed)
    with open(vcf, "r") as inVCF:
        for line in inVCF:
            variant_frequency = 0
            line = line.rstrip('\n')
            line = re.split(r'\t+', line.rstrip('\t'))
            if line[0].startswith("##"):
                print "\t".join(line)
            elif line[0] == '#CHROM':
                print '\t'.join(line)
    for variant in variants:
        for key, value in regions.items():
            if variant[0] == key and int(variant[1]) in value :
                counter += 1
                print '\t'.join(variant)
