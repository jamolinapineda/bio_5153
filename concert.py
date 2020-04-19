# /usr/bin/env python3
import re 

concert = "Katherine went to the concert to see Catheryn and the Cathryn’s. She ran into her friend Kathryn, who introduced Katherine to her friend Catherine. Together, they enjoyed the concert while texting inaudible snippets to their mutual friend, Kathrin. Their mercurial friend, katharine, felt left out."
print ("FullMatch\tStart\tEnd\tLenght")
print ("---------------------------------------------------------------")
for match in re.finditer("[KkC]ath(a)*(e)*r[iy]n(e)*('s)*", concert): 
	s = str(match.start())
	e = str(match.end()) 
	match_1 = match.group()
	match_lenght = str(len(match_1))
	# print(match.group() + " " + "Starts at: " + s  + " Ends at:" + e + " Size:" + match_lenght)
	print (match.group() + " " + "\t" + s + "\t" + e + "\t" + match_lenght)
print ("---------------------------------------------------------------")




# 	x = list('FullMatch,Start,End,lenght')
# 	y = list("12345678")
# 	table = []
# 	for i in x:
# 		row=[]
# 		for j in y:
# 			row.append(match.group())
# 			row.append(s)
# 			row.append(e)
# 			row.append(match_lenght)
# 		table.append(row)
# print(table) 