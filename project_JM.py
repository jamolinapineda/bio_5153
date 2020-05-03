# /usr/bin/env python3

#Julio Molina Pineda - BIOL_5153
import csv
import argparse
from Bio import SeqIO 
import collections 

parser = argparse.ArgumentParser(description = "This script matches a Bar-seq sequence read to the barcode library")

# add postional arguments 
parser.add_argument("fastq", help="Sequence Read")
parser.add_argument("library", help="The barcode library")
# parse the arguments
args = parser.parse_args() 


# read and parse the FASTQ file 
file =  SeqIO.parse(args.fastq, 'fastq')

#prints the records id 
# for reads in file:
# 	print (reads.seq) #WORKS FINE UNTIL HERE
# create a list for later usage 
List = []
#use the fastq file plus read and parse the library (csv) file
for reads in file: 
	barcode_read = reads.seq
	with open(args.library, 'r') as library: 
		#create a csv reader object 
		reader = csv.reader(library, delimiter=",")
		for line in reader:
			#skip blank lines 
			if not line: 
				continue

			else:
				strain = line[0]
				barcode = line[1]
				#CREATE DICCTIONARY (BARCODE KEY, STRAIN VALUE)
				#dict_libr = {barcode:strain}
				#print(dict_libr)
				#print (strain)     #WORKS FINE UNTIL HERE
				# if fastq sequence == barcode then print 1
				if barcode_read == barcode:
					#print(strain) #Works until here 
					List.append(strain)

#print(List) #works fine until here
# creating a counter:
count = collections.Counter(List)
for strain2 in count:
	print ('%s : %d' % (strain2, count[strain2]))
					


				#for printing if doing dicctionary:
				# for st, bar in dict_libr.items():
				# 	if bar == barcode_read:
				# 		print(st)

# 				# count repeats and print strain + number of repeats (relative abundance(?))




