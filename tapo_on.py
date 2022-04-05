from PyP100 import PyP100

p100 = PyP100.P100("192.168.178.58", "xxxuserxxx", "xxxpasswordxxx")
p100.handshake()
p100.login()
p100.turnOn()