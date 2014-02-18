#!/usr/bin/python

import API
import time

def printWorkerStatus(w):
    for worker in API.getWorkers():
        if (w == worker):
            debug_status("worker %d is up." % w.id)
    debug_status("worker %d is down")

def printAllUpWorkers():
    L = len(API.getWorkers())
    if (L == 1):
        debug_status("1 worker is up")
    else:
        debug_status("%d workers are up" % L)

def printAllWorkerTask():
    for w in API.getWorkers():
        printWorkerTask(w)

def printWorkerTask(w):
        schedules = API.getSchedules(w)
        string = "worker %d's schedules: " % w.id
        for s in schedules:
            string += "%d " % s.id,
        debug_status(string)

def printAllWorkerHeartBeat():
    for w in API.getWorkers():
        printWorkerHeartBeat(w)

def printWorkerHeartBeat(w):
        debug_status("worker %d's heartbeat: %s" % (w.id, w.heartbeat))

def doall():
    printAllUpWorkers()
    printAllWorkerTask()
    printAllWorkerHeartBeat()

def do(w):
    printWorkerStatus(w)
    printWorkerTask(w)
    printWorkerHeartBeat(w)

def debug_status(s):
    print "[status.py: %s] %s" % (time.ctime(), s)


if __name__ == '__main__':
    doall()
