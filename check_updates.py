#!/usr/bin/env python
# coding: utf8
"""
Created on 11 mai 2018
@author: delmotte
Ce script va parser un fichier au format *.gff3
Derive : ComptageSNP.py
"""
import os, sys, argparse, subprocess, re, datetime, time, shutil
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

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
orf = {}

print("\n\n"+ args.g + " | Started at " + str(datetime.datetime.now()) + "\n")

contentGFF = ["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"]
def gff3parser (filename, dictOrf):
    """ parser de GFF """
    with open(filename) as f:
        for line in f:
            if line.startswith("#"):
                continue
            content = line.strip().split("\t")
            if len(content) == len(contentGFF):
                value = [content[3], content[4], content[6]]
                #print(value)
                #print(content[8])
                numORF = content[8].strip().split(";")
                #print(numORF)
                for product in numORF:
                    if re.search(r"^product=ORF\d{0,3}", product):
                        keys = product[11:]
                        dictOrf[keys] = value
                        #return dictOrf
        return {}

def Seqslicer (Sequ, dictORF):
    """Slice sequence in fasta file from dict"""
    record = SeqIO.read(Sequ, "fasta")
    for keys, value in dictORF.items():   
        nameORF = "ORF" + keys
        print(value[2])
        seqORF = record.seq[(int(value[0])-1):int(value[1]) ]
        if value[2] == "-":
            pass
        elif value[2] == "+":
            seqORF = seqORF.reverse_complement()
        #print(nameORF, "\n",seqORF) Affiche les séquences dans le tem (stdrr)
        if not os.path.isfile(str(nameORF)+ ".fasta"):
            print("\n writing of" + str(nameORF)+ ".fasta ... \n")
            with open(str(nameORF)+ ".fasta", "a+") as f:
                f.writelines(">" + nameORF + "\n")
                f.writelines(str(seqORF))
        else :
            print("\n file {} already exist.. \n".format(str(nameORF)+ ".fasta"))
            

gff3parser(gffname,orf)

# Verification :
verif = []
for x in range (1,10):
    verif.append(str(x))

for val in verif:
    if not val in orf.keys():
        print(val)

#Slice the fasta
Seqslicer(args.g, orf)

print("\n\n"+ args.g + " | End at " + str(datetime.datetime.now()))

