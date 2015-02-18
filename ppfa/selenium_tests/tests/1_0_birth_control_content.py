import datetime
import json
from datetime import date,timedelta
import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from operis.log import log
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher

from selenium_tests.webdriver import PpfaWebDriver
#from selenium_tests.models import PpfaTest, PpfaTestAssertion

class BaseTests( PpfaWebDriver ):
    
    def runTest(self):
        
        self.broadcast("Waiting 30 Seconds")
        self.browser.implicitly_wait(30)
        
        self.broadcast("Loading http://www.google.com")
        self.base_url = "https://www.google.com/"
        
        self.browser.get(self.base_url + "/")
        
        self.broadcast("Searching for PPFA on Google")
        self.browser.get(self.base_url + "search?q=ppfa")
        self.screencap()
        self.page_source()
        
        #try:
            #try:
                #self.broadcast("Searching for PPFA with 'gs_htif0'")
                #id = 'gs_htif0'
                #self.browser.find_element_by_xpath("//input[@id='"+id+"']").clear()
            #except:
            #    self.broadcast("Searching for PPFA with 'gbqfq'")
            #    id = 'gbqfq'
            #    self.browser.find_element_by_xpath("//input[@id='"+id+"']").clear()
            #self.browser.find_element_by_xpath("//input[@id='"+id+"']").send_keys("PPFA")
            #self.browser.find_element_by_xpath("//button[@id='"+id+"']").click()
        
        #except:
            #self.broadcast("Google Search Not Found, Forcing QS")
            #self.browser.get(self.base_url + "/#q=ppfa")
            #return None
                
        
        for i in range(60):
            try:
                self.broadcast("Checking For Results") 
                if self.is_element_present(By.XPATH, "//div[@id='resultStats']"): 
                    self.broadcast("Received Search Results")
                    doPpfa = True
                    break
            except:
                self.broadcast("Waiting One Second For Results") 
                doPpfa = False
                pass
            time.sleep(1)
        else:       
            self.failassertion( "Google Result", "load", "Timeout" )
        
        if doPpfa:            
            self.broadcast("Scanning Search Results for 'Planned'")
            if self.is_element_present(By.XPATH, "//a[descendant::b[contains(text(),'Planned')]]"): 
                self.passassertion( "Google Result", "contains", "Planned" )
                self.browser.find_element_by_xpath("//a[descendant::b[contains(text(),'Planned')]]").click()
                self.broadcast("Waiting for Pageload of Planned Parenthood")
                
                for i in range(60):
                    try:
                        self.broadcast("Checking For Pageload") 
                        if self.is_element_present(By.XPATH, "//nav[@id='main-nav']"): 
                            self.broadcast("Received Pageload")
                            self.passassertion( "Planned Parenthood", "has", "loaded" )                    
                            doBC = True
                            break
                    except:
                        self.broadcast("Waiting One Second For Pageload") 
                        dodoBCPpfa = False
                        pass
                    time.sleep(1)
                else:       
                    self.failassertion( "PPFA Homepage", "has not", "loaded" )
                
                if doBC:
                    self.broadcast("Navigating to 'Birth Control'")
                    if self.is_element_present(By.XPATH, ("(//nav[@id='main-nav']/descendant::ul/descendant::li[1]/descendant::ul/descendant::a[contains(text(),'Birth Control')])")):
                        self.passassertion( "Birth Control Link", "does", "exist" )                    
                        self.browser.get("http://www.plannedparenthood.org/health-info/birth-control")
                        if self.is_element_present(By.XPATH, "//h1[contains(text(),'Birth Control')]"): 
                            self.passassertion( "Birth Control Page", "has", "loaded" )
                            self.broadcast("Arrived at 'Birth Control'")
            
        #self.runassertion( "Welcome to Python.org", "equals", "title" )
        #self.runassertion( "Python", "in", "title" )
        