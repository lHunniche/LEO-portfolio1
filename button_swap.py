from gpiozero import Button
import os

button = Button(2)

while True:
	button.wait_for_press()
	os.system("python3 swap_state.py")
	button.wait_for_release()
