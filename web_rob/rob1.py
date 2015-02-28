from selenium import webdriver
from selenium.webdriver.support.ui import Select
import sys
from PyQt4 import QtGui, QtCore
from err_window import Err_Window
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException


bChb = {'amount':None, 'limit':None}
bCh = {'amount':None, 'limit':None}

class Rob():

    def __init__(self, DICT, LINK): 
        
        def CreateWin(msg):
            app = QtGui.QApplication(sys.argv)
            tg = Err_Window(msg)
            tg.show()
            browser.quit()
            app.exec()

        def ch(lt, bChb):
            amount =  lt.find_elements_by_css_selector(".sum-option")
            for am in amount:
                temp = am.find_element_by_name("sum-selection")
                if (DICT['amount'] == int(temp.get_attribute('value'))):
                    bChb['amount'] = am.find_element_by_css_selector(".radio-fx.sum-selection")
                    bChb['amount'].find_element_by_css_selector(".radio").click()
                    break

            limit =  browser.find_elements_by_css_selector(".limit-option")
            for lm in limit:
                temp1 = lm.find_element_by_name("limit-selection")
                if (DICT['durat'] == int(temp1.get_attribute('value'))):
                    try:
                        bChb['limit'] = lm.find_element_by_css_selector(".radio-fx.limit-selection")
                        bChb['limit'].find_element_by_css_selector(".radio").click()
                        break
                    except ElementNotVisibleException:
                        CreateWin("Incorrect limit for this amount")
            return bChb       
        browser = webdriver.Firefox()
        browser.get(LINK)

        if ((DICT['amount']>=1000) and (DICT['amount']<=5000)):
            browser.find_element_by_id("tab-1").click()
            bCh = ch(browser.find_element_by_id("container-selection-1"), bChb)
        elif (DICT['amount']<=10000):
            browser.find_element_by_id("tab-2").click()
            bCh = ch(browser.find_element_by_id("container-selection-2"), bChb)
        elif ((DICT['amount']>=12000) and (DICT['amount']<=20000)):
            browser.find_element_by_id("tab-3").click()
            bCh = ch(browser.find_element_by_id("container-selection-3"), bChb)
        elif ((DICT['amount']>=25000) and (DICT['amount']<=45000)):
            browser.find_element_by_id("tab-4").click()
            bCh = ch(browser.find_element_by_id("container-selection-4"), bChb)
        else:
            CreateWin("Error in the selection price or limit: incorrect value")

        firstname = browser.find_element_by_id("firstname")
        lastname = browser.find_element_by_id("lastname")
        mobile = browser.find_element_by_id("mobile")
        email = browser.find_element_by_id("email")
        chb1 = browser.find_element_by_id("checkbox1")
        chb2 = browser.find_element_by_id("checkbox2")
        but = browser.find_element_by_id("container-form-submit")
            
        firstname.send_keys(DICT['firstname'])
        lastname.send_keys(DICT['lastname'])
        mobile.send_keys(DICT['mob_number'] )
        email.send_keys(DICT['email'])
        if (DICT['ch1'] == True):
            chb1.click()
        if (DICT['ch2'] == True):
            chb2.click()

        if ((bCh['amount'] is None) or (bCh['limit'] is None)):
            CreateWin("Error in the selection price or limit: incorrect value")
        else:
            try:
                bCh['amount'].find_element_by_css_selector(".radio-checked")
                bCh['limit'].find_element_by_css_selector(".radio-checked") 
            except NoSuchElementException:
                CreateWin("Error in the selection price or limit: wrong selection")
        if ((firstname.get_attribute('value') != DICT['firstname']) or (firstname.get_attribute('value') == '')):
            CreateWin("Error in the field: 'firstname'")
        elif ((lastname.get_attribute('value') != DICT['lastname']) or (lastname.get_attribute('value') == '')):
            CreateWin("Error in the field: 'lastname'")
        elif ((mobile.get_attribute('value') != DICT['mob_number']) or (mobile.get_attribute('value') == '')):
            CreateWin("Error in the field: 'mobile'")
        elif ((email.get_attribute('value') != DICT['email']) or (email.get_attribute('email') == '')):
            CreateWin("Error in the field: 'email'")
        else:
#            but.click()
            CreateWin("Sending form to server")

        
    
