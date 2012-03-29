##############################################################################
#
# Author: Daniel Packer <dp@danielpacker.org>
#
# Implements and tests an XOR hash function that takes a boolean key and 8bit 
# input to mimic the bacterial hash function found in the paper "Bacterial Hash 
# Function Using DNA-Based XOR Logic Reveals Unexpected Behavior of the LuxR 
# Promoter" -- http://www.ibc7.org/article/journal_v.php?sid=265
#

import random
import collections


# Run an xor chain on a given binary string with a given boolean key
# You can specify # of bits and direction in which to XOR the bitstring
def xor_chain(abyte="00000000", key=False, right2left=True, len=8):
	bytelist = list(abyte[::-1]) if (right2left) else list(abyte)
	hash = list()
	for i in range(len):
		#print(bytelist[i])
		bit = bool(int(bytelist[i]))
		#print("bit: " + str(bit))
		key = bit ^ key
		#print("key: " + str(key))
		hash.append(str(int(key)))
	#print("\n")
	return "".join(hash)

# convert byte (int from 0..255) to binary string
def byte_to_bin(rbyte=-1):
	# Generate random byte
	if (rbyte==-1):
		rbyte = random.randint(0,255)
	# format as binary string for output
	rbyte_str = "{0:08b}".format(rbyte)
	return rbyte_str


# make sure function is 1:1 for all possible bytes
def check():
	keyvals = {}
	for b in [False, True]:
		for d in [False, True]:
			#print("Testing for key=" + str(b) + "\n")
			for i in range(255):
				bstr = byte_to_bin(i)
				keyvals[bstr] = xor_chain(bstr, b, d)
			c = collections.Counter(keyvals.values())
			#print(keyvals)
			duplicates = [i for i in c if c[i]>1]
			numduplicates = len(duplicates)
			if (numduplicates):
				print("DUPLICATES FOUND: " + str(duplicates))
			else:
				print("hash works for all bytes with key="+str(b)+" with right to left="+str(d))
			numoriginals = len(keyvals.values())
			print("(number of originals: " + str(numoriginals) + " number of duplicates: " + str(numduplicates) + ")\n")	
