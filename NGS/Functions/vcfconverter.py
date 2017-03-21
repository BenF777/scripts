#!usr/bin/env python
# -*- coding: utf-8 -*-

import re

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
