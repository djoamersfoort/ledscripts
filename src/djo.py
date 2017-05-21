#!/usr/bin/env python2

import time;
import math;

import sys
sys.path.append('../lib')
from strip import *;

stripLength = 150;
lightCount = 50;
fadeDuration = 5.0
tau = math.pi * 2
lightOn = 3

coverPerc = 1 - lightOn / (lightCount * 0.5);

def getIntensity(now, pos):
    nodeNumber = float(pos)
    timePos = now / lightCount * tau;
    nodePos = (pos / lightCount) * tau;

    nodeIntensity = math.cos(timePos - nodePos) - coverPerc;
    return  max(0.0, nodeIntensity / (1.0 - coverPerc));

def getColorForPos(now, pos):
    m = getIntensity(now, pos)
    r = int(round(117 * m))
    g = int(round(24 * m))
    b = int(round(15 * m))
    return [r, g, b]

strip = Strip(stripLength)
strip.clear()
strip.send()

now = time.time() * 1.0

while True:
    now = now + (1 / 60.0)
    for i in range(0, stripLength + 2):
        strip.set(i, getColorForPos(now, i * 1.0));

    strip.send()
