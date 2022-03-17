#!/usr/bin/env python3
# 61dust.py

import argparse
from fileinput import filename
import mcb185 as mcb

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(description='Outputs of masked low entropy sequence.')
# required arguments
parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='required FASTA file')
parser.add_argument('--wins', required=True, type=int,
	metavar='<int>', help='required window size')
parser.add_argument('--ethresh', required=True, type=float,
	metavar='<float>', help='required entropy threshold')
# switches
parser.add_argument('--lowercase', action='store_true',
	help='lowercase or N based masking. N-based default')
# finalization
arg = parser.parse_args()

file = arg.fasta
wins = arg.wins
ethresh = arg.ethresh
lcase = arg.lowercase

for name, seq in mcb.read_fasta(file):
	seq = seq.upper()
	#create mask sequence
	output = ''
	for i in range(0, len(seq)-wins+1, 1):
		prob = mcb.ntprobs(seq[i:i+wins])
		entropy = mcb.e_calc(prob)
		if entropy > ethresh:
			output += seq[i]
		else:
			if lcase:
				output += seq[i].lower()
			else:
				output += 'n' 
	output += seq[-wins+1:]
	#output fasta file
	print(f'>{name}')
	for i in range(0, len(output), 60):
		print(output[i:i+60])