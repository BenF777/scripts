#!usr/bin/env python
# -*- coding: utf-8 -*-

import re

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
    return chr_dict
