exec(open('/home/pi/devel/rpipySSD1306/start.py').read())

pixBuf = 2

def checkChenWidth(inChan):
    out1 = inChan*10
    out2 = out1 + 10
    return (out1,out2)

def writeRect():
    pass


time.sleep(1)
disp.rect(x= 10, y = 10, width=10, height=10, color = 1)
disp.rect(x= 20, y = 40, width=10, height=10, color = 1)
disp.show()
time.sleep(1)
disp.fill(0)
disp.rect(x= 10, y = 10, width=10, height=10, color = 1)
disp.rect(x= 20, y = 40, width=10, height=10, color = 1)
disp.rect(x= 30, y = 10, width=10, height=10, color = 1)
disp.rect(x= 40, y = 10, width=10, height=10, color = 1)
disp.show()
time.sleep(1)
disp.fill(0)
disp.show()
time.sleep(1)
disp.fill(0)
disp.rect(x= 10, y = 10, width=10, height=10, color = 1)
disp.show()
time.sleep(1)
disp.rect(x= 20, y = 20, width=10, height=10, color = 1)
disp.show()
time.sleep(1)
disp.rect(x= 30, y = 30, width=10, height=10, color = 1)
disp.show()
time.sleep(1)
disp.rect(x= 20, y = 20, width=10, height=10, color = 1)
disp.show()
time.sleep(1)
disp.rect(x= 10, y = 10, width=10, height=10, color = 1)
disp.show()
time.sleep(1)
disp.fill(0)
dsip.show()

