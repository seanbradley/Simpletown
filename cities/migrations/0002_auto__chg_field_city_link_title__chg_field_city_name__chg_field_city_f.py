# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'City.link_title'
        db.alter_column(u'cities_city', 'link_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'City.name'
        db.alter_column(u'cities_city', 'name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'City.fips_class'
        db.alter_column(u'cities_city', 'fips_class', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'City.url'
        db.alter_column(u'cities_city', 'url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'City.feature_id'
        db.alter_column(u'cities_city', 'feature_id', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'City.state_name'
        db.alter_column(u'cities_city', 'state_name', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # Changing field 'City.fips_county_cd'
        db.alter_column(u'cities_city', 'fips_county_cd', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'City.state_abbreviation'
        db.alter_column(u'cities_city', 'state_abbreviation', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'City.full_county_name'
        db.alter_column(u'cities_city', 'full_county_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'City.county_name'
        db.alter_column(u'cities_city', 'county_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'City.feat_class'
        db.alter_column(u'cities_city', 'feat_class', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'City.primary_latitude'
        db.alter_column(u'cities_city', 'primary_latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3))

        # Changing field 'City.primary_longitude'
        db.alter_column(u'cities_city', 'primary_longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3))

        # Changing field 'City.description'
        db.alter_column(u'cities_city', 'description', self.gf('django.db.models.fields.TextField')(max_length=250, null=True))

    def backwards(self, orm):

        # Changing field 'City.link_title'
        db.alter_column(u'cities_city', 'link_title', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'City.name'
        db.alter_column(u'cities_city', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'City.fips_class'
        db.alter_column(u'cities_city', 'fips_class', self.gf('django.db.models.fields.CharField')(default='', max_length=2))

        # Changing field 'City.url'
        db.alter_column(u'cities_city', 'url', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'City.feature_id'
        db.alter_column(u'cities_city', 'feature_id', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'City.state_name'
        db.alter_column(u'cities_city', 'state_name', self.gf('django.db.models.fields.CharField')(default='', max_length=25))

        # Changing field 'City.fips_county_cd'
        db.alter_column(u'cities_city', 'fips_county_cd', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'City.state_abbreviation'
        db.alter_column(u'cities_city', 'state_abbreviation', self.gf('django.db.models.fields.CharField')(default='', max_length=2))

        # Changing field 'City.full_county_name'
        db.alter_column(u'cities_city', 'full_county_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'City.county_name'
        db.alter_column(u'cities_city', 'county_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'City.feat_class'
        db.alter_column(u'cities_city', 'feat_class', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'City.primary_latitude'
        db.alter_column(u'cities_city', 'primary_latitude', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=3))

        # Changing field 'City.primary_longitude'
        db.alter_column(u'cities_city', 'primary_longitude', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=3))

        # Changing field 'City.description'
        db.alter_column(u'cities_city', 'description', self.gf('django.db.models.fields.TextField')(default='', max_length=250))

    models = {
        u'cities.city': {
            'Meta': {'object_name': 'City'},
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'feat_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'feature_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'fips_class': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'fips_county_cd': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'full_county_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'primary_latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'primary_longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'state_abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cities']