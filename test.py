#!usr/bin/env python
# -*- coding: utf-8 -*-

import os

def fcount(path):
    patients = 0
    for f in os.listdir(path):
        patients += 1
    return patients

path_2016 = "/mnt/genmachines/MPS Data Hub/Samples/2016"
path_2015 = "/mnt/genmachines/MPS Data Hub/Samples/2015"
path_2014 = "/mnt/genmachines/MPS Data Hub/Samples/2014"
path_2012 = "/mnt/genmachines/MPS Data Hub/Samples/2012"

print("Year 2016: %s") %fcount(path_2016)
print("Year 2015: %s") %fcount(path_2015)
print("Year 2014: %s") %fcount(path_2014)
print("Year 2012: %s") %fcount(path_2012)

print("Total patients: %s") %(fcount(path_2016)+fcount(path_2015)+fcount(path_2014)+fcount(path_2012))

counter_tst15 = 0
counter_hpx = 0
for root, dirs, files in os.walk("/mnt/genmachines/MPS Data Hub/Samples"):
    for name in dirs:
        if "tst15" in name:
            #print os.path.join(root, name)
            counter_tst15 += 1
        if "hpx_csc" in name:
            counter_hpx += 1
print("Illumina TruSight Tumor 15 Libraries: %s") %counter_tst15
print("Agilent Haloplex HS ClearSeq Cancer Libraries: %s") %counter_hpx
