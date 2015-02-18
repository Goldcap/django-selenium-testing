# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PpfaTest'
        db.create_table(u'selenium_tests_ppfatest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_run', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'selenium_tests', ['PpfaTest'])

        # Adding model 'PpfaTestRun'
        db.create_table(u'selenium_tests_ppfatestrun', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ppfa_test', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ppfa_test_runs', to=orm['selenium_tests.PpfaTest'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'selenium_tests', ['PpfaTestRun'])

        # Adding model 'PpfaTestAssertion'
        db.create_table(u'selenium_tests_ppfatestassertion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('verb', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('object', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ppfa_test_run', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selenium_tests.PpfaTestRun'])),
            ('ppfa_test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selenium_tests.PpfaTest'])),
        ))
        db.send_create_signal(u'selenium_tests', ['PpfaTestAssertion'])


    def backwards(self, orm):
        # Deleting model 'PpfaTest'
        db.delete_table(u'selenium_tests_ppfatest')

        # Deleting model 'PpfaTestRun'
        db.delete_table(u'selenium_tests_ppfatestrun')

        # Deleting model 'PpfaTestAssertion'
        db.delete_table(u'selenium_tests_ppfatestassertion')


    models = {
        u'selenium_tests.ppfatest': {
            'Meta': {'object_name': 'PpfaTest'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_run': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'selenium_tests.ppfatestassertion': {
            'Meta': {'object_name': 'PpfaTestAssertion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ppfa_test': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['selenium_tests.PpfaTest']"}),
            'ppfa_test_run': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['selenium_tests.PpfaTestRun']"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'verb': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'selenium_tests.ppfatestrun': {
            'Meta': {'object_name': 'PpfaTestRun'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ppfa_test': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ppfa_test_runs'", 'to': u"orm['selenium_tests.PpfaTest']"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['selenium_tests']