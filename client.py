from __future__ import print_function
import rpyc
import sys

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print('Choose between \'load\' and \'train\' functions')
    exit()
  
  func = sys.argv[1]
  arg = int(sys.argv[2]) if len(sys.argv) == 3 else None

  c = rpyc.connect("localhost", 12345)

  c._config['sync_request_timeout'] = None

  if arg is None:
    exec('print(c.root.{}())'.format(func))
  else:
    exec('print(c.root.{}({}))'.format(func, arg))
