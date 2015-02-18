from django.contrib.auth.models import User, Group
from rest_framework import generics,viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response                                         
from rest_framework import status

from api.renderers import EmberJSONRenderer 
from api.filters import SearchFilter
from api.serializers import PpfaTestSerializer, PpfaTestRunSerializer,\
        PpfaTestAssertionSerializer, CustomPaginationSerializer,\
        PpfaTestStepSerializer, PpfaTestStepTypeSerializer
from api import mixins
from django.core.management import call_command
from StringIO import StringIO 
from operis.log import log

from selenium_tests.models import PpfaTest,PpfaTestRun,PpfaTestAssertion,PpfaTestStep, PpfaTestStepType
from selenium_tests.testrunner import runTest

class PpfaTestsView(mixins.ListByIdMixin, generics.ListCreateAPIView):
    model = PpfaTest
    serializer_class = PpfaTestSerializer
    filter_fields = ['name','location'] 
    renderer_classes = (EmberJSONRenderer,)
    filter_backends = (SearchFilter,)
    search_fields = ['name']
        
class PpfaTestView(mixins.ListByIdMixin, generics.RetrieveUpdateDestroyAPIView):
    model = PpfaTest
    serializer_class = PpfaTestSerializer
    renderer_classes = (EmberJSONRenderer,)
    
    def pre_save(self, obj):
        """
        Set any attributes on the object that are implicit in the request.
        """
        super(PpfaTestView, self).pre_save(obj)
        
        setattr(obj,'status',self.request.DATA['status'])

class PpfaTestPpfaTestRunsView(mixins.ChildrenByIdMixin, generics.ListCreateAPIView):
    model = PpfaTestRun
    serializer_class = PpfaTestRunSerializer
    filter_fields = ['date_created',] 
    renderer_classes = (EmberJSONRenderer,)
    filter_backends = (SearchFilter,)
    search_fields = ['date_created']
    ordering = ('-date_created',)
    
class PpfaTestRunsView(mixins.ListByIdMixin, generics.ListCreateAPIView):
    model = PpfaTestRun
    serializer_class = PpfaTestRunSerializer
    filter_fields = ['date_created',] 
    renderer_classes = (EmberJSONRenderer,)
    filter_backends = (SearchFilter,)
    search_fields = ['date_created']
    ordering = ('-date_created',)
    
    def pre_save(self, obj):
        """
        Set any attributes on the object that are implicit in the request.
        """
        
        super(PpfaTestRunsView, self).pre_save(obj)
        
        setattr(obj,'ppfa_test_id',self.request.DATA['ppfa_test'])  
        
class PpfaTestRunView(generics.RetrieveUpdateDestroyAPIView):
    model = PpfaTestRun
    serializer_class = PpfaTestRunSerializer
    renderer_classes = (EmberJSONRenderer,)
    
    def pre_save(self, obj):
        """
        Set any attributes on the object that are implicit in the request.
        """
        super(PpfaTestRunView, self).pre_save(obj)   
    
class PpfaTestAssertionsView(mixins.ListByIdMixin, generics.ListCreateAPIView):
    model = PpfaTestAssertion
    serializer_class = PpfaTestAssertionSerializer
    filter_fields = ['subject','verb','object',] 
    renderer_classes = (EmberJSONRenderer,)
    filter_backends = (SearchFilter,)
    search_fields = ['subject','verb','object',] 
    ordering = ('id',)
        
class PpfaTestAssertionView(generics.RetrieveUpdateDestroyAPIView):
    model = PpfaTestAssertion
    serializer_class = PpfaTestAssertionSerializer
    renderer_classes = (EmberJSONRenderer,)
    
    def pre_save(self, obj):
        """
        Set any attributes on the object that are implicit in the request.
        """
        super(PpfaTestAssertionView, self).pre_save(obj)
        
        setattr(obj,'status',self.request.DATA['status'])

class PpfaTestStepsView(mixins.ListByIdMixin, generics.ListCreateAPIView):
    model = PpfaTestStep
    serializer_class = PpfaTestStepSerializer
    filter_fields = ['subject','verb','object',] 
    renderer_classes = (EmberJSONRenderer,)
    filter_backends = (SearchFilter,)
    search_fields = ['subject','verb','object',] 
    ordering = ('id',)
    
    def pre_save(self, obj):
        """
        Set any attributes on the object that are implicit in the request.
        """
        
        super(PpfaTestStepsView, self).pre_save(obj)
        
        setattr(obj,'ppfa_test_id',self.request.DATA['ppfa_test'])  
            
class PpfaTestStepView(generics.RetrieveUpdateDestroyAPIView):
    model = PpfaTestStep
    serializer_class = PpfaTestStepSerializer
    renderer_classes = (EmberJSONRenderer,)
    
    def pre_save(self, obj):
        """
        Set any attributes on the object that are implicit in the request.
        """
        super(PpfaTestStepView, self).pre_save(obj)   
        
        setattr(obj,'ppfa_test_id',self.request.DATA['ppfa_test'])

class PpfaTestStepTypesView(mixins.ListByIdMixin, generics.ListCreateAPIView):
    model = PpfaTestStepType
    serializer_class = PpfaTestStepTypeSerializer
    filter_fields = ['name',] 
    renderer_classes = (EmberJSONRenderer,)
    filter_backends = (SearchFilter,)
    search_fields = ['name',] 
    ordering = ('id',)
    paginate_by = 0
    
    def pre_save(self, obj):
        """
        Set any attributes on the object that are implicit in the request.
        """
        
        super(PpfaTestStepTypesView, self).pre_save(obj)
         
            
class PpfaTestStepTypeView(generics.RetrieveUpdateDestroyAPIView):
    model = PpfaTestStepType
    serializer_class = PpfaTestStepTypeSerializer
    renderer_classes = (EmberJSONRenderer,)
    paginate_by = 0
    
    def pre_save(self, obj):
        """
        Set any attributes on the object that are implicit in the request.
        """
        super(PpfaTestStepTypeView, self).pre_save(obj)   
        
class PpfaTestRunExec(mixins.ListByIdMixin, generics.RetrieveUpdateDestroyAPIView):
    
    model = PpfaTestRun
    serializer_class = PpfaTestRunSerializer
    filter_fields = ['date_created',] 
    renderer_classes = (EmberJSONRenderer,)
    filter_backends = (SearchFilter,)
    search_fields = ['date_created']
    ordering = ('-date_created',)
    
    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        test = request.GET.get('location')
        run = request.GET.get('run')
        
        runTest(test,run,log())
        self.object = PpfaTestRun.objects.get(pk=run)
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)
        #if result:
        #    
        #else:
        #    return Response(status=status.HTTP_204_NO_CONTENT)
        #return Response(result) 

class PpfaTestRunTest(mixins.ListByIdMixin, generics.RetrieveUpdateDestroyAPIView):
    
    model = PpfaTestRun
    serializer_class = PpfaTestRunSerializer
    filter_fields = ['date_created',] 
    renderer_classes = (EmberJSONRenderer,)
    filter_backends = (SearchFilter,)
    search_fields = ['date_created']
    ordering = ('-date_created',)
    
    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        self.object = PpfaTestRun.objects.get(pk=297)
        #self.object = self.get_object()
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)
            
        #return Response(status=status.HTTP_204_NO_CONTENT)
        #return Response(result) 
