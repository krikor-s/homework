#!/usr/bin/env python3

#Horizontal Gene Transfer

#One way to find genes that have been recently added to a genome is to look 
#for outliers in codon usage. Using a GenBank file for a complete bacterial 
#genome (e.g. E. coli), compute the average codon usage of a genome and then
# compare individual genes to the genome as a whole. Outliers in codon usage
#bias could be genes that used to reside in a different genome.

#Use regex to parse the GenBank File
#Store codon usage frequencies as dictionaries
#Compare individual frequencies to the whole genome frequency
#Use K-L or Manhattan distance for comparisons

import sys
import argparse
import mcb185 as mcb

parser = argparse.ArgumentParser(description='Horizontal Gene Transfer')
parser.add_argument('--genome', required = True, type=str, metavar='<str>', 
    help = 'required gene file')
parser.add_argument('--thresh', required=True, type=float, metavar='<float>',
    help='required Manhattan distance')
arg = parser.parse_args()

genome = arg.genome
manhat = arg.thresh
afterorigin = False
seq = ''
genecoords = {}
with open(genome) as fp:
    for line in fp.readlines():
        line = line.rstrip()
        if ' gene ' in line:
            if 'complement' in line: continue
            lnsplit = line.split() #Find the gene coords and rid of words
            name = lnsplit[1]
            coords = name.split("..") #rid of .. between
            beg = int(coords[0])-1
            end = int(coords[1])
            assert(name not in genecoords)
            genecoords[name] = (beg, end)
        if 'ORIGIN' in line: #Link the seq start after ORIGIN
            afterorigin = True
        if afterorigin:
            words = line.split()
            seq += ''.join(words[1:])

geneseq = {}
totalcodons = {}
for k, v in genecoords.items(): #creating total genome codons frequencies
    gene = seq[v[0]:v[1]]
    geneseq[k] = gene
    totalcodons = mcb.codfreq(totalcodons, gene)

totcodons = 0 #calculate probabilities for codons in total genome
for k, v in totalcodons.items(): totcodons += v
for k, v in totalcodons.items(): totalcodons[k] = v/totcodons

for gc, gs in geneseq.items(): #calculate totale frequencies and
    indfreq = {}               #probabilities in individual genomes
    indfreq = mcb.codfreq(indfreq, gs)
    indtot = 0
    for ic, icount in indfreq.items(): indtot += icount
    for ic, icount in indfreq.items(): indfreq[ic] = icount/indtot
    distance = mcb.manhat(totalcodons, indfreq)
    if distance > manhat: print(gc)

#if # between 0 and 1.8 is given for Manhattan distance, this will spit out
#a coordinate of a potential gene that was a product of HGT.

#When given a genebank e.coli sequence this code will extract genes and link
#said genes to a their coordinates. It will then calculate the frequency and
#probability of each codon in the gene and compare with a Manhattan distance,
#provided by the user, to attempt to understand genes could have been a 
#product of HGT