#Author :Tharindra Galahena
#Project:security app using webcam
#Date   :02/06/2012

tty = ""
tp = ""
timer=""
sen = ""

def trm(string, st):
	end = len(string) - 1;
	return string[st:end]
	

def read_settings(ini_path):
	global tty
	global tp
	global timer
	global sen
	
	file = open(ini_path);

	tty = file.readline()
	tp= file.readline()
	timer = file.readline()
	sen = file.readline()

	tty = trm(tty, 4)
	tp = trm(tp, 3)
	timer = trm(timer, 5)
	sen = trm(sen, 4)
	file.close()
	return (tty, tp, timer, sen)
	
def write_settings(ini_path, tty, tp, timer, sen):
	file = open(ini_path, "w");
	file.write("tty="+tty+"\n")
	file.write("tp="+tp+"\n")
	file.write("time="+timer+"\n")
	file.write("sen="+sen+"\n")
	file.close()
	
