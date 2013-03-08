import array
import time
import datetime
import os
import random
import RPi.GPIO as GPIO

#class SerialIn(object):

class i2cIn(object):
	def __init__(self, address, bus):
		self.address = address
		self.bus = bus
		
	def write(self, value):
		self.bus.write_byte_data(self.address, 0, value)
		return -1
	
	def read(self):
		range1 = self.bus.read_byte_data(self.address, 2)
		range2 = self.bus.read_byte_data(self.address, 3)
		range3 = (range1 << 8) + range2
		return range3
