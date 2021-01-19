from __future__ import print_function
import rpyc
import sys

if __name__ == "__main__":
  func = sys.argv[1]
  c = rpyc.connect("localhost", 12345)
  exec('print(c.root.{}())'.format(func))