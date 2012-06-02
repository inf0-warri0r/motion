motion
======

motion sense security app for linux
------------------------------------

this app uses a webcam to sense motion and alert the owner by a sms. 
and also it also take two pictures of the motion. a HSDPA modem is used to send sms.

requirement:
----------------

python
python-wxgtk
python-opencv

use synaptic package manager to install them.

using the app:
---------------

go to the folder containing the files and run the "main.py" file or run,

python main.py 

command in terminal. then a window will appear. use "cam" button to see the video from cam. use it to mount the webcam. use "settings" button to set the number you want to sms, the activation timer, sensitivity and the usb port which modem is connected (ex : /dev/ttyUSB0 ). save it and use "Activate" button to activate. 


