#!usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import glob
import re
from collections import namedtuple
import pybedtools
import pandas as pd
import numpy as np
from itertools import izip

INTERVALS_BED = "/home/benflies/Bioinformatics/NGS_Pipelines/pipeline_Norlux/scripts/bed/NPHD.bed"

DIRECTORY = "/home/benflies/Bioinformatics/NGS_Pipelines/pipeline_Norlux/NGS_DATA/161114-ARJLA_NorLux_2/out/bam"

intermediate_csv = "/home/benflies/Desktop/intermediate.csv"
result_csv = "/home/benflies/Desktop/res_1.csv"

bam_file_list = [f for f in glob.iglob(DIRECTORY+"/*aligned.dupsMarked.bam")]

column_names = []
column_names.append("amplicon")
for name in bam_file_list:
    column_names.append(name)

lists = []

for file in bam_file_list:

    cov_list = []
    amplicon_list = []

    print file

    IntervalColumns = namedtuple('bed', ['chr', 'start', 'end', 'gene'])
    intervals_list = []

    with open(INTERVALS_BED, "r") as fin:
        for line in fin.readlines():
            line = line.rstrip('\n')
            line = re.split(r'\t+', line.rstrip('\t'))

            if len(line) == 5:
                line[1] = int(line[1])
                line[2] = int(line[2])
                bed_line = IntervalColumns(*(line[0], int(line[1]), int(line[2]), line[3]))
                intervals_list.append(bed_line)

    almnt = pybedtools.BedTool(file)
    coverage_result = almnt.coverage(intervals_list)

    for line in coverage_result:
        cov_list.append(int(line[4]))
        amplicon_list.append(str(line[3]))

    lists.append(cov_list)

with open(intermediate_csv, "w") as intermediate:
    writer = csv.writer(intermediate)
    writer.writerow(amplicon_list)
    for l in lists:
        writer.writerow(l)

a = izip(*csv.reader(open(intermediate_csv, "rb")))

with open(result_csv, "w") as result:
    writer1 = csv.writer(result)
    writer1.writerow(column_names)
    writer1.writerows(a)
"""
with open(result_csv_1, "rb") as csv_file:
    reader = csv.DictReader(csv_file)
    xs = []
    for row in reader:
        x = int(row)
        xs.append(x)
    x_average = sum(xs) / len(xs)
    print(x_average)
"""
