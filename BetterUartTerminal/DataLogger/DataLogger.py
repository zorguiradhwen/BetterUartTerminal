# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:18:11 2021

@author: radhwen.zorgui
"""

import time
import os
import sys
from datetime import datetime
from enum import IntEnum, Enum


class LogLevel(IntEnum):
    FATAL = 0
    ERROR = 1
    WARNING = 2
    INFO = 3
    TRACE = 4

class TimeStampType(Enum):
    CURRENT_TIME = 0
    DELTA_TIME = 1


class DataLogger:
        
    def __init__(self, loglevel = LogLevel.TRACE, show_date = True, show_subsecs = True, time_type = TimeStampType.CURRENT_TIME):      
        self.loglevel = loglevel
        self.show_date = show_date
        self.show_subsecs = show_subsecs
        self.time_type = time_type
        self.t0 = datetime.timestamp(datetime.now())
    
    def log(self, msg):
        now = "["
        if(self.time_type == TimeStampType.CURRENT_TIME):
            if(self.show_date):
                now += str(datetime.now().date()) + ", "
            else:
                pass
            if(self.show_subsecs):
                now += str(datetime.now().time()) + "]\t" # includes subsceonds at the end 
            else:
                now += datetime.now().strftime("%H:%M:%S") + "]\t"
        else:
            t1 = datetime.timestamp(datetime.now())
            delta = t1 - self.t0
            #dt_object = datetime.fromtimestamp(delta)
            now += "{:.6f}".format(delta) + "]\t" 
        print(now, msg)
        
    def fatal(self, msg):
        self.log("FATAL\t" + msg)              
    def error(self, msg):
        if(self.loglevel >= LogLevel.ERROR):
            self.log("ERROR\t" + msg)
    def warn(self, msg):
        if(self.loglevel >= LogLevel.WARNING):
            self.log("WARN \t" + msg)
    def info(self, msg):
        if(self.loglevel >= LogLevel.INFO):
            self.log("INFO \t" + msg)
    def trace(self, msg):
        if(self.loglevel >= LogLevel.TRACE):
            self.log("TRACE\t" + msg)

logger = DataLogger(loglevel=LogLevel.TRACE)
# delta = DataLogger(time_type = TimeStampType.DELTA_TIME)

if __name__ == "__main__":
    while True:
        
        logger.fatal("this is a fatal")
        logger.error("this is an error")
        logger.warn("this is a warning")
        logger.info("this is an info")
        logger.trace("this is a trace")
    
    
        #delta.fatal("delta time")
    
        time.sleep(0.5)

