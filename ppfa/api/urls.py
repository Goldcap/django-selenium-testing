from django.conf.urls import patterns, url, include
from rest_framework import viewsets, routers
from api.views import PpfaTestView, PpfaTestsView, PpfaTestRunView, PpfaTestRunsView, PpfaTestAssertionView, \
                        PpfaTestAssertionsView, PpfaTestStepView, PpfaTestStepsView, PpfaTestRunExec, \
                        PpfaTestStepTypesView, PpfaTestStepTypeView, PpfaTestPpfaTestRunsView, PpfaTestRunTest


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^api/ppfaTests/(?P<pk>\d+)/ppfaTestRuns($|/$)', PpfaTestPpfaTestRunsView.as_view()),
    url(r'^api/ppfaTests/(?P<pk>\d+)($|/$)', PpfaTestView.as_view()),
    url(r'^api/ppfaTests($|/$)', PpfaTestsView.as_view()),        
    url(r'^api/ppfaTestRuns/(?P<pk>\d+)($|/$)', PpfaTestRunView.as_view()),
    url(r'^api/ppfaTestRuns($|/$)', PpfaTestRunsView.as_view()),         
    url(r'^api/ppfaTestAssertions/(?P<pk>\d+)($|/$)', PpfaTestAssertionView.as_view()),
    url(r'^api/ppfaTestAssertions($|/$)', PpfaTestAssertionsView.as_view()),
    url(r'^api/ppfaTestSteps/(?P<pk>\d+)($|/$)', PpfaTestStepView.as_view()),
    url(r'^api/ppfaTestSteps($|/$)', PpfaTestStepsView.as_view()),
    url(r'^api/ppfaTestStepTypes/(?P<pk>\d+)($|/$)', PpfaTestStepTypeView.as_view()),
    url(r'^api/ppfaTestStepTypes($|/$)', PpfaTestStepTypesView.as_view()),
    url(r'^api/ppfaTestRunExec($|/$)', PpfaTestRunExec.as_view()),            
    url(r'^api/ppfaTestRunTest/(?P<pk>\d+)($|/$)', PpfaTestRunTest.as_view()),            
)
