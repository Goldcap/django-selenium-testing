import sys
import os.path
import importlib
from inspect import getmembers, isclass
from collections import defaultdict
from optparse import make_option

from django.utils import timezone   
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db.models.base import ModelBase
 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from operis.log import log
from selenium_tests.models import PpfaTest, PpfaTestRun

def runTest(location,run,logger):
    
    try:
        run = PpfaTestRun.objects.get(pk=run)
    except PpfaTestRun.DoesNotExist:
        return None
        
    test = run.ppfa_test
    
    logger.log("Found Test %s",[test.name],"debug")
    
    thetest = "selenium_tests.tests.%s" % test.location
    module = importlib.import_module(thetest)
    for name, obj in getmembers(module, lambda member: isclass(member) and member.__module__ == thetest):
        logger.log("Found Test Class %s",[name],"notice")
        #try:
        aclass = getattr(module,name)
        object = aclass()
        object.logger = logger
        object.testObject = test
        object.runObject = run        
        object.set_up()
            #try:
        object.runTest()
            #except:
            #    pass
        object.tear_down()
        #except:
        #    pass
        logger.log("Had Errors: %s",[len(object.errors)],"notice")
        if (len(object.errors) == 0):
            test.status = True
            run.status = True
            run.save()    
        
        test.last_run = run.date_created
        test.save()
        
        #if (test_result):
        #    return test_result
        #return None
        #self.logger.log("No Test Found in %s",[name],"error")