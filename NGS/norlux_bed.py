#!usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import namedtuple

INTERVALS_BED = "/home/benflies/Desktop/NPHD_NorLux_Covered.bed"
INTERVALS_BED_FIXED = "/home/benflies/Desktop/NPHD_NorLux_Covered_fixed.bed"

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











"""
if INTERVALS_BED:
  with open(INTERVALS_BED, "r") as start:
      with open(INTERVALS_BED_FIXED, "r") as end:
          for line in start.readlines():
              if line in INTERVALS_BED_FIXED:
                  print line

"""




"""
IntervalColumns = namedtuple('bed', ['chr', 'start', 'end', 'gene'])
intervals_list = []

if INTERVALS_BED:
  with open(INTERVALS_BED, "r") as fin:
      for line in fin.readlines():
          line = line.rstrip('\n')
          line = re.split(r'\t+', line.rstrip('\t'))
          print line

          if len(line) == 5:
              line[1] = int(line[1])
              line[2] = int(line[2])
              bed_line = IntervalColumns(*(line[0], int(line[1]), int(line[2]), line[3]))
              intervals_list.append(bed_line)

"""
