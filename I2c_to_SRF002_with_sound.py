
import array
import smbus
import time
import datetime
import os
import random
import basic_classes
from basic_classes import SongCollection
import input_classes
from input_classes import i2cIn

Ranger = i2cIn(0x70, smbus.SMBus(1))
now = datetime.datetime.now()
played = False
seconds = 0
Folder = "/home/pi/turrets/TurretSounds"
InRangeSongs = SongCollection(Folder + "/InRange")
OutRangeSongs = SongCollection(Folder + "/OutOfRange")
DroppedSongs = SongCollection(Folder + "/Dropped")
PickedSongs = SongCollection(Folder + "/PickedUp")
FireSongs = SongCollection(Folder + "/Fire")
InRange = False
pickedUp = False
dropped = False
fire = False

	
while True:
	if played == True:
		seconds += 1
		if seconds >= 5:
			if InRange == True:
				FireSongs.PlaySong()
			if InRange == False:
				played = False
				seconds = 0
	
	Ranger.write(0x51)
	time.sleep(0.5)
	rng = Ranger.read()
	if rng > 0:
		if rng < 100:
			if played == False:
				InRangeSongs.PlaySong()
				played = True
				InRange = True
		else:
			if InRange == True:
				OutRangeSongs.PlaySong()
				InRange = False
				
	myFile = open('data ' + str(now) + '.txt', 'a')
	myFile.write(str(rng) + "\n")
	myFile.close()
