# /usr/bin/env python3
# define the input file
list = []
infile = "/Users/JAMP/Desktop/watermelon_files/watermelon.gff"
with open (infile, 'r') as myfile: 
	for line in myfile:
		gene = line.split() [10]
		
		if not gene == "similar":
			list.append(gene)
list.sort()
print (list)



		




#	list.append(lines)
# print(list[0], end = " ")


