#!/usr/python

from pushbullet import PushBullet
from subprocess import call
import time

pb = PushBullet('KEY_HERE')
while True:
	call(["streamer","-f", "jpeg", "-o","image.jpeg"])
	with open("image.jpeg", "rb") as pic:
   		success, file_data = pb.upload_file(pic, "picture.jpg")

	success, push = pb.push_file(**file_data)
	time.sleep(600)

