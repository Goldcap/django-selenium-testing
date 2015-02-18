# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PpfaTestStepType'
        db.create_table(u'selenium_tests_ppfateststeptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'selenium_tests', ['PpfaTestStepType'])


    def backwards(self, orm):
        # Deleting model 'PpfaTestStepType'
        db.delete_table(u'selenium_tests_ppfateststeptype')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        },
        u'selenium_tests.ppfateststep': {
            'Meta': {'object_name': 'PpfaTestStep'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ppfa_test': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ppfa_test_steps'", 'to': u"orm['selenium_tests.PpfaTest']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'verb': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'selenium_tests.ppfateststeptype': {
            'Meta': {'object_name': 'PpfaTestStepType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'selenium_tests.profile': {
            'Approved': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'DateSubmitted': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 3, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'FirstName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'LastName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['selenium_tests']