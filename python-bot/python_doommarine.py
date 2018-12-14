#!/usr/bin/env python

import botbasic, time, sys
import botlib
from chvec import *
import math

debugTowards = False

def walkSquare ():
    bot.forward (100, 100)
    bot.select (["move"])
    bot.left (100, 100)
    bot.select (["move"])
    bot.back (100, 100)
    bot.select (["move"])
    bot.right (100, 100)
    bot.select (["move"])


def runArc (angle):
    bot.forward (100, 100)
    bot.turn (angle, 1)
    bot.select (["move"])
    bot.select (["turn"])


def circle (velocity, distance):
    while True:
        for a in range (0, 360, 45):
            runArc (a+180)
        time.sleep (5)
        for w in range (0, 10):
            print "attempting to change to weapon", w,
            # print "dhewm3 returns", b.changeWeapon (w)
            # time.sleep (3)

def testturn (a):
    bot.turn (a, 1)
    bot.select (["turn"])

def sqr (x):
    return x * x

def calcDist (d0, d1):
    p0 = bot.d2pv (d0)
    p1 = bot.d2pv (d1)
    s = subVec (p0, p1)
    return math.sqrt (sqr (s[0]) + sqr (s[1]))

def moveTowards (goalObj):
    bot.reset ()
    print "will go and find", goalObj
    print "I'm currently at", bot.getpos (me), "and", goalObj, "is at", bot.getpos (goalObj)
    """
    if not equVec (b.d2pv (b.getpos (me)), [12, 9]):
        print "failed to find getpos at 12, 9 for python"
    if not equVec (b.d2pv (b.getpos (i)), [40, 3]):
        print "failed to find getpos at 40, 3 for player"
    """
    if debugTowards:
        print "bot is at", bot.d2pv (bot.getpos (me))
        print "you are at", bot.d2pv (bot.getpos (you))
    distance = bot.calcnav (goalObj)
    if debugTowards:
        print "object", goalObj, "is", distance, "units away"
    if distance is None:
        if debugTowards:
            print "cannot reach", goalObj
        bot.turn (90, 1)
        bot.select (["turn"])
        bot.forward (100, 100)
        bot.select (["move"])
    else:
        if debugTowards:
            print "distance according to dijkstra is", distance
        bot.journey (100, distance, goalObj)
        if debugTowards:
            print "finished my journey to", goalObj
            print "  result is that I'm currently at", bot.getpos (me), "and", goalObj, "is at", bot.getpos (goalObj)
            print "      penguin tower coords I'm at", bot.d2pv (bot.getpos (me)), "and", goalObj, "is at", bot.d2pv (bot.getpos (goalObj))


def findAll ():
    for i in bot.allobj ():
        print "the location of python bot", me, "is", bot.getpos (me)
        if i != me:
            bot.aim (i)
            moveTowards (i)
            time.sleep (5)

def findYou (b):
    for i in b.allobj ():
        if i != b.me ():
            return i


def antiClock (b):
    print "finished west, north, east, south"
    print "west, north, east, south diagonal"
    for v in [[1, 1], [-1, 1], [-1, -1], [1, -1]]:
        print "turning",
        b.turnface (v, 1)
        b.sync ()
        print "waiting"
        time.sleep (10)
        print "next"
        b.reset ()


def clock (b):
    print "finished west, north, east, south"
    print "west, north, east, south diagonal"
    for v in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
        print "turning",
        b.turnface (v, -1)
        b.sync ()
        print "waiting"
        time.sleep (10)
        print "next"
        b.reset ()


doommarine = -2

def execBot (b, useExceptions = True):
    if useExceptions:
        try:
            botMain (b)
        except:
            print "bot was killed, or script terminated"
            return
    else:
        botMain (b)


def botMain (b):
    global me
    global you
    print "success!  python doom marine is alive"

    print "trying to get my id...",
    me = b.me ()
    print "yes"
    print "the python marine id is", me
    you = findYou (b)

    # b.change_weapon (1)
    # print "changed to 1"
    # time.sleep (2)

    while True:
        # Testing the jump/crouch method
        # b.reset ()
        # b.stepup (-2, 3*12)
        # print "Bot crouched"
        # b.select (['move'])
        # time.sleep (2)
        # b.stepup (100, 4*12)
        # print "Bot jumped"
        # b.select (['move'])

        # Testing the health
        # moveTowards (you)
        # b.face (you)
        # print "Health is: " + str(b.get_health ())
        # time.sleep (1)

        # Fire and reload weapon actions - works
        # b.start_firing ()
        # time.sleep (1)
        # print "Reloading weapon", b.reload_weapon ()
        # time.sleep (1)

        # Fire and reload weapon actions - reload doesn't occure because firing animation is not finished
        # b.start_firing ()
        # print "Reloading weapon", b.reload_weapon ()
        # time.sleep (1)

        # Testing changing weapons
        b.change_weapon(0)
        print "Weapon changed to: ", 0
        time.sleep(1)
        b.change_weapon(1)
        print "Weapon changed to: ", 1
        time.sleep(1)
        b.change_weapon(2)
        print "Weapon changed to: ", 2
        time.sleep(1)
        b.change_weapon(3)
        print "Weapon changed to: ", 3
        time.sleep(1)



if len (sys.argv) > 1:
    doommarine = int (sys.argv[1])

bot = botlib.bot ("localhost", "python_doommarine %d" % (doommarine))
execBot (bot, False)
