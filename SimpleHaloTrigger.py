import keyboard
import pyautogui
import time
import win32api, win32con

def click():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
	try:
		if pyautogui.pixel(640,390)[0] > 250:
			click()
		if pyautogui.pixel(399,299)[0] > 250:
			click()
	except:
		print()

		