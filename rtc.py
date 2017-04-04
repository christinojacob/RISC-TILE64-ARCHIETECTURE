import time

class rtclock:
    def __init__(self,hours,minutes,seconds):
        self.seconds=seconds
        self.minutes=minutes
        self.hours=hours

    def stopwatch(self):
        start = time.time()
        time.clock()
        elapsed = 0
        self.minutes=0
        self.seconds=0
        self.hours=0
        #while elapsed < seconds:
        while elapsed>-1:
            elapsed = time.time() - start
            time.sleep(1)
            self.seconds=int(elapsed)

            if(self.seconds%60==0) and (self.seconds!=0):
                self.minutes=self.minutes+1
            if(self.minutes%60==0) and (self.minutes!=0):
                self.hours=self.hours+1
            print self.hours,":",self.minutes,":",self.seconds
