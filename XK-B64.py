#XK-B64 v2.4.8

import base64, sys, time

def type(txt):
  for char in txt:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.02)
    
print("\033[1;31;40m")
type("Base64 Encoder/Decoder made by Unknown-XK\n")
print("\033[1;37;40m")
type("Hello to XK-B64...\n")

def xk():
  if True:
    time.sleep(1)
    print("\033[1;31;40m")
    type("Type 'e' for encoding, 'd' for decoding or 'x' for exit:")
    x = input()
    print("\033[1;37;40m")
  if x == "e":
    type("Enter the Message:\n\n")
    msg = input()
    print()
    msg = msg.encode("ascii")
    b64 = base64.b64encode(msg)
    b64m = b64.decode("ascii")
    type("Your encoded message is:\n\n")
    type(b64m)
    print()
  elif x == "d":
    type("Enter the encoded message:\n\n")
    b64m = input()
    print()
    b64m = b64m.encode("ascii")
    b64 = base64.b64decode(b64m)
    msg = b64.decode("ascii")
    type("Your decoded message is:\n\n")
    type(msg)
    print()
  elif x == "x":
    type("Process ended...\n")
    print("\033[0m")
    exit()
  else:
    type("Invalid input.\n")

while True:
  xk()
