                     
import sys
import os.path
import importlib
from inspect import getmembers, isclass
from collections import defaultdict
from optparse import make_option

from django.utils import timezone   
from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db.models.base import ModelBase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from operis.log import log
from selenium_tests.models import PpfaTest, PpfaTestRun

#This command takes an input table of artifacts, of a specific format,
#And ensures that image attatchments for each artifact in the table are created
#Then sets those images up to be parsed by the IKGEN.py

class Command(BaseCommand):
    help = 'Selenium Test Runner' 
    logger = None
    
    """
    option_list = BaseCommand.option_list + (
        make_option('--regenerate',
            action='store_true',
            dest='regenerate',
            default=False,
            help='Wipe Prior instances'),
        )
    """

    def handle(self, *args, **options):
        
        self.logger = log( self )
        
        self.logger.log("Starting Tests for %s",["Python"],"info")
        
        tests = PpfaTest.objects.all()
        for test in tests:
            self.logger.log("Found Test %s",[test.name],"debug")
            run = PpfaTestRun.objects.create(ppfa_test=test,
                               date_created=timezone.now()
                               )
        
            thetest = "selenium_tests.tests.%s" % test.location
            module = importlib.import_module(thetest)
            for name, obj in getmembers(module, lambda member: isclass(member) and member.__module__ == thetest):
                self.logger.log("Found Test Class %s",[name],"notice")
                try:
                    aclass = getattr(module,name)
                    object = aclass()
                    object.logger = self.logger
                    object.testObject = test
                    object.runObject = run
                    object.test()
                except:
                    pass
                self.logger.log("Had Errors: %s",[len(object.errors)],"notice")
                if (len(object.errors) == 0):
                    test.status = True
                    run.status = True
                    run.save()    
                
                test.last_run = run.date_created
                test.save()
                #self.logger.log("No Test Found in %s",[name],"error")