#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

# Invented by Kiki Jewell with a little help from Spaceman Sam, May 6, 2016

import time
import csv
import atexit



#######################
#     DRINK MAKER     #
#######################

############################################
# Initialize the motors on the Bot         #
############################################
# Set up the address for each of the pumps #
# NOTE: Since we don't have all 3 hats,    #
#   I've commented out for the other       #
#   two boards, until they come in         #
############################################

# bottom hat is default address 0x60
# Board 0: Address = 0x60 Offset = binary 0000 (no jumpers required)
bottom_hat = Adafruit_MotorHAT(addr=0x60)

# middle hat has A0 jumper closed, so its address 0x61.
# Board 1: Address = 0x61 Offset = binary 0001 (bridge A0)
middle_hat = Adafruit_MotorHAT(addr=0x61)
# top hat has A0 jumper closed, so its address 0x62.
# Board 2: Address = 0x62 Offset = binary 0010 (bridge A1, the one above A0)
###   top_hat = Adafruit_MotorHAT(addr=0x62)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    bottom_hat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    bottom_hat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    bottom_hat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    bottom_hat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    middle_hat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    middle_hat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    middle_hat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    middle_hat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
# top_hat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
# top_hat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
# top_hat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
# top_hat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

#####################
# Bottom Hat motors #
#####################
# Note: The pumps are indexed by the ingredient name
#   range(1,5) means make a set of 5 numbers, 0-indexed, start at 1
#   Keep in mind, 0-index to 5, is [0,1,2,3,4]
#   So starting at 1 means [1,2,3,4]
#   Index #0 is the name "Recipe" so it is skipped
ingr_pumps = {}
ingr_list = ["one", "two", "three", "four"]
temp_ingr_list = iter(ingr_list)
for each_motor in range(1, 5):
    ingr_pumps[temp_ingr_list.next()] = bottom_hat.getMotor(each_motor)
    #ingr_pumps[temp_ingr_list.next()] = "blah"

for each_pump in ingr_pumps:
    print each_pump


import threading

class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             self.total+=i

class Motors(threading.Thread):
    def __init__(self, motor, ounces):
        super(Motors, self).__init__()
        self.motor = motor
        self.ounces = ounces
        self.start()
        self.join()

    def run(self):
        print "Motor start."
        self.motor.setSpeed(255)
        self.motor.run(Adafruit_MotorHAT.FORWARD)
        time.sleep(self.ounces)
        print "Motor done."
        self.motor.run(Adafruit_MotorHAT.RELEASE)


<<<<<<< Updated upstream
class Kiki(threading.Thread):
    def __init__(self, time):
        super(Kiki, self).__init__()
        self.time = time
        self.start()
        self.join()

    def run(self):
        print "Kiki start."
        time.sleep(self.time)
        print "Kiki done."

thread1 = Kiki(1)
thread1 = Kiki(3)
thread1 = Kiki(6)
thread1 = Kiki(9)

#thread1 = Motors(ingr_pumps["one"],1)
#thread2 = Motors(ingr_pumps["two"],3)
#thread3 = Motors(ingr_pumps["three"],6)
#thread4 = Motors(ingr_pumps["four"],9)
=======
thread1 = Motors(ingr_pumps["one"],1)
thread2 = Motors(ingr_pumps["two"],3)
thread3 = Motors(ingr_pumps["three"],6)
thread4 = Motors(ingr_pumps["four"],9)
>>>>>>> Stashed changes
#thread1.start()
#thread1.join()
#thread4.start()
#thread4.join()

# At this point, both threads have completed

#from twisted.internet import reactor

#def f(s):
#    print "this will run 3.5 seconds after it was scheduled: %s" % s

#reactor.callLater(3.5, f, "hello, world")

## f() will only be called if the event loop is started.
#reactor.run()

####### Sample code to test interrupts
    # def runEverySecond( some_text ):
    #print some_text

    #l = task.LoopingCall(runEverySecond, "Kiki a second has passed")
    #l.start(1.0) # call every second

    # l.stop() will stop the looping calls
    #reactor.run()
####### END Temp code to test interrupts




#######################
# PRINT INGREDIENTS   #
#######################
# This prints all the ingredients, including 'Recipe'
