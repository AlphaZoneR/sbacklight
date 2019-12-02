BACKLIGHT_DIRECTORY = '/sys/class/backlight/intel_backlight/'

def get_max_brightness():
	with open(BACKLIGHT_DIRECTORY + 'max_brightness', 'r') as f:
		return int(f.read())

def get_actual_brightness():
	with open(BACKLIGHT_DIRECTORY + 'actual_brightness', 'r') as f:
		return int(f.read())

def write_brightness(brightness_val):
	if brightness_val > 0 and brightness_val < get_max_brightness():
		with open(BACKLIGHT_DIRECTORY + 'brightness', 'w') as f:
			f.write(str(brightness_val))

def set_brightness_percentage(percent):
	if percent <= 0:
		percent = 1
	if percent > 100:
		percent = 100

	max_brightness = get_max_brightness()
	actual_brightness = get_actual_brightness()
	brightness_to_set = int(percent / 100 * max_brightness)
	if actual_brightness < brightness_to_set:
		for brightness in range(actual_brightness, brightness_to_set, 100):
			write_brightness(brightness)
	elif actual_brightness > brightness_to_set:
		for brightness in range(actual_brightness, brightness_to_set, -100):
			write_brightness(brightness)
import sys
import socket

if len(sys.argv) == 3:
	value = int(sys.argv[2])
	if sys.argv[1] == 'inc':
		set_brightness_percentage(current_brightness_percentage + value)
	elif sys.argv[1] == 'dec':
		set_brightness_percentage(current_brightness_percentage - value)
	elif sys.argv[1] == 'set':
		set_brightness_percentage(value)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('127.0.0.1', 62300))
s.listen(10)

while True:
	c, _ = s.accept()
	current_brightness_percentage = int(get_actual_brightness() / get_max_brightness() * 100)
	data = c.recv(1024).decode()
	try:
		command, value = data.split(' ')
		value = int(value)
		print(command, value)

		if command == 'inc':
			set_brightness_percentage(current_brightness_percentage + value)
		elif command == 'dec':
			set_brightness_percentage(current_brightness_percentage - value)
		elif command == 'set':
			set_brightness_percentage(value)
	except:
		pass
	print(get_actual_brightness() / get_max_brightness() * 100)
	c.close()
