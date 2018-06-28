#!/usr/bin/env python
# coding: utf8
"""
Created on 11 mai 2018
@author: delmotte
Ce script va parser un fichier au format *.gff3
Derive : ComptageSNP.py
"""
import os
import sys
import argparse
import subprocess
import datetime, time
import shutil
import os

# python3 ~/Documents/updates_genome/check_updates.py -g ~/Documents/data/OsHV-1_strain_microVar_variant_A.fasta -a ~/Documents/data/OsHV-1_strain_microVar_variant_A.gff3 -o af11-t48-R1 -n 4

#python ~/Documents/updates_genome/check_updates.py 
# -g ~/Documents/data/OsHV-1_strain_microVar_variant_A.fasta
# -a ~/Documents/data/OsHV-1_strain_microVar_variant_A.gff3 
# -o af11-t48-R1 
# -n 4

parser = argparse.ArgumentParser(description='')
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.0', help="Show program's version number and exit.")
parser.add_argument('-g', help='Genome fasta file')
parser.add_argument('-a', help='GFF3 annotation file')
parser.add_argument('-o', help='basename for output files') #il y a une / à la fin de l'argument#
parser.add_argument('-n', help='Number of threads', type=int, default=4)
args = parser.parse_args()
""" Faut les *.fasta, le *.gff3 , et le *.vcf"""

gffname =  args.a
assert (gffname[-5:] == ".gff3"), "Problem with GFF3 file"

basename = args.o

print("\n\n"+ args.f + " | Started at " + str(datetime.datetime.now()))

contentGFF = ["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"]
def gff3parser (filename):
    """ parser de GFF """
    with open(filename) as f:
        for line in f:
            if line.startswith("#"):
                continue
            content = line.strip().split("\t")
            if len(content) == len(contentGFF):
                print(content[8])
                numORF = content[8].strip().split(";")
                print(numORF)

gff3parser(gffname)

print("\n\n"+ args.f + " | End at " + str(datetime.datetime.now()))