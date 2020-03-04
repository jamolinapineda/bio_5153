#! /usr/bin/env python3
my_file = open("/Users/jamolina/Desktop/bio_5153/p4b_chp03/dna.txt", "r")
dna = my_file.read()
my_dna = dna.upper()
# print(my_dna)
lenght = len(my_dna)
# print (lenght)
A_count = my_dna.count('A')
T_count = my_dna.count('T')
C_count = my_dna.count('C')
G_count = my_dna.count('G')
# print (A_count)
A_percentage = (A_count / float(lenght)) * 100
C_percentage = (C_count / float(lenght)) * 100
T_percentage = (T_count / float(lenght)) * 100
G_percentage = (G_count / float(lenght)) * 100
A = round(A_percentage,2)
G = round(G_percentage,2)
C = round(C_percentage,2)
T = round(T_percentage,2)
print ("Percentage A: " + str(A) + "%")
print ("Percentage T: " + str(T) + "%")
print ("Percentage C: " + str(C) + "%")
print ("Percentage G: " + str(G) + "%")
