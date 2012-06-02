#Author :Tharindra Galahena
#Project:security app using webcam
#Date   :02/06/2012

import datetime
import time
import opencv
from PIL import Image
from opencv import highgui 
import sms

camera = highgui.cvCreateCameraCapture(-1)
def get_image():

    im = highgui.cvQueryFrame(camera)
    im = opencv.cvGetMat(im)
    return opencv.adaptors.Ipl2PIL(im) 


def check(pix, pix2, w1, w2, h1, h2):
	i = 0
	c = 0
	m = 60
	for x in range(w1, w2):
		for y in range(h1, h2):
			if i >= 10 :
				r = pix[x,y][0]
				r2 = pix2[x,y][0]
				if r - r2 > m :
					c = c + 1
				else:
					if r - r2 < -1 *m:
						c = c + 1	
				i = 0
			else:
				i = i + 1
	return c

def activate(set_label, set_message, get_con, b, num, tty, sens):
	
	w = 15
	sen = 180
	try:
		w = int(b)
	except:		
			print "error"
	try:
		sen = 300 - int(sens)
	except:		
			print "error"
	tp_num = num
	
	set_label("waiting")
	for i in range(0,w):
		time.sleep(1)
		set_label(str(w - i))
		
	set_label("Disactivate")
	camshot2 = get_image()
	camshot_old = get_image()
	cnt = 0
	cnt2 = 0
	f = 0
	while 1:
		
		s = get_con()
		if s:
			break
		min_x = 5
		min_y = 3	
		max_x = 0
		max_y = 0
		try:
			camshot2 = get_image()
			camshot = camshot2 

			pix2 = camshot.load();
			pix_old = camshot_old.load();
		except:
			continue
		width, height = camshot2.size
		i = 0
		l = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
		
		for p in range(4):
			for q in range(6):
				l[p][q] = check(pix2, pix_old, q*width/6, (q + 1)*width/6, p*height/4, (p + 1)*height/4)
		for y in range(0,4):
			for x in range(0,6):
				if l[y][x] > sen:
					if min_x > x:
						min_x = x
					if min_y > y:
						min_y = y
					if max_x < x:
						max_x = x
					if max_y < y:
						max_y = y

		w1 = (width/6)*min_x
		w2 = (width/6)*(max_x + 1)
		h1 = (height/4)*min_y
		h2 = (height/4)*(max_y + 1)
		
		if (h2 - h1 >= height /4 or w2 - w1 >= width/4):
			f = 1
			cnt = cnt + 1
			if cnt == 1:
				tmp = camshot
			if cnt > 1:
				save_images(tmp, camshot)
				set_message("motion detected!!!")
				cnt = 0
				cnt2 = 0
				f = 0
				sms.send_sms(num, tty)
				time.sleep(5)
				set_message("---------------------")
		if f:
			cnt2 = cnt2 + 1 
			if cnt2 >= 10 and cnt < 2:
				f = False
				cnt = 0
				cnt2 = 0
		try:		
			camshot_old = camshot2
		except:
			continue	
		time.sleep(0.1)


def save_images(tmp, camshot):
	stamp = str(datetime.datetime.now())
	extension = ".jpg"
	directry = "img/"
	filename = directry + stamp + " 1 " + extension
	tmp.save(filename, "JPEG")
	filename = directry + stamp + " 2 " + extension
	camshot.save(filename, "JPEG")
