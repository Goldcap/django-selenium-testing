import os
import json
import redis
import shutil
import datetime

from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
from pyvirtualdisplay import Display


from selenium import webdriver                 
from django.test import TestCase
from django.conf import settings
from selenium_tests.models import PpfaTestAssertion

class PpfaWebDriver(TestCase):
    
    browser = None
    profile = None
    logger = None
    testObject = None  
    runObject = None
    errors = []
    publisher = None
    
    profile_path = None
    
    redis_key = "proxy_request"
    redis_session = 1
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    
    assert_failed_requests = True
    
    def __init__(self, *args, **kw):
        
        self.r = redis.StrictRedis(host=self.REDIS_HOST, port=self.REDIS_PORT, db=0)
        session = self.r.get("proxy_request")
        if session:
            self.redis_session = session
        #print self.redis_session
        
        super(PpfaWebDriver, self).__init__(*args, **kw)
        
    def set_up(self):
        self.clearSession(200)
        self.clearSession(404)
        self.clearSession(500)
        
        self.publisher = RedisPublisher(facility='foobar', broadcast=True)
    
        self.broadcast("Starting Test '"+self.runObject.ppfa_test.name+"'")
        self.startup()       
        
    def count_requests(self):
        
        requests_200 = self.getSession(200)
        self.broadcast("Total Requests (200): %s" % len(requests_200))
        
        requests_404 = self.getSession(404)
        self.broadcast("Total Requests (404): %s" % len(requests_404))
        if len(requests_404) > 0 and self.assert_failed_requests:
            self.failassertion( "Assets Missing", "from", "pageload"  )
            for failure in requests_404:
                print failure
                self.broadcast(failure)
            
        requests_500 = self.getSession(500)
        self.broadcast("Total Requests (500): %s" % len(requests_500))
        if len(requests_500) > 0 and self.assert_failed_requests:
            self.failassertion( "Assets Broken", "from", "pageload"  )
            for failure in requests_500:
                print failure
                self.broadcast(failure)
            
    def tear_down(self):
        
        self.count_requests()
        
        if self.shut_down():
            return self.runObject
            
    def startup(self):
        
        self.broadcast("Starting Xvfb Display")
        display = Display(visible=0, size=(1024, 768))
        display.start()
 
        self.broadcast("Starting Firefox Browser")
        self.profile = webdriver.FirefoxProfile()
        # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
        self.profile.set_preference("network.proxy.type", 1)
        self.profile.set_preference("network.proxy.http",settings.PROXY_HOST)
        self.profile.set_preference("network.proxy.http_port",int(settings.PROXY_PORT))
        self.profile.set_preference("network.proxy.ssl",settings.PROXY_HOST)
        self.profile.set_preference("network.proxy.ssl_port",int(settings.PROXY_PORT))
        self.profile.set_preference("general.useragent.override","ppfa_test_runner")
        self.profile.update_preferences()
        self.profile_path = os.path.join('tmp',self.profile.profile_dir)
        #print "Destination is in %s" % self.profile_path
        source = os.path.join(os.path.dirname(__file__),'cert8.db')
        #print "Source is in %s" % source
        shutil.copy2(source, self.profile_path)
        
        self.browser = webdriver.Firefox(self.profile)       
            
    def setSession( self, id ):
        self.redis_session = id
        self.r.set(self.redis_key,self.redis_session)
    
    def clearSession( self, status ):
        self.r.zremrangebyrank(self.redis_key+"::"+str(status)+"::"+str(self.redis_session),0,-1)
        
    def getSession( self, status ):
        print "Looking for %s" % (self.redis_key+"::"+str(status)+"::"+str(self.redis_session))
        results = self.r.zrange(self.redis_key+"::"+str(status)+"::"+str(self.redis_session),0,-1)
        return results
    
    def page_source(self):
        time = datetime.datetime.now().strftime("%I%M%p_%B_%d_%Y")
        path = "screens/"+str(self.runObject.id)
        if not os.path.exists(path):
            os.mkdir(path)
        filename = self.redis_key+"_"+str(self.redis_session)+"_"+str(time)+".html"
        with open(os.path.join(path, filename), 'wb') as temp_file:
            temp_file.write(self.browser.page_source.encode('ascii','replace'))
        
    def screencap(self):
        time = datetime.datetime.now().strftime("%I%M%p_%B_%d_%Y")
        path = "screens/"+str(self.runObject.id)
        if not os.path.exists(path):
            os.mkdir(path)
        filename = self.redis_key+"_"+str(self.redis_session)+"_"+str(time)+".png"
        print filename
        self.browser.save_screenshot(os.path.join(path, filename))
                
    def broadcast( self, message ):
        print message
        if self.publisher:
            message = {"message":message}
            self.publisher.publish_message(RedisMessage(json.dumps(message)))
            
    def runassertion( self, subject, verb, object  ):
        assertion = PpfaTestAssertion.objects.create(
                        ppfa_test=self.testObject,
                        ppfa_test_run=self.runObject,
                        subject=subject,
                        verb=verb,
                        object=object,
                    )
        result = assertion.run_assertion(self.browser)
        status_type = 'success'
        if not result:
            self.errors.append(assertion.id)
            status_type = 'error'
        self.logger.log("'%s' %s %s:: %s",[subject, verb, object, assertion.status_string],status_type)
        self.broadcast("'%s' %s %s:: %s" % (subject, verb, object, assertion.status_string,))
        return result
        
    def passassertion( self, subject, verb, object  ):
        assertion = PpfaTestAssertion.objects.create(
                        ppfa_test=self.testObject,
                        ppfa_test_run=self.runObject,
                        subject=subject,
                        verb=verb,
                        object=object,
                        status=True
                    )
        status_type = 'success'
        self.logger.log("'%s' %s %s:: %s",[subject, verb, object, assertion.status_string],status_type)
        self.broadcast("'%s' %s %s:: %s" % (subject, verb, object, assertion.status_string,))
        return False
        
    def failassertion( self, subject, verb, object  ):
        assertion = PpfaTestAssertion.objects.create(
                        ppfa_test=self.testObject,
                        ppfa_test_run=self.runObject,
                        subject=subject,
                        verb=verb,
                        object=object,
                        status=False
                    )
        self.errors.append(assertion.id)
        status_type = 'error'
        self.logger.log("'%s' %s %s:: %s",[subject, verb, object, assertion.status_string],'error')
        self.broadcast("'%s' %s %s:: %s" % (subject, verb, object, assertion.status_string,))
        return False
        
    def is_element_present(self, how, what):
        try: self.browser.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.browser.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.browser.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
        
    def shut_down(self):
        self.broadcast("Done Testing")
        self.browser.quit()
        for root, dirs, files in os.walk(self.profile_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        return True
        
    
        
