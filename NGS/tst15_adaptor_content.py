#!usr/bin/env python
# -*- coding: utf-8 -*-

from Bio import SeqIO
from datetime import datetime

now = datetime.now()

print 'Request Time: %s/%s/%s %s:%s:%s' % (now.day, now.month, now.year, now.hour, now.minute, now.second)

"""
def trim_adaptors(records, adaptor):
    len_adaptor = len(adaptor)
    for record in records:
        index = record.seq.find(adaptor)
        if index == -1:
            yield record
        else:
            yield record[index+len_adaptor]

original_reads = SeqIO.parse("/home/benflies/NGS_Data/FASTQ/fastq_tst_ffpe/15001181_S1_L001_R1_001_copy.fastq", "fastq")
trimmed_reads = trim_adaptors(original_reads, "ATCTCGTATGCCGTCTTCTGCTTG")
count = SeqIO.write(trimmed_reads, "trimmed.fastq", "fastq")
print("Saved %i reads" % count)
"""
from Bio import SeqIO

adapter_counter = 0
clean_counter = 0

for rec in SeqIO.parse("/home/benflies/NGS_Data/FASTQ/fastq_tst_ffpe/15001181_S1_L001_R1_001_copy.fastq", "fastq"):
    if "ATCTCGTATGCCGTCT" in rec :
        adapter_counter += 1

for rec in SeqIO.parse("/home/benflies/NGS_Data/FASTQ/fastq_tst_ffpe/15001181_S1_L001_R1_001_copy.fastq", "fastq"):
    if "ATCTCGTATGCCGTCT" not in rec :
        clean_counter += 1

print adapter_counter
print clean_counter
