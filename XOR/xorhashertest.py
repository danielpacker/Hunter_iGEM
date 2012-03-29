import xorhashobj

x = xorhashobj.hasher("00000000", True, True, 8)

i=0

while (x.step()):
	i+=1
	output = x.output()
	print("Step " + str(i) + ": " + str(int(output)))

x.reset() # now can start again

i=0

while (x.step()):
	i+=1
	output = x.output()
	print("Step " + str(i) + ": " + str(int(output)))

