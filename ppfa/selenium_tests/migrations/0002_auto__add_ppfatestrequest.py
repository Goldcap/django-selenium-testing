# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PpfaTestRequest'
        db.create_table(u'selenium_tests_ppfatestrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ppfa_test', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ppfa_test_queue_test', to=orm['selenium_tests.PpfaTest'])),
            ('request_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'selenium_tests', ['PpfaTestRequest'])


    def backwards(self, orm):
        # Deleting model 'PpfaTestRequest'
        db.delete_table(u'selenium_tests_ppfatestrequest')


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
            'ppfa_test': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ppfa_test_assertion_test'", 'to': u"orm['selenium_tests.PpfaTest']"}),
            'ppfa_test_run': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ppfa_test_assertion_run'", 'to': u"orm['selenium_tests.PpfaTestRun']"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'verb': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'selenium_tests.ppfatestrequest': {
            'Meta': {'object_name': 'PpfaTestRequest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ppfa_test': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ppfa_test_queue_test'", 'to': u"orm['selenium_tests.PpfaTest']"}),
            'request_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
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