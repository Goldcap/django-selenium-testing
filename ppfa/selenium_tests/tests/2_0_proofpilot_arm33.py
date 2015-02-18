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
        
        self.broadcast("Loading http://uat.ppfa.net/php_redirect.php")
        self.base_url = "http://uat.ppfa.net"
        
        self.browser.get("http://ppfa_users:ppfa_me@uat.ppfa.net/php_redirect.php")
        
        self.broadcast("Entering PID")
        # find the element that's name attribute is q (the google search box)
        inputElement = self.browser.find_element_by_name("pid")
        
        # type in the search
        inputElement.send_keys("123456")

        self.broadcast("Entering ARM (33)")
        # find the element that's name attribute is q (the google search box)
        inputElement = self.browser.find_element_by_name("arm")
        
        # type in the search
        inputElement.send_keys("33")
        
        self.broadcast("Submitting Form")
        button = self.browser.find_element_by_class_name('btn-primary')
        button.click()
        
        try:
            # we have to wait for the page to refresh, the last thing that seems to be updated is the title
            WebDriverWait(self.browser, 10).until(EC.title_contains("ProofPilot"))
        
            # You should see "cheese! - Google Search"
            self.broadcast("Redirected to ProofPilot")
        
            self.passassertion( "Redirect", "to", "ProofPilot" )
        
        except:
            self.failassertion( "Redirect", "to", "ProofPilot" )
        
        self.broadcast("Loading Planned Parenthood")
        self.browser.get(self.base_url)
        
        now = datetime.date.today()
        arm = self.browser.get_cookie("_pau")
        pid = self.browser.get_cookie("_pap")
        pad = self.browser.get_cookie("_pad")
        
        if arm['value'] == "33":
           self.passassertion( "ARM", "value", "found" )
           self.broadcast("Found ARM Cookie")
        else:
           self.failassertion( "ARM", "value", "not found" )
           self.broadcast("Didn't find ARM Cookie")
            
            
        if pid['value'] == "123456":
           self.passassertion( "PID", "value", "found" )
           self.broadcast("Found PID Cookie")
        else:
           self.failassertion( "PID", "value", "not found" )
           self.broadcast("Didn't find PID Cookie")
           
        if pad['value'] == str(now):
           self.passassertion( "DATE", "value", "found" )
           self.broadcast("Found DATE Cookie")
        else:
           self.failassertion( "DATE", "value", "not found" )
           self.broadcast("Didn't find DATE Cookie")
        
        chatpages = ['/health-info/birth-control/birth-control-pill',
                    '/health-info/birth-control/withdrawal-pull-out-method',
                    '/health-info/birth-control/birth-control-vaginal-ring-nuvaring',
                    '/health-info/birth-control/birth-control-patch-ortho-evra',
                    '/health-topics/abortion-4260.asp',
                    '/health-topics/emergency-contraception-morning-after-pill-4363.asp',
                    '/health-topics/pregnancy/pregnancy-test-21227.asp',
                    '/info-for-teens/',
                    '/info-for-teens/pregnancy-33811.asp',
                    '/info-for-teens/pregnancy/im-pregnant-now-what-33830.asp',
                    '/info-for-teens/pregnancy/am-pregnant-33831.asp']   
        
        for chatpage in chatpages:
            self.browser.get(self.base_url + chatpage)
            try:
                chatitem = self.browser.find_element_by_class_name('lpchat-container')
                self.passassertion( "CHAT item on", chatpage, "found" )
            except NoSuchElementException:
                self.failassertion( "CHAT item on", chatpage, "not found" )
                
        hcpages = [ '/health-center/WI',
                    '/health-center/wisconsin/appleton/54911/appleton-central-health-center-2578-91860',
                    '/health-center/IL',
                    '/health-center/illinois/aurora/60504/aurora-health-center-3483-90430']
        
        for hcpage in hcpages:
            self.browser.get(self.base_url + hcpage)
            try:
                chatitem = self.browser.find_element_by_name('docasap')
                self.failassertion( "OAS item on", hcpage, "found" )
            except NoSuchElementException:
                self.passassertion( "OAS item on", hcpage, "not found" )
                
        
       
           
            
            