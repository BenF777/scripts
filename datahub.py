#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

datahub = "/mnt/genmachines/MPS Data Hub/Samples/2017/"
#datahub = "/home/benflies/Desktop/test/"

sample_basename = "test"

library_prep_kit = "/tst15/"

directory = datahub+sample_basename+library_prep_kit

print(directory)

os.makedirs(directory)

shutil.copy("/home/benflies/Desktop/test_file", directory)

open(directory+"_workflow.txt", "a").close()

workflow_file = open(directory+"_workflow.txt", "w")

workflow_file.write("analysis:\n")
workflow_file.write("    raw_reads:\n")
workflow_file.write("        - test.fastq.gz\n")
workflow_file.write("    assemblies:\n")
workflow_file.write("    variants:\n")

workflow_file.close()
