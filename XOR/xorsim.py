##############################################################################
#
# Author: Daniel Packer <dp@danielpacker.org>
#
# Simulation of bacterial hash function
#

from xorhash import byte_to_bin, xor_chain
import pygame
from pygame.locals import *

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

font = pygame.font.Font(None, 25)

# center-align stuff
xoffset=width/2

##########################################################################
# MAIN LOOP


while done==False:
	for event in pygame.event.get(): # User did something
		if (event.type == KEYUP) or (event.type == KEYDOWN):
			print event
			if (event.key == K_ESCAPE):
				done = True
		if event.type == pygame.QUIT: # clicked close
			done=True # Flag that we are done, exit loop
	# Set the screen background
	screen.fill(black)

	##################################################################
	# BEGIN DRAWING

	# draw agar plate
	pygame.draw.circle(screen, white, [width/2, height/2], height/2)

	text = font.render("key", True, black)
	screen.blit(text, [xoffset,20])
	pygame.draw.line(screen,black,[xoffset-50,50],[xoffset+50,50],5)
	bstr = byte_to_bin(-1)
	bstrlist = list(bstr)
	hash = []
	for i in range(8):	
		yoffset = (i+2) * 45
		text = font.render(bstrlist[i],True, black)
		screen.blit(text, [xoffset-50,yoffset])
		pygame.draw.circle(screen, red if int(bstrlist[i]) else green, [xoffset, yoffset], 20)

	# END DRAWING
	##################################################################

	# Update screen 20 times/sec
	clock.tick(20)
	pygame.display.flip()

pygame.quit () # exit properly
