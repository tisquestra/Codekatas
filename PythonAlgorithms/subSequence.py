from itertools import combinations


def find_longest_sequence(sequence):

	for seqLen in range(len(sequence), 0, -1): # our given subsequence length
		#find all ordered combinations within that subsequence that have that length
		for sub in combinations(sequence, seqLen):
			if list(sub) == sorted(sub):
				print sub
				return sub
				

find_longest_sequence([3, 1, 0, 2, 4])
		