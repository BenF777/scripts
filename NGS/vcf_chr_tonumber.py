#!usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import namedtuple

VCF = "/home/benflies/Desktop/NPHD_NorLux_Covered.bed"
VCF_FIXED = "/home/benflies/Desktop/NPHD_NorLux_Covered_fixed.bed"

print INTERVALS_BED

with open(INTERVALS_BED) as f:
    seen = set()
    for line in f:
        if line in seen:
            print(line)
        else:
            seen.add(line)

with open(INTERVALS_BED_FIXED,"w") as s:
    for item in seen:
        s.write("%s" % item)
