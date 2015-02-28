import sys
from PyQt4 import QtGui, QtCore
from err_window import Err_Window

class INERROR(Exception):
    
    def __init__(self, msg):
        Exception.__init__(self)

