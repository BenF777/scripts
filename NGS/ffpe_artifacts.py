#!usr/bin/env python
# -*- coding: utf-8 -*-

import re

VCFFILE = "/mnt/genmachines/MPS Data Hub/Samples/2016/16026735/mltp_som_brca_m_plus/16026735_full_variant_table_sophia.vcf"

with open(VCFFILE, "r") as inVCF:
    AT=0
    AC=0
    AG=0
    CG=0
    CT=0
    CA=0
    GA=0
    GT=0
    GC=0
    TA=0
    TC=0
    TG=0
    for line in inVCF:
        line = line.rstrip("\n")
        line = re.split(r"\t+", line.rstrip("\t"))
        if line[0].startswith("#"):
            continue
        else:
            alt = line[4]
            ref = line[3]

            if ref=="A" and alt=="T":
                AT+=1
            if ref=="A" and alt=="C":
                AC+=1
            if ref=="A" and alt=="G":
                AG+=1
            if ref=="C" and alt=="A":
                CA+=1
            if ref=="C" and alt=="T":
                CT+=1
            if ref=="C" and alt=="G":
                CG+=1
            if ref=="T" and alt=="A":
                TA+=1
            if ref=="T" and alt=="C":
                TC+=1
            if ref=="T" and alt=="G":
                TG+=1
            if ref=="G" and alt=="C":
                GC+=1
            if ref=="G" and alt=="T":
                GT+=1
            if ref=="G" and alt=="A":
                GA+=1

print(AT)
print(AG)
print(AC)

print(TA)
print(TC)
print(TG)

print(CG)
print(CT)
print(CA)

print(GC)
print(GT)
print(GA)
