import time

def makeTrueY(inY, rect=128):
    if inY > 128:
        return None
    else:
        return rect - inY 


class Mixer:
    def __init__(self, disp, width = 128, height = 64):
    
        self.disp = disp
        
        self.timeSleep = 1.
        self.defaultAmpl = 0.73    
    
        self.buffer = 20
        self.bar = 12
        self.gap = 4
        self.buffer = 5

        self.dictVUs = {}
        
        self.V1 = self.defaultAmpl
        self.V2 = self.defaultAmpl
        self.V3 = self.defaultAmpl
        self.V4 = self.defaultAmpl
        self.V5 = self.defaultAmpl
        self.V6 = self.defaultAmpl
        
        self.ymax = 64
        self.ymin = 0
        self.yhead = 5
        self.ymx = 0
        self.yb = 5
        self.yrng = self.ymax - self.yhead - self.yb
        # init barh
        self.barh1 = int(self.yrng * self.V1)
        self.barh2 = int(self.yrng * self.V2)
        self.barh3 = int(self.yrng * self.V3)
        self.barh4 = int(self.yrng * self.V4)
        self.barh5 = int(self.yrng * self.V5)
        self.barh6 = int(self.yrng * self.V6)
        #
        buffer = self.buffer
        bar = self.bar
        gap = self.gap
        #
        self.x_ = 0    
        self.x0 = self.x_ + buffer        #
        self.x1 = self.x0+bar   #1
        self.x2 = self.x1+gap   #1
        self.x3 = self.x2+bar   #2
        self.x4 = self.x3+gap   #2
        self.x5 = self.x4+bar   #3
        self.x6 = self.x5+gap   #3
        self.x7 = self.x6+bar   #   4
        self.x8 = self.x7+gap   #4
        self.x9 = self.x8+bar   #5
        self.x10 = self.x9+gap  #5
        self.x11 = self.x10+bar #6
        self.x12 = self.x11+gap #6

    def updateScreen(self):
        self._update_barh()
        self._update_rects()
        self._write_levels()
        time.sleep(self.timeSleep)
    
    def clearScreen(self):
        self._write_clear()
        
    def setVolumeVector(self,V1=.73,
                            V2=.73,
                            V3=.73,
                            V4=.73,
                            V5=.73,
                            V6=.73):
        self.V1 = V1
        self.V2 = V2
        self.V3 = V3
        self.V4 = V4
        self.V5 = V5
        self.V6 = V6
        
    
    
    def _update_barh(self):
        self.barh1 = int(self.yrng * self.V1)
        self.barh2 = int(self.yrng * self.V2)
        self.barh3 = int(self.yrng * self.V3)
        self.barh4 = int(self.yrng * self.V4)
        self.barh5 = int(self.yrng * self.V5)
        self.barh6 = int(self.yrng * self.V6)
    
    def _update_rects(self):    
        #                  [  a   ,    b   ,     c   ,     d     , e]
        #
        self.dictVUs[1] = [self.x0, self.yb, self.bar, self.barh1, 1]
        self.dictVUs[2] = [self.x2, self.yb, self.bar, self.barh2, 1]
        self.dictVUs[3] = [self.x4, self.yb, self.bar, self.barh3, 1]
        self.dictVUs[4] = [self.x6, self.yb, self.bar, self.barh4, 1]
        self.dictVUs[5] = [self.x8, self.yb, self.bar, self.barh5, 1]
        self.dictVUs[6] = [self.x10, self.yb, self.bar, self.barh6,1]
        
    def _write_level(self,channelNum):
        self.disp.fill(0)
        self.disp.show()
        a,b,c,d,e = self.dictVUs[channelNum]
        self.disp.rect(a,self.ymax-b,c,d,e)
        self.disp.show()
    
    def _write_levels(self):
        self.disp.fill(0)
        self.disp.show()
       
        for VU in self.dictVUs:
        #  all channels VU bar
            a,b,c,d,e = self.dictVUs[VU]
            print(VU,a,b,c,d,e)
            yr = self.ymax - self.yb - d
            self.disp.rect(a,yr,c,d,e)
        self.disp.show()
        
    def _write_clear(self):
        self.disp.fill(0)
        self.disp.show()
        #self.disp.
    
    
        

