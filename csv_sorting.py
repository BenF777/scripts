#!usr/bin/env python
# -*- coding: utf-8 -*-

import csv

input_csv_mnemonics = "/home/benflies/Desktop/mnemonic.csv" #csv with 1 column named "mnemonics"
input_csv_text = "/home/benflies/Desktop/noms.csv" #csv with 2 columns named "NOMS" and "TEXT"
result_csv = "/home/benflies/Desktop/result.csv" #name of the final csv (will contain 3 columns mnemonics, NOMS, TEXT)

def csv_to_dict(file_name):
    rows = []
    with open(file_name, "rt") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)
    return rows

mnemonics = csv_to_dict(input_csv_mnemonics)
noms = csv_to_dict(input_csv_text)

with open(result_csv, 'w') as res:
    fieldnames = ["mnemonic", "NOM", "TEXT"]
    writer = csv.DictWriter(res, fieldnames = fieldnames)
    writer.writeheader()
    for mne in mnemonics:
        for nom in noms:
            if mne["mnemonic"] in nom["TEXT"]:
                writer.writerow({"mnemonic":mne["mnemonic"], "NOM": nom["NOM"], "TEXT": nom["TEXT"]})
