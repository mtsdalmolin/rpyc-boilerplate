from __future__ import print_function
import rpyc
import sys

if __name__ == "__main__":
  if len(sys.argv) < 2:
      print('Choose between \'load\' and \'train\' functions')
      exit()
  func = sys.argv[1]
  c = rpyc.connect("localhost", 12345)
  exec('print(c.root.{}())'.format(func))
