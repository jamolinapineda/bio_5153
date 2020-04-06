# /usr/bin/env python3
import csv
import argparse 

parser = argparse.ArgumentParser(description = "This script returns the start and end coordinates of a given .gff file")
parser.add_argument("GFF", help="the .gff file")
parser.add_argument("FASTA", help="the .fasta file")
args = parser.parse_args()

# open the GFF and FASTA files
gff = open(args.GFF, 'r')
fasta = open(args.FASTA, 'r')

# list for start and end coordinate
gene_start = []
gene_end = []

# read GFF file, line by line
for line in gff:
	# remove line breaks
	line = line.rstrip('\n')
	# split each line on the tab character
	# sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')
	fields = line.split('\t')
	# store the gene start and end coordinates
	gene_start.append(fields[3])
	gene_end.append(fields[4])

# print the genes in alphabetical order
for s, e in zip(gene_start, gene_end):
	print("start: " + s + " and" + " end: " + e)
gff.close()
fasta.close()


		



