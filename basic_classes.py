import array
import time
import datetime
import os
import random
import math

class Vector(object):
    #'Represents a 2D vector.'
    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)
        
    def __add__(self, val):
        return Point( self[0] + val[0], self[1] + val[1] )
    
    def __sub__(self,val):
        return Point( self[0] - val[0], self[1] - val[1] )
    
    def __iadd__(self, val):
        self.x = val[0] + self.x
        self.y = val[1] + self.y
        return self
        
    def __isub__(self, val):
        self.x = self.x - val[0]
        self.y = self.y - val[1]
        return self
    
    def __div__(self, val):
        return Point( self[0] / val, self[1] / val )
    
    def __mul__(self, val):
        return Point( self[0] * val, self[1] * val )
    
    def __idiv__(self, val):
        self[0] = self[0] / val
        self[1] = self[1] / val
        return self
        
    def __imul__(self, val):
        self[0] = self[0] * val
        self[1] = self[1] * val
        return self
                
    def __getitem__(self, key):
        if( key == 0):
            return self.x
        elif( key == 1):
            return self.y
        else:
            raise Exception("Invalid key to Point")
        
    def __setitem__(self, key, value):
        if( key == 0):
            self.x = value
        elif( key == 1):
            self.y = value
        else:
            raise Exception("Invalid key to Point")
        
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

class SongCollection(object):
	def __init__(self, filePath):
		self.collection = list()
		self.filePath = filePath
		self.getFileNames()
		
	def getFileNames(self):
		songList = list()
		for root, dirs, files in os.walk(self.filePath):
			for filename in files:
				self.collection.append(filename)

	def GetSize(self):
		return len(self.collection)
	
	def PlaySong(self):
		os.system('mpg321 ' + self.filePath + "/" + str(self.GetRandom()) + ' & ')
	
	def GetRandom(self):
		key = random.randrange(0, self.GetSize())
		return self.collection[key]
	
	def GetFilePath(self):
		return self.filePath
