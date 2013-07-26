# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'cities_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('county_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=250, blank=True)),
            ('feat_class', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('feature_id', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('fips_class', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('fips_county_cd', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('full_county_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('link_title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('primary_latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3, blank=True)),
            ('primary_longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3, blank=True)),
            ('state_abbreviation', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('state_name', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
        ))
        db.send_create_signal(u'cities', ['City'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'cities_city')


    models = {
        u'cities.city': {
            'Meta': {'object_name': 'City'},
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            'feat_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'feature_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'fips_class': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'fips_county_cd': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'full_county_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'primary_latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'primary_longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'state_abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['cities']