import math
import os
import random
import sys

import pymunk

from .layer import Layer

from wyggles.mathutils import *

world_min_x = 0 
world_min_y = 0 
world_max_x = 1024
world_max_y = 768

def materializeRandomFromCenter(sprite):
    halfMaxX = world_max_x / 2
    halfMaxY = world_max_x / 2
    diameter = 400
    radius = diameter / 2
    sprite.materialize_at( (halfMaxX - radius) + (random.random() * diameter), (halfMaxY - radius) + (random.random() * diameter))        

class SpriteEngine():
    
    def __init__(self):
        self.root = Layer("root")
        #
        self.beacons = []
        self.idCounter = 0
        #
        self.gravityX = 0
        #self.gravityY = 9.8 ;        
        self.gravityY = 0
        # new stuff
        self.space = pymunk.Space()
        self.space.iterations = 35
        self.space.gravity = (self.gravityX, self.gravityY)
        
    def addBeacon(self, beacon) :
        self.beacons.append(beacon) ;

    def removeBeacon(self, beacon):
        self.beacons.remove(beacon)

    def query(self, x, y, distance):
        beacon = None
        result = None
        for beacon in self.beacons:
            dist = distance2d(x, y, beacon.x, beacon.y)
            if(dist < distance):
                if(result == None):
                    result = [beacon]
                else:
                    result.append(beacon)
        return result

    def gen_id(self, name):
        result = name + str(self.idCounter)
        self.idCounter += 1
        return result
        
    def get_root(self):
        return self.root    

#fixme: singleton pattern
sprite_engine = SpriteEngine()
