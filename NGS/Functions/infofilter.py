#!usr/bin/env python
# -*- coding: utf-8 -*-

import re

def info_filter(vcf, info_field, threshold):
    with open(vcf, "r") as inVCF:
        for line in inVCF:
            variant_frequency = 0
            line = line.rstrip('\n')
            line = re.split(r'\t+', line.rstrip('\t'))
            if line[0].startswith("##"):
                print "\t".join(line)
            elif line[0] == '#CHROM':
                print '\t'.join(line)
            elif re.search(r'^(\d+|X|Y)|^chr(\d+|X|Y)', line[0]):
                flag = 0
                for k,x in enumerate(line[7].split(';')):
                    if info_field == "QUAL":
                        if float(line[5]) > threshold:
                            flag = 1
                            break
                    elif info_field == "DP4_freq":
                        summ = 0
                        if x.split('=')[0] == info_field.split('_freq')[0]:
                            l = x.split('=')[1]
                            reference = float(l.split(",")[0]) + float(l.split(",")[1])
                            alternate = float(l.split(",")[2]) + float(l.split(",")[3])
                            summ = float(reference) + float(alternate)
                            variant_frequency = float(alternate) / summ
                            if variant_frequency > threshold:
                                flag = 1
                                break
                    elif info_field == "DP4_SB":
                        SB = 0
                        if x.split('=')[0] == info_field.split('_SB')[0]:
                            l = x.split('=')[1]
                            forward = float(l.split(",")[2])
                            reverse = float(l.split(",")[3])
                            if forward > 0 and reverse > 0:
                                SB = float(forward) / float(reverse)
                            elif forward == 0:
                                SB = 0
                            elif reverse == 0:
                                SB = 1
                            if SB > threshold:
                                flag = 1
                                break
                    else:
                        if x.split('=')[0] == info_field:
                            if float(x.split('=')[1]) > threshold:
                                flag = 1
                                break
                if flag == 1 :
                    print '\t'.join(line)
            else:
                continue
                #print '\t'.join(line)
