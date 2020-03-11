# /usr/bin/env python3

# define the input file 
infile = "/Users/jamolina/Desktop/bio_5153/shaver_etal.csv"

# open and parse 

with open(infile, 'r') as shaver: 
	for line in shaver:
		line = line.rstrip("\n")
		fields = line.split("\t")
		if(fields[3] == 'Stepps'):
			# print(fields[3], fields[7], fields[8])
			print ('\t' .join([fields[3], fields[7], fields [8]]))