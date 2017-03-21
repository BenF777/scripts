#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
from itertools import chain
from os.path import normpath, basename
sys.path.append("/home/benflies/Bioinformatics/Scripts/NGS/Functions")
from vcfconverter import vcf_converter
from bedconverter import bed_converter
from regionfilter import region_filter
from infofilter import info_filter
import argparse
from argparse import RawTextHelpFormatter


parser = argparse.ArgumentParser(
    description="""
    ------- VCF Filterer -------

     Developed by Ben Flies, LNS

    ----------------------------""",
    formatter_class=RawTextHelpFormatter)

"""Define possible input arguments"""
parser.add_argument("VCF", type=str, help="Input VCF File (required)")
parser.add_argument("-BED", type=str, help="Input BED File")
parser.add_argument("-QUAL", type=str, help="Genotype Quality Threshold")
parser.add_argument("-DP", help="Variant Coverage (Depth) Threshold")
parser.add_argument("-DP4_freq", help="Variant Allele Frequency Threshold")
parser.add_argument("-DP4_SB", help="Strand Bias Threshold")

args = parser.parse_args()

VCF_FILE = args.VCF
print "filtering file %s" %VCF_FILE

"""
elif args.DP:
    print "filtering for minimum coverage"
elif args.DP4_freq:
    print "filtering for minimum variant allele frequency"
elif args.DP4_SB:
    print "filtering for minimum strand bias"
"""


#VCF_FILE = "/home/benflies/NGS_Data/Norlux/186PDX_S4_snps.vcf"
BED_FILE = "/home/benflies/Desktop/NPHD_NorLux_Covered_fixed.bed"

#BED_FILE = sys.argv[1]

#VCF_FILE = "/home/benflies/Desktop/15001181_S1_surecall_duplicates.vcf"
#BED_FILE = "/home/benflies/NGS_Data/00100-1407755742_Regions.bed"

counter = 0

base = basename(normpath(VCF_FILE))
base = base.rsplit(".vcf")[0]

open("/home/benflies/Desktop/"+base+"_filtered_"+str(counter)+".vcf", "w").writelines([l for l in open(VCF_FILE).readlines()])

if ".bed" in sys.argv[1]:
    sys.stdout = open("/home/benflies/Desktop/"+base+"_filtered_"+str(counter)+".vcf", "w")
    region_filter(VCF_FILE, BED_FILE)
    sys.stdout.close()
    for arg in sys.argv[2:]:
        l = arg.split('=')
        info = str(l[0])
        val = float(l[1])
        counter += 1
        counter_1 = counter - 1
        sys.stdout = open("/home/benflies/Desktop/"+base+"_filtered_"+str(counter)+".vcf", "w")
        info_filter("/home/benflies/Desktop/"+base+"_filtered_"+str(counter_1)+".vcf", info, val)
        sys.stdout.close()
        #os.remove("/home/benflies/Desktop/"+base+"_filtered_"+str(counter_1)+".vcf")
