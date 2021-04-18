from pynput.keyboard import Key, Listener
from a import *
from b import *
import re
import sys
from pynput.keyboard import Key, Listener
from myftp import *

import os
if not os.path.exists("human_faces1"):
    os.makedirs("human_faces1")
if not os.path.exists("human_faces2"):
    os.makedirs("human_faces2")
while True:
	ftp_files=list_files()
	for file in ftp_files:
		if not os.path.exists("./human_faces2/"+file):
			download_from_ftp(file)
	c=int(raw_input("Enter: 1)add_faces 2)log attendence 0)exit\t"))
	if(c==1):
		add_member()
	elif(c==2):
		while True:
			#k = cv2.waitKey(1000) #run with 500 milisec gap
			print("---------------")
			a=raw_input("Continue Y(Enter)/N\t")
			print("---------------")
			if(a=='y' or a=='Y' or a==""):
				log_member()
			elif(a=='n' or a=='N'):
				  break
	elif(c==0):
		exit(1)
	else:
		print("invalid choice")