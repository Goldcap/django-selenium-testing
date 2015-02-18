import datetime
import json
from datetime import date,timedelta

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from operis.log import log
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher

from selenium_tests.webdriver import PpfaWebDriver
#from selenium_tests.models import PpfaTest, PpfaTestAssertion

class BaseTests( PpfaWebDriver ):
    
    def runTest(self):
        
        self.assert_failed_requests = False
        
        self.broadcast("Loading http://www.python.org")
        self.browser.get("http://www.python.org")
        
        self.runassertion( "Welcome to Python.org", "equals", "title" )
        self.runassertion( "Python", "in", "title" )
        