# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Removing unique constraint on 'TimeseriesValuesAndFlags', fields ['datetime']
        #db.delete_unique(u'timeseriesvaluesandflags', ['datetime'])

        # Adding model 'TimeSeriesCache'
        db.create_table('lizard_fewsnorm_timeseriescache', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geolocationcache', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_fewsnorm.GeoLocationCache'])),
            ('parametercache', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_fewsnorm.ParameterCache'])),
            ('modulecache', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_fewsnorm.ModuleCache'])),
            ('timestepcache', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_fewsnorm.TimeStepCache'])),
        ))
        db.send_create_signal('lizard_fewsnorm', ['TimeSeriesCache'])

        # Adding model 'TimeStepCache'
        db.create_table('lizard_fewsnorm_timestepcache', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ident', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('lizard_fewsnorm', ['TimeStepCache'])

        # Removing M2M table for field parameter on 'GeoLocationCache'
        db.delete_table('lizard_fewsnorm_geolocationcache_parameter')

        # Removing M2M table for field module on 'GeoLocationCache'
        db.delete_table('lizard_fewsnorm_geolocationcache_module')


    def backwards(self, orm):

        # Deleting model 'TimeSeriesCache'
        db.delete_table('lizard_fewsnorm_timeseriescache')

        # Deleting model 'TimeStepCache'
        db.delete_table('lizard_fewsnorm_timestepcache')

        # Adding M2M table for field parameter on 'GeoLocationCache'
        db.create_table('lizard_fewsnorm_geolocationcache_parameter', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('geolocationcache', models.ForeignKey(orm['lizard_fewsnorm.geolocationcache'], null=False)),
            ('parametercache', models.ForeignKey(orm['lizard_fewsnorm.parametercache'], null=False))
        ))
        db.create_unique('lizard_fewsnorm_geolocationcache_parameter', ['geolocationcache_id', 'parametercache_id'])

        # Adding M2M table for field module on 'GeoLocationCache'
        db.create_table('lizard_fewsnorm_geolocationcache_module', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('geolocationcache', models.ForeignKey(orm['lizard_fewsnorm.geolocationcache'], null=False)),
            ('modulecache', models.ForeignKey(orm['lizard_fewsnorm.modulecache'], null=False))
        ))
        db.create_unique('lizard_fewsnorm_geolocationcache_module', ['geolocationcache_id', 'modulecache_id'])

        # Adding unique constraint on 'TimeseriesValuesAndFlags', fields ['datetime']
        #db.create_unique(u'timeseriesvaluesandflags', ['datetime'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lizard_fewsnorm.aggregationperiods': {
            'Meta': {'object_name': 'AggregationPeriods', 'db_table': "u'aggregationperiods'", 'managed': 'False'},
            'aggregationperiodkey': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'aggregationperiodkey'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'lizard_fewsnorm.fewsnormsource': {
            'Meta': {'object_name': 'FewsNormSource'},
            'database_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'lizard_fewsnorm.geolocationcache': {
            'Meta': {'object_name': 'GeoLocationCache', '_ormbases': ['lizard_geo.GeoObject']},
            'fews_norm_source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.FewsNormSource']"}),
            'geoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lizard_geo.GeoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'module': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lizard_fewsnorm.ModuleCache']", 'null': 'True', 'through': "orm['lizard_fewsnorm.TimeSeriesCache']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parameter': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lizard_fewsnorm.ParameterCache']", 'null': 'True', 'through': "orm['lizard_fewsnorm.TimeSeriesCache']", 'blank': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'timestep': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lizard_fewsnorm.TimeStepCache']", 'null': 'True', 'through': "orm['lizard_fewsnorm.TimeSeriesCache']", 'blank': 'True'}),
            'tooltip': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'lizard_fewsnorm.locations': {
            'Meta': {'object_name': 'Locations', 'db_table': "u'locations'", 'managed': 'False'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'attributea': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'attributeb': ('django.db.models.fields.FloatField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'locationkey': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'locationkey'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parentlocationid': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'relationalocationid': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'relationblocationid': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tooltip': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'visibilityendtime': ('django.db.models.fields.DateTimeField', [], {}),
            'visibilitystarttime': ('django.db.models.fields.DateTimeField', [], {}),
            'x': ('django.db.models.fields.FloatField', [], {}),
            'y': ('django.db.models.fields.FloatField', [], {}),
            'z': ('django.db.models.fields.FloatField', [], {})
        },
        'lizard_fewsnorm.modulecache': {
            'Meta': {'object_name': 'ModuleCache'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'lizard_fewsnorm.moduleinstances': {
            'Meta': {'object_name': 'ModuleInstances', 'db_table': "u'moduleinstances'", 'managed': 'False'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'moduleinstancekey': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'moduleinstancekey'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'lizard_fewsnorm.parametercache': {
            'Meta': {'object_name': 'ParameterCache'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'lizard_fewsnorm.parametergroups': {
            'Meta': {'object_name': 'ParameterGroups', 'db_table': "u'parametergroups'", 'managed': 'False'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'displayunit': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'groupkey': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'groupkey'"}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parametertype': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'lizard_fewsnorm.parameters': {
            'Meta': {'object_name': 'Parameters', 'db_table': "u'parameters'", 'managed': 'False'},
            'attributea': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'attributeb': ('django.db.models.fields.FloatField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'groupkey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.ParameterGroups']", 'db_column': "'groupkey'"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parameterkey': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'parameterkey'"}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'valueresolution': ('django.db.models.fields.FloatField', [], {})
        },
        'lizard_fewsnorm.qualifiers': {
            'Meta': {'object_name': 'Qualifiers', 'db_table': "u'qualifiers'", 'managed': 'False'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'qualifierkey': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'qualifierkey'"})
        },
        'lizard_fewsnorm.qualifiersets': {
            'Meta': {'object_name': 'QualifierSets', 'db_table': "u'qualifiersets'", 'managed': 'False'},
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'qualifierkey1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'qualifierkey1'", 'db_column': "'qualifierkey1'", 'to': "orm['lizard_fewsnorm.Qualifiers']"}),
            'qualifierkey2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'qualifierkey2'", 'null': 'True', 'db_column': "'qualifierkey2'", 'to': "orm['lizard_fewsnorm.Qualifiers']"}),
            'qualifierkey3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'qualifierkey3'", 'null': 'True', 'db_column': "'qualifierkey3'", 'to': "orm['lizard_fewsnorm.Qualifiers']"}),
            'qualifierkey4': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'qualifierkey4'", 'null': 'True', 'db_column': "'qualifierkey4'", 'to': "orm['lizard_fewsnorm.Qualifiers']"}),
            'qualifiersetkey': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'qualifiersetkey'"})
        },
        'lizard_fewsnorm.timeseriescache': {
            'Meta': {'object_name': 'TimeSeriesCache'},
            'geolocationcache': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.GeoLocationCache']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modulecache': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.ModuleCache']"}),
            'parametercache': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.ParameterCache']"}),
            'timestepcache': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.TimeStepCache']"})
        },
        'lizard_fewsnorm.timeseriescomments': {
            'Meta': {'object_name': 'TimeseriesComments', 'db_table': "u'timeseriescomments'", 'managed': 'False'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'serieskey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.TimeseriesKeys']", 'null': 'True', 'primary_key': 'True', 'db_column': "'serieskey'"})
        },
        'lizard_fewsnorm.timeserieskeys': {
            'Meta': {'object_name': 'TimeseriesKeys', 'db_table': "u'timeserieskeys'", 'managed': 'False'},
            'aggregationperiodkey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.AggregationPeriods']", 'null': 'True', 'db_column': "'aggregationperiodkey'", 'blank': 'True'}),
            'locationkey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.Locations']", 'db_column': "'locationkey'"}),
            'moduleinstancekey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.ModuleInstances']", 'null': 'True', 'db_column': "'moduleinstancekey'", 'blank': 'True'}),
            'parameterkey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.Parameters']", 'db_column': "'parameterkey'"}),
            'qualifiersetkey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.QualifierSets']", 'null': 'True', 'db_column': "'qualifiersetkey'", 'blank': 'True'}),
            'serieskey': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'serieskey'"}),
            'timestepkey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.Timesteps']", 'null': 'True', 'db_column': "'timestepkey'", 'blank': 'True'})
        },
        'lizard_fewsnorm.timeseriesmanualeditshistory': {
            'Meta': {'object_name': 'TimeseriesManualEditsHistory', 'db_table': "u'timeseriesmanualeditshistory'", 'managed': 'False'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'editdatetime': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'flags': ('django.db.models.fields.IntegerField', [], {}),
            'scalarvalue': ('django.db.models.fields.FloatField', [], {}),
            'serieskey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.TimeseriesKeys']", 'primary_key': 'True', 'db_column': "'serieskey'"}),
            'userkey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.Users']", 'null': 'True', 'db_column': "'userkey'", 'blank': 'True'})
        },
        'lizard_fewsnorm.timeseriesvaluesandflags': {
            'Meta': {'object_name': 'TimeseriesValuesAndFlags', 'db_table': "u'timeseriesvaluesandflags'", 'managed': 'False'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'primary_key': True}),
            'flags': ('django.db.models.fields.IntegerField', [], {}),
            'scalarvalue': ('django.db.models.fields.FloatField', [], {}),
            'serieskey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_fewsnorm.TimeseriesKeys']", 'db_column': "'serieskey'"})
        },
        'lizard_fewsnorm.timestepcache': {
            'Meta': {'object_name': 'TimeStepCache'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'lizard_fewsnorm.timesteps': {
            'Meta': {'object_name': 'Timesteps', 'db_table': "u'timesteps'", 'managed': 'False'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'timestepkey': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'timestepkey'"})
        },
        'lizard_fewsnorm.users': {
            'Meta': {'object_name': 'Users', 'db_table': "u'users'", 'managed': 'False'},
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'userkey': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'userkey'"})
        },
        'lizard_geo.geoobject': {
            'Meta': {'object_name': 'GeoObject'},
            'geo_object_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_geo.GeoObjectGroup']"}),
            'geometry': ('django.contrib.gis.db.models.fields.GeometryField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        'lizard_geo.geoobjectgroup': {
            'Meta': {'object_name': 'GeoObjectGroup'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'source_log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lizard_fewsnorm']
