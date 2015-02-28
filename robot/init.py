from selenium import webdriver
from selenium.webdriver.support.ui import Select
from rob1 import Rob
import sys
from PyQt4 import QtGui, QtCore
from err_window import Err_Window

DICT = {
        'amount': 4000,
        'durat': 30,
        'firstname': 'Vasya',
        'lastname': '',
        'mob_number': '3350090',
        'email': 'xxx@xxx.xx',
        'ch1': True,
        'ch2': True,
        }

LINK = "http://bbpujcka.cz/"
#app = QtGui.QApplication(sys.argv)
#tg = Err_Window("hhhhhhh")
#tg.show()

#app.exec()
Rob(DICT, LINK)


