#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot #Import a base Robot

class Charlier(Robot): #Create a Robot
    
    def init(self):    #To initialyse your robot
        
        
        #Set the bot color in RGB
        self.setColor(0, 200, 100)
        self.setGunColor(200, 200, 0)
        self.setRadarColor(255, 60, 0)
        self.setBulletsColor(255, 150, 150)
        
        #get the map size
        size = self.getMapSize()
        
    
    def run(self): #main loop to command the bot
        
        #self.move(90) # for moving (negative values go back)
        #self.stop()
        self.gunTurn(180)
        self.stop()
        self.turn(90) #for turning (negative values turn counter-clockwise)
        self.move(90)
        self.stop()
        self.fire(10)
        self.move(50)
        #self.setGunDirection(40) # set the Gun direction (bottom = 0°)

    def sensors(self): #NECESARY FOR THE GAME
        pass

    def onHitByBullet(self, bulletBotId, bulletPower): #NECESARY FOR THE GAME
        print "hit by ", bulletBotId, "with power:", bulletPower
        
    def onBulletHit(self, botId, bulletId):
        print "fire done on ",  botId
        
    def onBulletMiss(self, bulletId):#NECESARY FOR THE GAME
        """when my bullet hit a wall"""
        print "the bullet ",  bulletId, "fail"
        
