# /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO 

# create an argument parser object
parser = argparse.ArgumentParser(description = "This script parses a GFF file and does stuff with it")

# add postional arguments 
parser.add_argument("gff", help="the .gff file")
parser.add_argument("fasta", help="the .fasta file")

# parse the arguments
args = parser.parse_args()

# read and parse the FASTA file 
genome = SeqIO.read(args.fasta, 'fasta')

# # print(dir(genome))
# print(genome.description)
# print (len(genome.seq))
# print(genome.seq) 

# read GFF file, line by line
with open(args.gff, 'r') as gff_file: 

	#create a csv reader object 
	reader = csv.reader(gff_file, delimiter="\t")

	for line in reader:
		#skip blank lines 
		if not line: 
			continue

		else:
			start = line[3]
			end = line[4]
			

			print(start, end)

			#test wheter this is a CDS feature 

			#if it is CDS feature, then extract the substring/sequence

			#calculate and print GC content for that substring (2 decimal places)


#list for gene names
gene_names = []



# # read GFF file, line by line
# for line in gff:

# 	# remove line breaks
# 	line = line.rstrip('\n')
	
# 	# split each line on the tab character
# 	# sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')
# 	fields = line.split('\t')

# 	# split the attributes field (index = 8), each attribute is separated by ' ; '

# 	attributes = fields[8].split(' ; ')

# 	# we only need the first item in this list
# 	# print(attributes[0])
# 	gene_fields = attributes[0].split('Gene ')

# 	# print the gene name
# 	# print(gene_fields[1])

# 	# store the gene name
# 	gene_names.append(gene_fields[1])


	# extract the DNA sequence from the genome for this feature

	# print the DNA sequence for this feature

	# calculate the GC content for this feature, and print it to the screen

# print the genes in alphabetical order
# for gene in sorted(gene_names):
# 	print(gene)


#gff.close()

		



