##############################################################################
#
# Author: Daniel Packer <dp@danielpacker.org>
#
# Simulation of bacterial hash function
#

from xorhash import byte_to_bin, xor_chain
import xorhashobj
import pygame
from pygame.locals import *
import random

# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)
pygame.init()

# Set the height and width of the screen
height=480
width=640
size=[width, height]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("xorsim")

#Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

font = pygame.font.Font(None, 30)

# center-align stuff
xoffset=width/2

reset=True # reset the plate

# create hasher object with random byte
bstr = byte_to_bin(-1)
bstrlist = list(bstr)
xo = xorhashobj.hasher(bstr, True, False, 8)

##########################################################################
# MAIN LOOP

step=0

colors_default = {
	0: black,	1: black,
	2: black,	3: black, 
	4: black,	5: black,
	6: black,	7: black
}
colors = {}
do_step = False
continuous = True

while done==False:
	for event in pygame.event.get(): # User did something
		if (event.type == KEYDOWN):
			print event
			if (event.key == K_ESCAPE):
				done = True
			elif (event.key==K_r):
				reset = True
			elif (event.key==K_SPACE):
				do_step = True
			elif (event.key==K_c):
				continuous = False if continuous else True
		if event.type == pygame.QUIT: # clicked close
			done=True # Flag that we are done, exit loop
	# Set the screen background
	screen.fill(black)

	if ((do_step == False) and (continuous == False)):
		continue
	else:
		do_step = False

	if (reset):
		print("Resetting")
		step=0
		xo.reset()
		colors = dict(colors_default)
		reset = False	

	xo.step()
	output = xo.output()
	colors[step] = green if output else red

	##################################################################
	# BEGIN DRAWING

	# draw agar plate
	pygame.draw.circle(screen, white, [width/2, height/2], height/2)

	# draw key
	text = font.render(str(int(xo.key())), True, black)
	screen.blit(text, [xoffset,20])
	pygame.draw.line(screen,black,[xoffset-50,50],[xoffset+50,50],5)

	# draw all the colonies
	for i in range(8):
		yoffset = (i+2) * 45
		text = font.render(bstrlist[i],True, black)
		screen.blit(text, [xoffset-50,yoffset-10])
		pygame.draw.circle(screen, colors[i],  [xoffset, yoffset], 20)
#screen, red if int(bstrlist[i]) else green, [xoffset, yoffset], 20)

	# END DRAWING
	##################################################################

	print("STEP: " + str(step))
	if (step==7):
		reset=True
	else:
		step +=1

	# Update screen 20 times/sec
	clock.tick(10)
	pygame.display.flip()

pygame.quit () # exit properly
