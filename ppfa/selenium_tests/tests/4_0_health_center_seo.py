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
        
        cases = []
        case = {"url":"/health-center/colorado/alamosa/81101/alamosa-2153-90210",
                    "title":"Birth Control, STD Testing & Abortion - Alamosa, CO",
                    "description":"Visit Alamosa for family planning services, including STD testing and abortions. Make an appointment with Planned Parenthood."}
        cases.append(case)
        case = {"url":"/health-center/florida/tallahassee/32304/the-sally-bellamy-health-center-2154-90270",
                    "title":"Birth Control & STD Testing - Tallahassee, FL",
                    "description":"Visit The Sally Bellamy Health Center for family planning services, including STD testing. Make an appointment with Planned Parenthood."}
        cases.append(case)
        case = {"url":"/health-center/ohio/cincinnati/45219/elizabeth-campbell-surgical-center-3347-91260",
                    "title":"Family Planning & Abortion Clinic - | Cincinnati, OH",
                    "description":"Visit Elizabeth Campbell Surgical Center for family planning and abortion services. Make an appointment with Planned Parenthood."}
        cases.append(case)
        case = {"url":"/health-center/pennsylvania/west-chester/19382/west-chester-surgical-center-3918-91460",
                    "title":"Family Planning & Abortion Clinic - | West Chester, PA",
                    "description":"Visit West Chester Surgical Center for family planning and abortion services. Make an appointment with Planned Parenthood."}
        cases.append(case)
        case = {"url":"/health-center/missouri/st.-louis/63108/reproductive-health-services-of-ppslr-3302-90770",
                    "title":"Family Planning & Abortion Clinic - | St. Louis, MO",
                    "description":"Visit Reproductive Health Services of PPSLR for family planning and abortion services. Make an appointment with Planned Parenthood."}
        cases.append(case)
        case = {"url":"/health-center/indiana/indianapolis/46268/georgetown-health-center-2870-90500",
                    "title":"Family Planning & Abortion Clinic - | Indianapolis, IN",
                    "description":"Visit Georgetown Health Center for family planning and abortion services. Make an appointment with Planned Parenthood."}
        cases.append(case)
        case = {"url":"/health-center/texas/houston/77023/prevention-park-dysplasia-clinic-3497-91650",
                    "title":"Family Planning in Texas - Houston, TX",
                    "description":"Visit Prevention Park Dysplasia Clinic for family planning services. Make an appointment with Planned Parenthood."}
        cases.append(case)
        
        
        for case in cases:
            self.broadcast("Getting Case")
            self.browser.get("http://ppfa_users:ppfa_me@" + self.base_url + case["url"])
            self.runassertion( case["title"], "equals", "title" )
            
            titleTag = self.browser.find_element_by_xpath("//meta[@name='title']")
            titleValue = titleTag.get_attribute("content")
            print "'" + titleValue + "'"
            if titleValue.strip(' \t\n\r') == case["title"]:
                self.passassertion( "Title Meta Tag", "is", "correct" )
            else:
                self.failassertion( "Title Meta Tag", "is", "incorrect" )
                
            descriptionTag = self.browser.find_element_by_xpath("//meta[@name='description']")
            descriptionValue = descriptionTag.get_attribute("content")
            print "'" + descriptionValue + "'"
            if descriptionValue.strip(' \t\n\r') == case["description"]:
                self.passassertion( "Description Meta Tag", "is", "correct" )
            else:
                self.failassertion( "Description Meta Tag", "is", "incorrect" )
           
        