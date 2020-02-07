#! /Bin/Bash 

#assn01-01
find ~/ -name “nad*” 

#assn01-02 
top
#the command is using 0% of the CPU 
#The information from processes and memory was found using the top command: MemRegions: 140917 total, 1069M resident, 51M private, 375M shared. PhysMem: 4079M used (1473M wired), 16M unused.


#assn01-03
grep misc_feature ~/Desktop/Watermelon_files/watermelon.gff | sort -k7gr > IR_regions.gff


#assn01-04
grep misc_feature ~/Desktop/Watermelon_files/watermelon.gff | grep -c chloroplast
grep misc_feature ~/Desktop/Watermelon_files/watermelon.gff | grep -vc chloroplast
#the IR sequences can be identified since they are annotated as ‘misc_feature’
#IR fragments from inside the chloroplast have the word chloroplast in the comments
#There are more fragments (28) coming from the inside of the chloroplast IR as compared to the outside (9) 

#assn01-05
grep GGATCC ~/Desktop/Watermelon_files/watermelon_nt/*.fasta > with_BamHI
grep -v GAATTC ~/Desktop/Watermelon_files/watermelon_nt/with_BamHI > BamHI_no_EcoRV | less -FX BamHI_no_EcoRV


#assn01-06
cat ~/Desktop/example_files/shaver_etal.csv | head -n1000 | tail -n500

#assn01-07
sort -k2,2r -k3,3 ~/Desktop/example_files/fruit.txt | column -t