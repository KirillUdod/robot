from selenium import webdriver
from selenium.webdriver.support.ui import Select
from rob1 import Rob
import sys
from PyQt4 import QtGui, QtCore
from err_window import Err_Window

DICT = {
        'amount': 4000,
        'durat': 30,
        'firstname': 'NAme',
        'lastname': 'Fam',
        'mob_number': '3350090',
        'email': 'man@i.ru',
        'ch1': True,
        'ch2': True,
        }

LINK = "http://bbpujcka.cz/"
Rob(DICT, LINK)


