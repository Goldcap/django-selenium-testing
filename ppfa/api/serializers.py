from django.contrib.auth.models import User, Group   
from django.conf import settings   
from rest_framework import pagination
from rest_framework import serializers
from api import fields

from selenium_tests.models import PpfaTest,PpfaTestRun,PpfaTestAssertion,PpfaTestStep, PpfaTestStepType

class CustomMetaSerializer(serializers.Serializer):
    count = serializers.Field(source='paginator.count')
    num_pages = serializers.Field(source='paginator.num_pages')
    current_page = fields.CurrentPageField(source='paginator')
    rpp = serializers.Field(source='paginator.per_page')
    
class CustomPaginationSerializer(pagination.BasePaginationSerializer):
    # Takes the page object as the source
    meta = CustomMetaSerializer(source='*')
    results_field = 'results'
    
class PpfaTestSerializer(serializers.ModelSerializer):
    
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(required=False,
                                  max_length=100,
                                  source='name')
    location = serializers.CharField(required=False,
                                  max_length=100,
                                  source='location')  
    date_created = serializers.DateTimeField(required=False,
                                  format='iso-8601',
                                  source='date_created')
    last_run = serializers.DateTimeField(required=False,
                                  format='iso-8601',
                                  source='last_run')  
    status = serializers.CharField(required=False,
                                  max_length=100,
                                  source='status')
    ppfa_test_runs = serializers.PrimaryKeyRelatedField(many=True,read_only=True )
    ppfa_test_steps = serializers.PrimaryKeyRelatedField(many=True,read_only=True )
        
    class Meta:
        model = PpfaTest
        #meta_dict = dict()
        #meta_dict['foo'] = 'bar'
        resource_name = 'ppfa-tests'
        fields = ('id', 'name', 'location', 'date_created', 'last_run', 'status', 'ppfa_test_runs', 'ppfa_test_steps', )
        
    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.location = attrs.get('location', instance.location)
            return instance

        # Create new instance
        return PpfaTest(**attrs)

class PpfaTestRunSerializer(serializers.ModelSerializer):
    
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    date_created = serializers.DateTimeField(required=False,
                                  format='iso-8601',
                                  source='date_created')
    status = serializers.CharField(required=False,
                                  max_length=100,
                                  source='status')
    ppfa_test = serializers.PrimaryKeyRelatedField(read_only=True)
    ppfa_test_assertions = serializers.PrimaryKeyRelatedField(many=True, source='ppfa_test_assertion_run', read_only=True)
        
    class Meta:
        model = PpfaTestRun
        #meta_dict = dict()
        #meta_dict['foo'] = 'bar'
        resource_name = 'ppfa-test-runs'
        fields = ('id', 'date_created', 'status', 'ppfa_test', 'ppfa_test_assertions', )
        
    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.date_created = attrs.get('date_created', instance.date_created)
            return instance

        # Create new instance
        return PpfaTestRun(**attrs)

class PpfaTestAssertionSerializer(serializers.ModelSerializer):
    
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    subject = serializers.CharField(required=False,
                                  max_length=100)
    verb = serializers.CharField(required=False,
                                  max_length=100)  
    object = serializers.CharField(required=False,
                                  max_length=100)  
    status = serializers.BooleanField(required=False)  
    ppfa_test_run = serializers.PrimaryKeyRelatedField(read_only=True)
    ppfa_test = serializers.PrimaryKeyRelatedField(read_only=True)
        
    class Meta:
        model = PpfaTestAssertion
        #meta_dict = dict()
        #meta_dict['foo'] = 'bar'
        resource_name = 'ppfa-test-assertions'
        fields = ('id', 'subject', 'verb', 'object', 'status', 'ppfa_test_run', 'ppfa_test', )
        
    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.subject = attrs.get('subject', instance.subject)
            instance.verb = attrs.get('verb', instance.verb)
            instance.object = attrs.get('object', instance.object)
            return instance

        # Create new instance
        return PpfaTestAssertion(**attrs)
        

class PpfaTestStepSerializer(serializers.ModelSerializer):
    
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    subject = serializers.CharField(required=False,
                                  max_length=100)
    verb = serializers.CharField(required=False,
                                  max_length=100)  
    object = serializers.CharField(required=False,
                                  max_length=100)  
    ppfa_test = serializers.PrimaryKeyRelatedField(read_only=True)
        
    class Meta:
        model = PpfaTestStep
        #meta_dict = dict()
        #meta_dict['foo'] = 'bar'
        resource_name = 'ppfa-test-steps'
        fields = ('id', 'subject', 'verb', 'object', 'ppfa_test', )
        
    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.subject = attrs.get('subject', instance.subject)
            instance.verb = attrs.get('verb', instance.verb)
            instance.object = attrs.get('object', instance.object)
            return instance

        # Create new instance
        return PpfaTestStep(**attrs)

        
class PpfaTestStepTypeSerializer(serializers.ModelSerializer):
    
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(required=False,
                                  max_length=255)
        
    class Meta:
        model = PpfaTestStepType
        #meta_dict = dict()
        #meta_dict['foo'] = 'bar'
        resource_name = 'ppfaTestStepTypes'
        fields = ('id', 'name', )
        
    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.subject = attrs.get('name', instance.name)
            return instance

        # Create new instance
        return PpfaTestStep(**attrs)
                