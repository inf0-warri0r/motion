import Image
import sys
#import Image
import sys, os
import wx
import time
import opencv
import thread
from PIL import Image
from opencv import highgui 
import threading
import os
import datetime
import settings

class Main(wx.App):
  
   def OnInit(self):
       self.tty, self.tp, self.timer, self.sen = settings.read_settings("setings")
       window = wx.Frame(None, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
       self.settings_window = wx.Frame(window, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
       window.SetTitle("inf0_warri0r - motion")
       window.SetSize((300, 150))
       window.Bind(wx.EVT_CLOSE,self.destroy)
       panel = wx.Panel(window)
       
       
       img = wx.Image("headder.jpg", wx.BITMAP_TYPE_ANY)
       imageCtrl = wx.StaticBitmap(panel, wx.ID_ANY,
                                         wx.BitmapFromImage(img))
       imageCtrl.SetBitmap(wx.BitmapFromImage(img))
       panel.Refresh()
        
        
       main_box = wx.BoxSizer(wx.VERTICAL)
       main_box.Add(panel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
       button_box = wx.BoxSizer(wx.HORIZONTAL)
       self.cam_button = wx.Button(window,label="Cam")
       self.cam_button.Bind(wx.EVT_BUTTON, self.play)
       button_box.Add(self.cam_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4) 
       self.active_button = wx.Button(window,label="Activate")
       self.active_button.Bind(wx.EVT_BUTTON, self.toggle_active)
       button_box.Add(self.active_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
       self.settings_button = wx.Button(window,label="Settings")
       button_box.Add(self.settings_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
       self.settings_button.Bind(wx.EVT_BUTTON, self.settings)   
       main_box.Add(button_box, 0, wx.EXPAND, 0)
       
       message_box = wx.BoxSizer(wx.VERTICAL)
       self.message_entry = wx.TextCtrl(window, size=(280, -1), name="a")
       self.message_entry.SetValue("---------------------")
       message_box.Add(self.message_entry, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
       main_box.Add(message_box, 0, wx.EXPAND, 0)

       window.SetSizer(main_box)
       window.Layout()
       window.Show()
       self.SetTopWindow(window)
       self.f = True
       self.f2 = True
       self.set_f = False
       return True
   
   def settings(self, event):
      
      if self.set_f == False:
		   
           self.settings_window.SetTitle("Settings")
           self.settings_window.SetSize((450, 300))
           self.settings_window.Bind(wx.EVT_CLOSE,self.settings)
 
           main_box = wx.BoxSizer(wx.VERTICAL)
           
           up_box = wx.BoxSizer(wx.VERTICAL)
           headder_text = wx.StaticText(self.settings_window, -1, "Settings")
           up_box.Add(headder_text, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
           tty_text = wx.StaticText(self.settings_window, -1, "tty")
           up_box.Add(tty_text, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
           self.tty_entry = wx.TextCtrl(self.settings_window, size=(405, -1), name="a")
           self.tty_entry.SetValue(self.tty)
           up_box.Add(self.tty_entry, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
           main_box.Add(up_box, 0, wx.EXPAND, 0)
            
           middle_box = wx.BoxSizer(wx.HORIZONTAL)
           box1 = wx.BoxSizer(wx.VERTICAL)
           time_text = wx.StaticText(self.settings_window, -1, "Time")
           box1.Add(time_text, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
           self.timer_entry = wx.TextCtrl(self.settings_window, size=(200, -1), name="a")
           self.timer_entry.SetValue(self.timer)
           box1.Add(self.timer_entry, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
           middle_box.Add(box1, 0, wx.EXPAND, 0)

           
           box2 = wx.BoxSizer(wx.VERTICAL)
           number_text = wx.StaticText(self.settings_window, -1, "Number")
           box2.Add(number_text, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
           self.tp_entry = wx.TextCtrl(self.settings_window, size=(200, -1), name="a")
           self.tp_entry.SetValue(self.tp)
           box2.Add(self.tp_entry, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
           middle_box.Add(box2, 0, wx.EXPAND, 0)
           
           main_box.Add(middle_box, 0, wx.EXPAND, 0)
           
           down_box = wx.BoxSizer(wx.VERTICAL)
           sen_text = wx.StaticText(self.settings_window, -1, "Sensitivity")
           down_box.Add(sen_text, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
           p = 120
           try:
               p = int(self.sen)
           except:		
               print "aa"
           self.sen_sld = wx.Slider(self.settings_window, value=p, minValue=100, maxValue=200, pos=(20, 20), size=(405, -1), style=wx.SL_HORIZONTAL, name="sencitive")
           down_box.Add(self.sen_sld, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
           main_box.Add(down_box, 0, wx.EXPAND, 0)
           
           buttons_box = wx.BoxSizer(wx.HORIZONTAL)
           self.save_button = wx.Button(self.settings_window,label="Save")
           self.save_button.Bind(wx.EVT_BUTTON, self.save)
           buttons_box.Add(self.save_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
           self.cancle_button = wx.Button(self.settings_window,label="Cancle")
           self.cancle_button.Bind(wx.EVT_BUTTON, self.settings)
           buttons_box.Add(self.cancle_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
           
           main_box.Add(buttons_box, 0, wx.EXPAND, 0)
           

           self.settings_window.SetSizer(main_box)
           self.settings_window.Layout()
           self.settings_window.Show()
           self.SetTopWindow(self.settings_window)
           self.set_f = True
      else:
           self.settings_window.Show(show=False)
           self.set_f = False
   
   def save(self, event):
	   self.tty = str(self.tty_entry.GetValue())
	   self.timer = str(self.timer_entry.GetValue())
	   self.tp = str(self.tp_entry.GetValue())
	   self.sen = str(self.sen_sld.GetValue())
	   
	   settings.write_settings("setings", self.tty, self.tp, self.timer, str(self.sen))
   def get_con(self):
	   return self.f
   def set_fu(self, th_func, th_cam):
	   self.thf = th_func   
	   self.thc = th_cam 
	    
   def play(self,event):
	   if self.f2:
            self.f2 = False
            self.thc()
			
   def toggle_active(self,event):
        if self.f:
			self.f = False
			self.thf(self.timer, self.tp, self.tty, self.sen);
        else:
			self.active_button.SetLabel("Activate")
			self.f = True
        print "a"  
   def set_cam(self):
	   self.f2 = True
   def set_button_label(self, a):
	   self.active_button.SetLabel(a)
   def set_entry(self, a):
	   self.message_entry.SetValue(a)
	   self.message_entry.Refresh()
   def destroy(self,event):
       self.f = False
       event.Skip()
       exit(0)
