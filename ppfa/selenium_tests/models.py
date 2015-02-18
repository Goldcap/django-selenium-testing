from datetime import datetime
from django.utils import timezone   

from django.db import models
from django.contrib.auth.models import User, Group 


#http://stackoverflow.com/questions/1760421/how-can-i-render-a-manytomanyfield-as-checkboxes
class Profile(models.Model):
    """
    """
    user = models.ForeignKey(User, blank=True, null=True, unique=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DateSubmitted = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    
    Approved = models.IntegerField(default=-1)
    
    def __str__(self):
        return "%s %s" % (self.FirstName, self.LastName)
    
    def __unicode__(self):
        return "%s %s" % (self.FirstName, self.LastName)
        
    @property
    def last_login(self):
        try:
            al = ActivityLog.objects.filter(user=self.user,activity='Login').order_by('-DateAdded')[0]
            return al.DateAdded
        except:
            return None
            
#http://stackoverflow.com/questions/1760421/how-can-i-render-a-manytomanyfield-as-checkboxes
class PpfaTest(models.Model):
    """
    """
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_created = models.DateTimeField(blank=True, null=True)
    last_run = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(blank=True, default=False)
    
    class Meta:
        verbose_name_plural = "PpfaTests"
        
    class Ember:
        #This will show up as the title
        index_list = ['Name','Location','DateCreated','LastRun','Status','Runs','Assertions']
        fields = ['name','location','date_created','last_run','status']
    
    @property
    def status_string(self):
        return "Success" if ( self.status == 1 ) else "Failure"

    def __str__(self):
        return "%s (%s - %s)" % (self.name, self.last_run, self.status_string)
    
    def __unicode__(self):
        return "%s (%s - %s)" % (self.name, self.last_run, self.status_string)
        
class PpfaTestRun(models.Model):
    """
    """
    ppfa_test = models.ForeignKey(PpfaTest, related_name='ppfa_test_runs')
    date_created = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    status = models.BooleanField(blank=True, default=False)
    
    class Meta:
        verbose_name_plural = "PpfaTestRuns"
        
    class Ember:
        #This will show up as the title
        index_list = ['Test','DateCreated','Status']
        fields = ['ppfa_test','date_created','status']
    
    def __str__(self):
        return "%s (#%s) on %s" % (self.ppfa_test.name, self.id, self.date_created)
    
    def __unicode__(self):
        return "%s (#%s) on %s" % (self.ppfa_test.name, self.id, self.date_created)

#http://stackoverflow.com/questions/1760421/how-can-i-render-a-manytomanyfield-as-checkboxes
class PpfaTestAssertion(models.Model):
    """
    """
    subject = models.CharField(max_length=100)
    verb = models.CharField(max_length=100)
    object = models.CharField(max_length=100)
    status = models.BooleanField(blank=True, default=False)
    ppfa_test_run = models.ForeignKey(PpfaTestRun, related_name='ppfa_test_assertion_run')
    ppfa_test = models.ForeignKey(PpfaTest, related_name='ppfa_test_assertion_test')
    
    class Meta:
        verbose_name_plural = "PpfaTestAssertions"
        
    class Ember:
        #This will show up as the title
        index_list = ['Subject','Verb','Object','Status','Run','Test']
        fields = ['subject','verb','object','status','ppfa_test_run','ppfa_test']
    
    @property
    def status_string(self):
        return "Success" if ( self.status == 1 ) else "Failure"

    def __str__(self):
        return "%s %s %s" % (self.subject, self.verb, self.object)
    
    def __unicode__(self):
        return "%s %s %s" % (self.subject, self.verb, self.object)
        
    def run_assertion(self,browser):
        try:
            if self.verb == "equals":
                assert self.subject == getattr(browser,self.object)
            elif self.verb == "has":
                assert self.subject in getattr(browser,self.object)
            self.status = True
        except AssertionError:
            self.status = False
        self.save()
        return self.status

class PpfaTestStep(models.Model):
    """
    """
    subject = models.CharField(max_length=100)
    verb = models.CharField(max_length=100)
    object = models.CharField(max_length=100)
    ppfa_test = models.ForeignKey(PpfaTest, related_name='ppfa_test_steps')
    
    class Meta:
        verbose_name_plural = "PpfaTestSteps"
        
    class Ember:
        #This will show up as the title
        index_list = ['Subject','Verb','Object','Test']
        fields = ['subject','verb','object','ppfa_test']
    
    def __str__(self):
        return "%s %s %s" % (self.subject, self.verb, self.object)
    
    def __unicode__(self):
        return "%s %s %s" % (self.subject, self.verb, self.object)

class PpfaTestStepType(models.Model):
    """
    """
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "PpfaTestStepTypes"
        
    class Ember:
        #This will show up as the title
        index_list = ['Name']
        fields = ['name']
    
    def __str__(self):
        return "%s" % (self.name,)
    
    def __unicode__(self):
        return "%s" % (self.name,)
                
class PpfaTestRequest(models.Model):
    """
    """
    ppfa_test = models.ForeignKey(PpfaTest, related_name='ppfa_test_queue_test')
    request_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "PpfaTestRequests"
        
    class Ember:
        #This will show up as the title
        index_list = ['Date','Test',]
        fields = ['request_date', 'ppfa_test',]
    
    def __str__(self):
        return "%s on %s" % (self.test, self.request_date)
    

    def __str__(self):
        return "%s on %s" % (self.test, self.request_date)
        

    