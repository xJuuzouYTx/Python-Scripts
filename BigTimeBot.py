from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

listax=[]
listay=[]

while keyboard.is_pressed('q') == False:
	try:
		y=206
		if pyautogui.pixel(512,y)[2] == 255:
			listax.append(512)
			listay.append(y)
		if pyautogui.pixel(566,y)[2] == 255:
			listax.append(566)
			listay.append(y)
		if pyautogui.pixel(613,y)[2] == 255:
			listax.append(613)
			listay.append(y)
		if pyautogui.pixel(653,y)[2] == 255:
			listax.append(653)
			listay.append(y)
		if pyautogui.pixel(710,y)[2] == 255:
			listax.append(710)
			listay.append(y)
		if pyautogui.pixel(758,y)[2] == 255:
			listax.append(758)
			listay.append(y)
		if pyautogui.pixel(815,y)[2] == 255:
			listax.append(815)
			listay.append(y)

		y=260
		if pyautogui.pixel(512,y)[2] == 255:
			listax.append(512)
			listay.append(y)
		if pyautogui.pixel(266,y)[2] == 255:
			listax.append(266)
			listay.append(y)
		if pyautogui.pixel(613,y)[2] == 255:
			listax.append(613)
			listay.append(y)
		if pyautogui.pixel(653,y)[2] == 255:
			listax.append(653)
			listay.append(y)
		if pyautogui.pixel(710,y)[2] == 255:
			listax.append(710)
			listay.append(y)
		if pyautogui.pixel(758,y)[2] == 255:
			listax.append(758)
			listay.append(y)
		if pyautogui.pixel(815,y)[2] == 255:
			listax.append(815)
			listay.append(y)

		y=306
		if pyautogui.pixel(512,y)[2] == 255:
			listax.append(512)
			listay.append(y)
		if pyautogui.pixel(266,y)[2] == 255:
			listax.append(266)
			listay.append(y)
		if pyautogui.pixel(613,y)[2] == 255:
			listax.append(613)
			listay.append(y)
		if pyautogui.pixel(653,y)[2] == 255:
			listax.append(653)
			listay.append(y)
		if pyautogui.pixel(710,y)[2] == 255:
			listax.append(710)
			listay.append(y)
		if pyautogui.pixel(758,y)[2] == 255:
			listax.append(758)
			listay.append(y)
		if pyautogui.pixel(815,y)[2] == 255:
			listax.append(815)
			listay.append(y)

		y=345
		if pyautogui.pixel(512,y)[2] == 255:
			listax.append(512)
			listay.append(y)
		if pyautogui.pixel(266,y)[2] == 255:
			listax.append(266)
			listay.append(y)
		if pyautogui.pixel(613,y)[2] == 255:
			listax.append(613)
			listay.append(y)
		if pyautogui.pixel(653,y)[2] == 255:
			listax.append(653)
			listay.append(y)
		if pyautogui.pixel(710,y)[2] == 255:
			listax.append(710)
			listay.append(y)
		if pyautogui.pixel(758,y)[2] == 255:
			listax.append(758)
			listay.append(y)
		if pyautogui.pixel(815,y)[2] == 255:
			listax.append(815)
			listay.append(y)

		y=404
		if pyautogui.pixel(512,y)[2] == 255:
			listax.append(512)
			listay.append(y)
		if pyautogui.pixel(266,y)[2] == 255:
			listax.append(266)
			listay.append(y)
		if pyautogui.pixel(613,y)[2] == 255:
			listax.append(613)
			listay.append(y)
		if pyautogui.pixel(653,y)[2] == 255:
			listax.append(653)
			listay.append(y)
		if pyautogui.pixel(710,y)[2] == 255:
			listax.append(710)
			listay.append(y)
		if pyautogui.pixel(758,y)[2] == 255:
			listax.append(758)
			listay.append(y)
		if pyautogui.pixel(815,y)[2] == 255:
			listax.append(815)
			listay.append(y)

		y=453
		if pyautogui.pixel(512,y)[2] == 255:
			listax.append(512)
			listay.append(y)
		if pyautogui.pixel(266,y)[2] == 255:
			listax.append(266)
			listay.append(y)
		if pyautogui.pixel(613,y)[2] == 255:
			listax.append(613)
			listay.append(y)
		if pyautogui.pixel(653,y)[2] == 255:
			listax.append(653)
			listay.append(y)
		if pyautogui.pixel(710,y)[2] == 255:
			listax.append(710)
			listay.append(y)
		if pyautogui.pixel(758,y)[2] == 255:
			listax.append(758)
			listay.append(y)
		if pyautogui.pixel(815,y)[2] == 255:
			listax.append(815)
			listay.append(y)

		y=509
		if pyautogui.pixel(512,y)[2] == 255:
			listax.append(512)
			listay.append(y)
		if pyautogui.pixel(266,y)[2] == 255:
			listax.append(266)
			listay.append(y)
		if pyautogui.pixel(613,y)[2] == 255:
			listax.append(613)
			listay.append(y)
		if pyautogui.pixel(653,y)[2] == 255:
			listax.append(653)
			listay.append(y)
		if pyautogui.pixel(710,y)[2] == 255:
			listax.append(710)
			listay.append(y)
		if pyautogui.pixel(758,y)[2] == 255:
			listax.append(758)
			listay.append(y)
		if pyautogui.pixel(815,y)[2] == 255:
			listax.append(815)
			listay.append(y)
		
		
		time.sleep(1.3)
		for i in range(len(listax)):
			print(listax)
			click(listax[i],listay[i])
		listax=[]
		listay=[]
	except:
		print('e')