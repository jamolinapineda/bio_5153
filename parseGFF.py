# /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO 


def get_args():
	# create an argument parser object
	parser = argparse.ArgumentParser(description = "This script parses a GFF file and does stuff with it")

	# add postional arguments 
	parser.add_argument("gff", help="the .gff file")
	parser.add_argument("fasta", help="the .fasta file")

	# parse the arguments
	return parser.parse_args()


def parse_fasta():
	# read and parse the FASTA file 
	return SeqIO.read(args.fasta, 'fasta')

def parse_gff(genome):
	# read GFF file, line by line
	with open(args.gff, 'r') as gff_file: 

		#create a csv reader object 
		reader = csv.reader(gff_file, delimiter="\t")

		for line in reader:
			#skip blank lines 
			if not line: 
				continue

			else:
				feature_type = line[2]
				start = int(line[3])
				end = int(line[4])
				strand = line[6]
				attributes = line[8]
				
				#test wheter this is a CDS feature 
				#if it is CDS feature, then extract the substring/sequence
				if feature_type == "CDS":
					#extract this feature from the genome
					feature_seq = genome[start-1:end]
				
					print(attributes)
					print(feature_seq)
					feature_GC = gc(feature_seq)
					print(round(feature_GC,2)) 

def gc(sequence): 
	#calculate and print the GC content for the substring (2 decimal)
	count_of_G = sequence.count('G')
	count_of_C = sequence.count('C')

	return(count_of_G + count_of_C)/len(sequence)

def main(): 
	genome_sequence = parse_fasta()
	parse_gff(genome_sequence.seq)

#get the command-line arguments before calling main()
args = get_args()


# execue the program by calling main 
if __name__ == "__main__": 
	main()

# # print(dir(genome))
# print(genome.description)
# print (len(genome.seq))
# print(genome.seq) 

				

			

			
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

		



