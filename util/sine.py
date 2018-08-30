# print sine to screen
# require python 2.7
#

import math

def get_sine():
  n = 16
  for i in range(0, n):
    a = math.sin(2*math.pi * i / n)
    d = (a + 1)*0x80
    if d >= 0xFF:
      d = 0xFF
    print("0x%02X, // %.4f" % (d, a))

get_sine()
