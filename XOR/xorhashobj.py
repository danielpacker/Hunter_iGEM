##############################################################################
#
# Author: Daniel Packer <dp@danielpacker.org>
#
# Implements and tests an XOR hash function that takes a boolean key and 8bit 
# input to mimic the bacterial hash function found in the paper "Bacterial Hash 
# Function Using DNA-Based XOR Logic Reveals Unexpected Behavior of the LuxR 
# Promoter" -- http://www.ibc7.org/article/journal_v.php?sid=265
#
#


import random
import collections


# xor hash object for use in simulation
class hasher:
	def __init__(self, abyte="00000000", key=False, right2left=True, len=8):
		self.bytelist = list(abyte[::-1]) if (right2left) else list(abyte)
		self.key_orig = key
		self.key_new = key
		self.r2l = right2left
		self.len = len
		self.position = 0
		self.hash = []
	def step(self):
		#print("POSITION = " + str(self.position))
		if (self.position < self.len):
			bit = bool(int(self.bytelist[self.position]))
			self.key_new = bit ^ self.key_new
			self.hash.append(str(int(self.key_new)))
			self.position += 1
			return True
		else:
			return False
	def output(self):
		return self.key_new
	
	def hash(self):
		if (self.position == (len-1)):
			return self.hash
		else:
			print("Hash not fully computed!")
			return -1
	def reset(self):
		self.position = 0
		del self.hash[:]	
		self.key_new = self.key_orig
	def key(self):
		return self.key_orig
	
# /end xor hash object
