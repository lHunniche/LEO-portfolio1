from gpiozero import LED
from gpiozero import Button
from time import sleep

green = LED(22)
yellow = LED(27)
red = LED(17)

state = open("state.txt", "w")
state.write("0")
state.close()

may_drive = False
red.on()

def trans_to_red():
	green.off()
	yellow.on()
	sleep(2)
	yellow.off()
	red.on()

def trans_to_green():
	yellow.on()
	sleep(2)
	red.off()
	yellow.off()
	green.on()

def check_for_change():
	global may_drive
	file = open("state.txt", "r")
	state = file.readline()

	if state == "0" and may_drive:
		#trans to red
		trans_to_red()
		may_drive = False
	elif state == "1" and not may_drive:
		#trans to green
		trans_to_green()
		may_drive = True
	file.close()

while True:
	check_for_change()
	sleep(0.1)
