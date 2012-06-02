#Author :Tharindra Galahena
#Project:security app using webcam
#Date   :02/06/2012

import os
import serial
 
def sms_alert(num, tty):
	try:
		ser = serial.Serial(tty, 19200, timeout=5)
		ser.open()
		ser.write('ATZ\r')
		ser.write('AT+CMGF=1\r')
		ser.write('AT+CMGS=\"'+ num +'\"\r')
		ser.write('intruder alert!!!\n')
		ser.write(chr(26))
		#line = ser.readline() 
		#print line
		ser.close()
	except Exception, e:
		raise e
		print "error"
	


def send_sms(num, tty):
	p = os.fork()
	if p == 0:
		 sms_alert(num, tty)
		 exit(0)
	else:
		os.system("sleep 0.5")
		
		

