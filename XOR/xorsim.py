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


def rendertext(font, text, pos=(0,0), color=(255,255,255), bg=(0,0,0)):
	lines = text.splitlines()
	#print(lines)
	#first we need to find image size...
	width = height = 0
	for l in lines:
		width = max(width, font.size(l)[0])
		height += font.get_linesize()
		#create 8bit image for non-aa text..
		img = pygame.Surface((width, height), 0, 8)
		img.set_palette([bg, color])
		#render each line
		height = 0
		for l in lines:
			t = font.render(l, 0, color, bg)
			img.blit(t, (0, height))
			height += font.get_linesize()
	return img

# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)
blue = (0, 0, 255)
grey = (150, 150, 150)
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
bigfont = pygame.font.Font(None, 40)
smallfont = pygame.font.Font(None, 24)

# center-align stuff
xoffset=width/2

reset=True # reset the plate

# create hasher object with random byte
bstr = byte_to_bin(-1)
bstrlist = list(bstr)
xo = xorhashobj.hasher(bstr, True, False, 8)

# text
ins_label = "Hit 'I' for instructions"
ins_full_text ="The following commands are available:\n\
  1     - Set key to True\n\
  0     - Set key to False\n\
  R     - Reset the hash\n\
  SPACE - Step through the hash one compuation at a time\n\
  c     - Toggle automatic mode (use SPACE to step)\n\
  ESC   - exit\n\
  \n\
  Press 'I' again to leave instructions"


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
outputs = {}
do_step = False
continuous = True
instructions = False

while done==False:
	for event in pygame.event.get(): # User did something
		if (event.type == KEYDOWN):
			print event
			if (event.key == K_ESCAPE):
				done = True
			elif (event.key==K_r):
				reset = True
			elif (event.key==K_SPACE):
				continuous = False
				do_step = True
			elif (event.key==K_c):
				continuous = False if continuous else True
			elif (event.key==K_i):
				instructions = False if instructions else True
			elif (event.key==K_0):
				reset = True
				xo.key(False)
			elif (event.key==K_1):
				reset=True
				xo.key(True)
		if event.type == pygame.QUIT: # clicked close
			done=True # Flag that we are done, exit loop
	# Set the screen background
	screen.fill(black)

	if (instructions):
		img = rendertext(font, ins_full_text, (0,0), white)
		screen.blit(img, [10,10])
		pygame.display.flip()
		continue

	if ((do_step == False) and (continuous == False)):
		continue
	else:
		do_step = False

	if (reset):
		print("Resetting")
		step=0
		xo.reset()
		colors = dict(colors_default)
		outputs = dict()
		reset = False	

	xo.step()
	output = xo.output()
	colors[step] = green if output else red
	outputs[step] = output

	##################################################################
	# BEGIN DRAWING

	# draw agar plate
	pygame.draw.circle(screen, white, [width/2, height/2], height/2)

	# draw instructions
	text = smallfont.render(ins_label, True, grey)
	screen.blit(text, [width-175, height-30])
	
	# draw key
	text = bigfont.render(str(int(xo.key())), True, blue)
	screen.blit(text, [xoffset-10,20])
	pygame.draw.line(screen,black,[xoffset-50,50],[xoffset+50,50],5)

	# draw all the colonies
	for i in range(8):
		yoffset = (i+2) * 45

		# highlight the input that's active
		if (i==step):
			text = bigfont.render(bstrlist[i],True, blue)
		else:
			text = font.render(bstrlist[i],True, black)
		screen.blit(text, [xoffset-50,yoffset-10])	

		# draw the colony the green for 1 and red for 0
		# and show the value in the circle	
		pygame.draw.circle(screen, colors[i],  [xoffset, yoffset], 20)
		outputtext = ""
		if (i in outputs):
			outputtext = str(int(outputs[i]))
		outputtext = font.render(outputtext,True, white)
		screen.blit(outputtext, [xoffset-10,yoffset-10])
#screen, red if int(bstrlist[i]) else green, [xoffset, yoffset], 20)

	# END DRAWING
	##################################################################

	print("STEP: " + str(step))
	if (step==7):
		reset=True
	else:
		step +=1

	# Update screen 20 times/sec
	clock.tick(2)
	pygame.display.flip()

pygame.quit () # exit properly
