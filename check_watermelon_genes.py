#! /usr/bin/env python3

# load required modules
import re
import sys
import os 
import csv 

query = 'watermelon_genes.fa'
reference_set = 'watermelon_reference_genes.fa'

parts = query.split('.')
base_filename = parts[0]

blast_output = base_filename + ".blastn" 
blast_error = base_filename + ".err"                             
blast_command = "blastn -query " + query + " -subject " + reference_set + " -outfmt '6 qseqid sseqid pident qcovs'" + " -max_target_seqs 1" + " > " + blast_output + " 2>" + blast_error

#print(blast_command)

#execute the blast search
os.system(blast_command)

#parse the blast output 
# read GFF file, line by line
with open(blast_output, 'r') as blastout: 

	#create a csv reader object 
	reader = csv.reader(blastout, delimiter="\t")
	for line in reader:
		if float(line[2]) == 100 and float(line[3]) == 100: 
			print('-OK')
		else:
			print (line [0], line[1], "are a problem")
