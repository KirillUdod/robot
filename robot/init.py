#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from rob1 import Rob
import sys
from PyQt4 import QtGui, QtCore
from err_window import Err_Window


LINK = "http://bbpujcka.cz/"
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

Rob(DICT, LINK)

#ошибка несоответствия лимита и количества
#DICT = {
#        'amount': 4000,
#        'durat': 300,
#        'firstname': 'NAme',
#        'lastname': 'Fam',
#        'mob_number': '3350090',
#        'email': 'man@i.ru',
#        'ch1': True,
#        'ch2': True,
#        }

#Rob(DICT, LINK)

#пустое поле имени
#DICT = {
#        'amount': 4000,
#        'durat': 30,
#        'firstname': '',
#        'lastname': 'Fam',
#        'mob_number': '3350090',
#        'email': 'man@i.ru',
#        'ch1': True,
#        'ch2': True,
#        }

#Rob(DICT, LINK)

#неправильный лимит
#DICT = {
#        'amount': 4000,
#        'durat': 301,
#        'firstname': 'NAme',
#        'lastname': 'Fam',
#        'mob_number': '3350090',
#        'email': 'man@i.ru',
#        'ch1': True,
#        'ch2': True,
#        }

#Rob(DICT, LINK)

#неправильное количество
#DICT = {
#        'amount': 400,
#        'durat': 30,
#        'firstname': 'NAme',
#        'lastname': 'Fam',
#        'mob_number': '3350090',
#        'email': 'man@i.ru',
#        'ch1': True,
#        'ch2': True,
#        }

#Rob(DICT, LINK)


