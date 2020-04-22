# /usr/bin/env python3

from collections import defaultdict
import csv

#declare the dictionary; key = codon, value = single-letter aa
codon2aa = defaultdict(dict)


# read tab delimeted file, line by line
with open('codons.tab', 'r') as codon_file: 

	#create a csv reader object 
	reader = csv.reader(codon_file, delimiter="\t")

	for line in reader:
		#skip blank lines 
		if not line: 
			continue

		elif line[0].startswith("#"):
			continue

		else:
			# print(line[0],line[2])
			codon2aa[line[0]] = line[2]

print ("codon_dict = {")
for codon, aa in codon2aa.items(): 
	print("'" + codon + "'" + ':' + "'" + aa + "'", end=", ")
print ('}')


		



