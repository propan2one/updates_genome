#!/usr/bin/env python
# coding: utf8
"""
Created on 11 mai 2018
@author: delmotte
Ce script va parser un fichier au format *.gff3
Dérive de faesteri_convert (le regex) et cmd_abondance_oshv.py (gestion list / dict)
"""
import os
import sys
import argparse
import subprocess
import datetime, time
import shutil
import os
import re
from Bio.Blast import NCBIWWW
from Bio import SeqIO

#python  /export/home/delmotte/Documents/updates_genome/check_updates.py -g /export/home/delmotte/Documents/data/diversite_ohsv1/oshv-1A.fa  -a /export/home/delmotte/Documents/data/diversite_ohsv1/oshv-1A-corr.gff3  -o af11-t48-R1  -n 4

#python  /export/home/delmotte/Documents/updates_genome/check_updates.py 
# -g /export/home/delmotte/Documents/data/diversite_ohsv1/oshv-1A.fa 
# -a /export/home/delmotte/Documents/data/diversite_ohsv1/oshv-1A-corr.gff3 
# -o af11-t48-R1 
# -n 4

parser = argparse.ArgumentParser(description='')
#parser.add_argument('-f', help='R1 fastq file')
#parser.add_argument('-r', help='R2 fastq file', default='')
parser.add_argument('-g', help='Genome fasta file')
parser.add_argument('-a', help='GFF3 annotation file')
parser.add_argument('-o', help='basename for output files') #il y a une / à la fin de l'argument#
parser.add_argument('-n', help='Number of threads', type=int, default=4)
args = parser.parse_args()
""" Faut les *.fasta, le *.gff3 , et le *.vcf"""

gffname =  args.a
assert (gffname[-5:] == ".gff3"), "Problem with GFF3 file"
fastaname =  args.g
assert (fastaname[-7:] == ".fasta" or fastaname[-3:] == ".fa" ), "Problem with fasta file"

basename = args.o
#bamfile = basename + "_viralign.bam"
#count_reads = basename + "_count_reads.txt"

contentGFF = []
info_gff = {}
def gff3parser (filename):
    """ parser de GFF """
    with open(filename) as f:
        for line in f:
            if line.startswith("#"):
                continue
            content = line.strip().split("\t")
            if len(content) == len(contentGFF):
                numORF = content[8].strip().split(";")
                for orf in numORF:
                    if re.search(r"^product=ORF[0-9]+", orf):
                        contentGFF.append(orf)
                        print(orf)
                info_gff = dict(zip(contentGFF, list(content[3], content[4], content[6])) )

#print("\n\n"+ args.f + " | Started at " + str(datetime.datetime.now()))

gff3parser(gffname)
print(info_gff)
#print("\n\n"+ args.f + " | End at " + str(datetime.datetime.now()))