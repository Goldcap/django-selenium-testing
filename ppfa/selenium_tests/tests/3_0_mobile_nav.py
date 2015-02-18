import datetime
import json
from datetime import time,date,timedelta
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
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
#from selenium_tests.models import PpfaTest, PpfaTestAssertion

class BaseTests( PpfaWebDriver ):
    
    def runTest(self):
        
        self.broadcast("Waiting 2 Seconds")
        self.browser.implicitly_wait(2)
        
        self.base_url = "uat.ppfa.net"
        
        self.broadcast("Getting Base URL")
        self.browser.get("http://ppfa_users:ppfa_me@"+self.base_url)
        
        navpages = ['/index.php?cID=373',
                    '/index.php?cID=17566',
                    '/index.php?cID=262',
                    '/index.php?cID=3460',
                    '/index.php?cID=3470',
                    '/index.php?cID=189',
                    '/index.php?cID=16907',
                    '/index.php?cID=17270',
                    '/index.php?cID=4241',]   
        
        self.broadcast("Looking for Navigation Items")
        for navpage in navpages:
            self.broadcast("Getting Page " + navpage)
            self.browser.get("http://" + self.base_url + navpage)
            self.broadcast("GOT")
            try:
                navitem = self.browser.find_element_by_class_name('inner-sub-nav')
                self.passassertion( "NAV item on", navpage, "found" )
            except NoSuchElementException:
                self.failassertion( "NAV item on", navpage, "not found" )
                
        
       
           
            
            