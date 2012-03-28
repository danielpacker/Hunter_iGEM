##############################################################################
#
# Author: Daniel Packer <dp@danielpacker.org>
#
# Simulation of bacterial hash function
#

from xorhash import byte_to_bin, xor_chain
import pygame
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
pygame.display.set_caption("My Game")
#Loop until the user clicks the close button.
done=False
# Used to manage how fast the screen updates
clock=pygame.time.Clock()

font = pygame.font.Font(None, 25)

# -------- Main Program Loop -----------

xoffset=width/2

while done==False:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done=True # Flag that we are done so we exit this loop
	# Set the screen background
	screen.fill(black)
	# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

	# draw agar plate
	pygame.draw.circle(screen, white, [width/2, height/2], height/2)

	text = font.render("key", True, black)
	screen.blit(text, [xoffset,20])
	pygame.draw.line(screen,black,[xoffset-50,50],[xoffset+50,50],5)
	bstrlist = list(byte_to_bin(-1))

	for i in range(8):	
		yoffset = (i+2) * 45
		text = font.render(bstrlist[i],True, black)
		screen.blit(text, [xoffset-50,yoffset])
		pygame.draw.circle(screen, red if int(bstrlist[i]) else green, [xoffset, yoffset], 20)

	# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
	# Limit to 20 frames per second
	clock.tick(20)
	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
# Be I	DLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
