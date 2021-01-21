# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:53:44 2021

@author: radhwen.zorgui
"""

import sys
import glob
import serial
import threading
import time
from DataLogger import DataLogger





class Terminal:

    def __init__(self, baudrate=115200):
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = baudrate

    def serial_ports(self):
        """ Lists serial port names
    
            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
    
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result
    
    def connect(self):
        if (len(self.serial_ports()) > 0):
            self.serial_port.port = self.serial_ports()[0]
            try:
                self.serial_port.open()
            except Exception as e:
                print(e)
            finally :
                if(self.serial_port.is_open):
                    print("Connected to" + self.serial_port.portstr)
                else:
                    exit()
    
    def disconnect(self):
        self.serial_port.close()
                    
                


s = Terminal()
print(s.serial_ports())
s.connect()
while True:
    line = s.serial_port.readline().decode("utf-8")
    print(line)

s.disconnect()