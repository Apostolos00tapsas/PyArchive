#!/usr/bin/env python
"""
antikythera.py - The Antikythera Mechanism
Author: Sean B. Palmer, inamidst.com
Based on the Greek original.

The folllowing schematics were used: 
 * http://www.math.sunysb.edu/~tony/whatsnew/column/
   antikytheraI-0400/images/smallgears.gif
 * http://www.perseus.tufts.edu/GreekScience/Students/Jesse/antik.gif

"""


from math import floor
from decimal import Decimal as dec

verbose = False

class Gear(object): 
   def __init__(self, name, teeth): 
      self.name = name
      self.teeth = dec(teeth)
      self.pos = dec(0)
      self.siblings = []
      self.pairs = []
      self.contrates = []

   def forward(self, degrees=None, seen=None): 
      if seen is not None: 
         if self in seen: return
         seen.append(self)
      else: seen = [self]

      if verbose: 
         print (self.name, 'forward', degrees)

      if degrees is None: 
         degrees = dec(360) / self.teeth

      self.pos = (self.pos + degrees) % dec(360)

      for sibling in self.siblings: 
         deg = degrees * (self.teeth / sibling.teeth)
         sibling.backward(deg, seen=seen)

      for pair in self.pairs: 
         pair.forward(degrees, seen=seen)

      for contrate in self.contrates: 
         contrate.backward(degrees, seen=seen)

   def backward(self, degrees=None, seen=None): 
      if seen is not None:
         if self in seen: return
         seen.append(self)
      else: seen = [self]

      if verbose: 
         print (self.name, 'backward', degrees)

      if degrees is None:
         degrees = dec(360) / self.teeth

      self.pos = (self.pos - degrees) % dec(360)

      for sibling in self.siblings:
         deg = degrees * (self.teeth / sibling.teeth)
         sibling.forward(deg, seen=seen)

      for pair in self.pairs:
         pair.backward(degrees, seen=seen)

      for contrate in self.contrates:
         contrate.forward(degrees, seen=seen)

   def bind(self, gear, local, remote): 
      if gear not in local: 
         local.append(gear)
      if self not in remote: 
         remote.append(self)

   def link(self, gear): 
      """Create a bidirectional link between gears."""
      self.bind(gear, self.siblings, gear.siblings)

   def pair(self, gear): 
      """Create a pairing of gears."""
      self.bind(gear, self.pairs, gear.pairs)

   def contrate(self, gear): 
      """Join to a contrate gear."""
      self.bind(gear, self.contrates, gear.contrates)

def sunmoon(): 
   B64 = Gear('B64', 64) # B Outer - Sun Gear

   A = Gear('A', 64) # Sun Movement
   B64.contrate(A)

   C38 = Gear('C38', 38) # C Inner
   C38.link(B64)

   C48 = Gear('C48', 48) # C Outer
   C48.pair(C38)

   D24 = Gear('D24', 24) # D Inner
   D24.link(C48)

   D127 = Gear('D127', 127) # D Outer
   D127.pair(D24)

   B32 = Gear('B32', 32) # B Inner - Moon Gear
   B32.link(D127)

   for i in xrange(16): 
      B32.forward()
      print (A.pos, B32.pos)

def antikythera(): 
   moon = Gear('Moon', 200) # Actual value unknown
   sun = Gear('Sun', 225) # Marked as "?"
   crank = Gear('Crank', 225)
   B1 = Gear('B1', 225)
   L1 = Gear('L1', 36)
   B2 = Gear('B2', 64)
   C1 = Gear('C1', 38)
   M1 = Gear('M1', 96)
   L2 = Gear('L2', 54)
   C2 = Gear('C2', 48)
   D1 = Gear('D1', 24)
   E1 = Gear('E1', 32)
   B3 = Gear('B3', 32)
   O1 = Gear('O1', 32)
   N = Gear('N', 64)
   M2 = Gear('M2', 16)
   E2i = Gear('E2i', 32)
   B4 = Gear('B4', 32)
   D2 = Gear('D2', 127)
   O2 = Gear('O2', 48)
   K1 = Gear('K1', 32)
   J = Gear('J', 64)
   E2ii = Gear('E2ii', 32)
   E4 = Gear('E4', 222)
   E3 = Gear('E3', 192)
   F1 = Gear('F1', 48)
   K2 = Gear('K2', 48)
   E5 = Gear('E5', 48)
   F2 = Gear('F2', 30)
   G2 = Gear('G2', 60)
   G1 = Gear('G1', 20)
   H1 = Gear('H1', 60)
   H2 = Gear('H2', 15)
   I = Gear('I', 60)

   # Differential Turntable
   # These two gears are a shim to reproduce the effect of the differential
   # gear, E3/E4, to which J and K are attached. The speed of the differential
   # turntable should be the difference of Sun (E1) and Moon (E2) divided by
   # two, which is (254 - 19) / 2. Hence the 235:38 ratio.
   X235 = Gear('X235', 235)
   X38 = Gear('X38', 38)

   B1.contrate(sun)
   
   L1.link(B2)
   B2.link(C1)
   M1.link(L2)
   C2.link(D1)
   E1.link(B3)
   O1.link(N)
   N.link(M2)
   E2i.link(B4)
   B4.link(D2)
   K1.link(J)
   J.link(E2ii)
   E3.link(F1)
   K2.link(E5)
   F2.link(G2)
   G1.link(H1)
   H2.link(I)
   X235.link(X38)

   crank.pair(sun)
   moon.pair(B4)
   B1.pair(B2)
   B2.pair(B3)
   L1.pair(L2)
   C1.pair(C2)
   M1.pair(M2)
   D1.pair(D2)
   E1.pair(E5)
   E2i.pair(E2ii)
   O1.pair(O2)
   K1.pair(K2)
   E3.pair(E4)
   F1.pair(F2)
   G2.pair(G1)
   H1.pair(H2)

   # Differential pairings
   B1.pair(X235)
   E3.pair(X38)

   return crank, sun, moon, N, G1, I

def main(): 
   import sys

   if len(sys.argv) == 2: 
      degrees = dec(sys.argv[1])
   else: degrees = dec(180)

   crank, sun, moon, N, G1, I = antikythera()
   crank.forward(degrees)

   def format(label, gear, sign=''): 
      pos = round(gear.pos, 5)
      return (u'%s: %s%s\u00B0' % (label, sign, pos)).encode('utf-8')

   print (format('Sun', sun))
   print (format('Moon', moon))
   print (format('4 Year Dial', N, '-'))
   print (format('Synodic Month', G1, '-'))
   print (format('Lunar Year', I, '-'))

if __name__ == '__main__': 
   main()
