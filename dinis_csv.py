#!usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import re

input_csv_mnemonics = "/home/benflies/Desktop/Stat_Hb.csv" #csv with 1 column named "mnemonics"
result_csv = "/home/benflies/Desktop/res.csv"

def csv_to_dict(file_name):
    rows = []
    with open(file_name, "rt") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)
    return rows

mnemonics = csv_to_dict(input_csv_mnemonics)

with open(result_csv, 'w') as res:
    for i in mnemonics:
        header = []
        for name, row in i.items():
            header.append(name)
        break
    name = re.sub("{<HbA$", '', name)
    writer = csv.DictWriter(res, fieldnames=header)
    writer.writeheader()
    for mne in mnemonics:
        if "{<HbAS" in mne["Diagnostic Cod\xc3\xa9"]:
            continue
        if "{<HbAC" in mne["Diagnostic Cod\xc3\xa9"]:
            continue
        if "{<HbAE" in mne["Diagnostic Cod\xc3\xa9"]:
            continue
        if "{<HbAD" in mne["Diagnostic Cod\xc3\xa9"]:
            continue
        if "{<HbA" in mne["Diagnostic Cod\xc3\xa9"]:
            writer.writerow(mne)
