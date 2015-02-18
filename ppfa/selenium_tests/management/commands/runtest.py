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
from selenium_tests.testrunner import runTest

#This command takes an input table of artifacts, of a specific format,
#And ensures that image attatchments for each artifact in the table are created
#Then sets those images up to be parsed by the IKGEN.py

class Command(BaseCommand):
    help = 'Selenium Test Runner' 
    logger = None
    
    def handle(self, *args, **options):
        
        self.logger = log( self )
        self.logger.log("Starting Tests for %s",["Python"],"info")
        
        test = PpfaTest.objects.get(location=args[0])
        run = PpfaTestRun.objects.create(ppfa_test=test,
                               date_created=timezone.now()
                               )
        
        runTest(args[0],run.pk,self.logger)