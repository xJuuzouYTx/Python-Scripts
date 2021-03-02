import keyboard
import win32api, win32con
import pyautogui
import time

#Automatizando tareas de AmongUs, adaptado a una pantalla de 1366x768

def mouse(xI, yI, xD, yD):
	win32api.SetCursorPos((xI,yI))
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.1)
	win32api.SetCursorPos((xD,yD))
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click(x,y):
	win32api.SetCursorPos((x,y))
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def delizarTargeta():
	win32api.SetCursorPos((560,590))
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	time.sleep(1)
	win32api.SetCursorPos((400,300))
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.1)
	for i in range(400, 1200,30):
		win32api.SetCursorPos((i,300))
		time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def recordar():
	if pyautogui.pixel(383, 343)[0] == r and  pyautogui.pixel(383, 343)[1] == g and  pyautogui.pixel(383, 343)[2] == b:
		time.sleep(0.2)
		click(800,343)
	if pyautogui.pixel(470, 343)[0] == r and  pyautogui.pixel(383, 343)[1] == g and  pyautogui.pixel(383, 343)[2] == b:
		time.sleep(0.2)
		click(800,343)
	if pyautogui.pixel(550, 343)[0] == r and  pyautogui.pixel(383, 343)[1] == g and  pyautogui.pixel(383, 343)[2] == b:
		time.sleep(0.2)
		click(800,343)
	if pyautogui.pixel(383, 425)[0] == r and  pyautogui.pixel(383, 343)[1] == g and  pyautogui.pixel(383, 343)[2] == b:
		time.sleep(0.2)
		click(800,343)
	if pyautogui.pixel(470, 425)[0] == r and  pyautogui.pixel(383, 343)[1] == g and  pyautogui.pixel(383, 343)[2] == b:
		time.sleep(0.2)
		click(800,343)
	if pyautogui.pixel(550, 425)[0] == r and  pyautogui.pixel(383, 343)[1] == g and  pyautogui.pixel(383, 343)[2] == b:
		time.sleep(0.2)
		click(800,343)
	if pyautogui.pixel(383, 495)[0] == r and  pyautogui.pixel(383, 343)[1] == g and  pyautogui.pixel(383, 343)[2] == b:
		time.sleep(0.2)
		click(800,343)
	if pyautogui.pixel(470, 495)[0] == r and  pyautogui.pixel(383, 343)[1] == g and  pyautogui.pixel(383, 343)[2] == b:
		time.sleep(0.2)
		click(800,343)
	if pyautogui.pixel(450, 495)[0] == r and  pyautogui.pixel(383, 343)[1] == g and  pyautogui.pixel(383, 343)[2] == b:
		time.sleep(0.2)
		click(800,343)
	
while keyboard.is_pressed('0')==False:
	try:
		if keyboard.is_pressed('1'):

			#Rojo
			if pyautogui.pixel(400, 190)[0] == 255 and  pyautogui.pixel(400, 190)[1] == 0 and  pyautogui.pixel(400, 190)[2] == 0:
				mouse(400, 190, 960, 195)
			elif pyautogui.pixel(400, 330)[0] == 255 and pyautogui.pixel(400, 330)[1] == 0 and pyautogui.pixel(400, 330)[2] == 0:
				mouse(400, 330, 960, 195)
			elif pyautogui.pixel(400, 460)[0] == 255 and pyautogui.pixel(400, 460)[1] == 0 and pyautogui.pixel(400, 460)[2] == 0:
				mouse(400, 460, 960, 195)
			elif pyautogui.pixel(400, 590)[0] == 255 and pyautogui.pixel(400, 590)[1] == 0 and pyautogui.pixel(400, 590)[2] == 0:
				mouse(400, 590, 960, 195)
			#Azul
			if pyautogui.pixel(400, 190)[2] == 255 and pyautogui.pixel(400, 190)[0] == 38 :
				mouse(400, 190, 960, 330)
			elif pyautogui.pixel(400, 330)[2] == 255 and pyautogui.pixel(400, 330)[0] == 38:
				mouse(400, 330, 960, 330)
			elif pyautogui.pixel(400, 460)[2] == 255 and pyautogui.pixel(400, 460)[0] == 38:
				mouse(400, 460, 960, 330)
			elif pyautogui.pixel(400, 590)[2] == 255 and pyautogui.pixel(400, 590)[0] == 38:
				mouse(400, 590, 960, 330)
			#Rosa
			if pyautogui.pixel(400, 190)[0] == 255 and pyautogui.pixel(400, 190)[2] == 255:
				mouse(400, 190, 960, 590)
			elif pyautogui.pixel(400, 330)[0] == 255 and pyautogui.pixel(400, 330)[2] == 255:
				mouse(400, 330, 960, 590)
			elif pyautogui.pixel(400, 460)[0] == 255 and pyautogui.pixel(400, 460)[2] == 255:
				mouse(400, 460, 960, 590)
			elif pyautogui.pixel(400, 590)[0] == 255 and pyautogui.pixel(400, 590)[2] == 255:
				mouse(400, 590, 960, 590)
			#Amarillo
			if pyautogui.pixel(400, 190)[0] == 255 and pyautogui.pixel(400, 190)[1] == 235:
				mouse(400, 190, 960, 460)
			elif pyautogui.pixel(400, 330)[0] == 255 and pyautogui.pixel(400, 330)[1] == 235:
				mouse(400, 330, 960, 460)
			elif pyautogui.pixel(400, 460)[0] == 255 and pyautogui.pixel(400, 460)[1] == 235:
				mouse(400, 460, 960, 460)
			elif pyautogui.pixel(400, 590)[0] == 255 and pyautogui.pixel(400, 590)[1] == 235:
				mouse(400, 590, 960, 460)
		if keyboard.is_pressed('2'):
			click(680,384)
		if keyboard.is_pressed('3'):
			delizarTargeta()
	#383 343
	#470 343
	#550 343
	except:
		print()




