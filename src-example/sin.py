#!/usr/bin/python

import math;
import time;
import random;
import copy;

import sys;
sys.path.append('../lib');
from strip import *;

# 2D declining sin

class Sin(Effect):
  x0 = 0;
  y0 = 10;

  def __init__(self, strip2D):
    super(Sin, self).__init__(strip2D);
    self.strip2D.strip.clear();
    self.strip2D.send();

  def step(self, count):
    for x in range(7):
      for y in range(21):
        xx = x - self.x0;
        yy = y - self.y0;
        d = math.sqrt(xx * xx + yy * yy);
        if d == 0: d = 1;
        b = 7 + 8 * math.sin(2 * math.pi * (d - float(count)/20) / 4) / d;
        b = int(b);
        if b < 0: b = 0;
        self.strip2D.set(x, y, colors[b]);
    #time.sleep(0.10);

colors = [
  [0, 0, 1], 
  [0, 0, 4], 
  [0, 0, 9], 
  [0, 0, 16], 
  [0, 0, 25], 
  [0, 0, 36], 
  [0, 0, 49], 
  [0, 0, 64], 
  [4, 4, 81], 
  [16, 16, 100], 
  [36, 36, 121], 
  [64, 64, 143], 
  [100, 100, 168], 
  [143, 143, 195], 
  [195, 195, 224], 
  [255, 255, 255], 
];

if __name__ == "__main__":
  e = Sin(Strip2D(7, 21));
  e.run();


