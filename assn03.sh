#!/bin/bash

# assn03-1
for i in {808..8008}; do echo "TR-$i"; done

# assn03-2
alias ls=‘ls -al’
alias less=‘less -SN’

# assn03-3
find ~/Desktop/gene_trees/ -name "*.fasta" | wc -l
# 15085 FASTA files 

# assn03-4 
find ~/Desktop/gene_trees/ -name "*.tre" | wc -l
# 14640 phylogenetic trees

# assn03-5 
find ~/Desktop/gene_trees/ -name "*.sched" | wc -l
15262 analyses have been run 

# assn03-06 
for f in *.fasta; do if [ "${f%.fasta}_raxml.tre" -nt "$f" ]; then mv "$f" ~/Desktop/gene_trees/fasta_done/ ; fi done | find ~/Desktop/gene_trees/ -name "*.fasta" | wc -l
#622

#assn03-07
find ~/Desktop/gene_trees/ -name "*.sched" | xargs grep "Program Return Code: 0" | wc -l
# 15217 successful runs (each file actually had “Program Return Code:0” twice)
# 45 unsuccessful runs 

#assn03-08 
For g in ~Desktop/gene_trees/*.fasta; do write_raxml_job_script.py $f > ${f%.fasta}.pbs; fi done