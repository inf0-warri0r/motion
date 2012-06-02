#!/usr/bin/python

#Author :Tharindra Galahena
#Project:security app using webcam
#Date   :02/06/2012

import thread
import ui
import motion
import pygame
from pygame.locals import *

def start_th(w, num, tty, sen):
    
    thread.start_new_thread( motion.activate, (set_label, set_message, get_con, w, num, tty, sen, ))	
	
       
def start_cam():
	 
    thread.start_new_thread( cam, (set_label, 2, ))	

       
app = ui.Main()
app.set_fu(start_th, start_cam)

def cam(a, b):
	res = (640,480)
	pygame.init()
	screen = pygame.display.set_mode((640,480))
	pygame.display.set_caption('Cam')
	pygame.font.init()
	f = False
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
				f = True
		if f: 
			app.set_cam()
			break
		sr = motion.get_image()
		camshot = pygame.image.frombuffer(sr.tostring(), res, "RGB")
		screen.blit(camshot, (0,0))
		pygame.display.flip()
		
def get_con():
	return app.get_con()		
def set_label(a):
	app.set_button_label(a)
def set_message(a):
	app.set_entry(a)
app.MainLoop()
