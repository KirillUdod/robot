from selenium import webdriver
from selenium.webdriver.support.ui import Select
from err_window import Err_Window
import sys
from PyQt4 import QtGui, QtCore

class Rob():

    def __init__(self, DICT, browser): 
    
        def ch(lt):
            amount =  lt.find_elements_by_css_selector(".sum-option")
            for am in amount:
                temp = am.find_element_by_name("sum-selection")
                if (DICT['amount'] == int(temp.get_attribute('value'))):
                    am.find_element_by_css_selector(".radio-fx.sum-selection").find_element_by_css_selector(".radio").click()
                    break

            limit =  browser.find_elements_by_css_selector(".limit-option")
            for lm in limit:
                temp1 = lm.find_element_by_name("limit-selection")
                if (DICT['durat'] == int(temp1.get_attribute('value'))):
                    lm.find_element_by_css_selector(".radio-fx.limit-selection").find_element_by_css_selector(".radio").click()
                    break
        
        if ((DICT['amount']>=1000) and (DICT['amount']<=5000)):
            browser.find_element_by_id("tab-1").click()
            ch(browser.find_element_by_id("container-selection-1"))
        elif (DICT['amount']<=10000):
            browser.find_element_by_id("tab-2").click()
            ch(browser.find_element_by_id("container-selection-2"))
        elif ((DICT['amount']>=12000) and (DICT['amount']<=20000)):
            browser.find_element_by_id("tab-3").click()
            ch(browser.find_element_by_id("container-selection-3"))
        elif ((DICT['amount']>=25000) and (DICT['amount']<=45000)):
            browser.find_element_by_id("tab-4").click()
            ch(browser.find_element_by_id("container-selection-4"))
        else:
            print("error1") 

        firstname = browser.find_element_by_id("firstname")
        lastname = browser.find_element_by_id("lastname")
        mobile = browser.find_element_by_id("mobile")
        email = browser.find_element_by_id("email")
        chb1 = browser.find_element_by_id("checkbox1")
        chb2 = browser.find_element_by_id("checkbox2")
            
        firstname.send_keys(DICT['firstname'])
        lastname.send_keys(DICT['lastname'])
        mobile.send_keys(DICT['mob_number'] )
        email.send_keys(DICT['email'])
        if (DICT['ch1'] == True):
            chb1.click()
        if (DICT['ch2'] == True):
            chb2.click()

        if (firstname.get_attribute('value') == DICT['firstname']):
            app = QtGui.QApplication(sys.argv)
            tg = Err_Window("sssssssssssssss")
            tg.show()
            app.exec()
            browser.close()
        lastname.get_attribute('value')
        mobile.get_attribute('value')
        email.get_attribute('value')
    
