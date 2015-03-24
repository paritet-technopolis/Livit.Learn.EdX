# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Scale'
        db.create_table('labster_scale', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('labster', ['Scale'])

        # Adding model 'Category'
        db.create_table('labster_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('labster', ['Category'])

        # Adding field 'Answer.difficulty'
        db.add_column('labster_answer', 'difficulty',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Problem.is_adaptive'
        db.add_column('labster_problem', 'is_adaptive',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Problem.answer_type'
        db.add_column('labster_problem', 'answer_type',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Problem.number_of_destractors'
        db.add_column('labster_problem', 'number_of_destractors',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Problem.content'
        db.add_column('labster_problem', 'content',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Problem.feedback'
        db.add_column('labster_problem', 'feedback',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Problem.time'
        db.add_column('labster_problem', 'time',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Problem.sd_time'
        db.add_column('labster_problem', 'sd_time',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Problem.discrimination'
        db.add_column('labster_problem', 'discrimination',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Problem.guessing'
        db.add_column('labster_problem', 'guessing',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Problem.image_url'
        db.add_column('labster_problem', 'image_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding M2M table for field scales on 'Problem'
        db.create_table('labster_problem_scales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('problem', models.ForeignKey(orm['labster.problem'], null=False)),
            ('scale', models.ForeignKey(orm['labster.scale'], null=False))
        ))
        db.create_unique('labster_problem_scales', ['problem_id', 'scale_id'])

        # Adding M2M table for field categories on 'Problem'
        db.create_table('labster_problem_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('problem', models.ForeignKey(orm['labster.problem'], null=False)),
            ('category', models.ForeignKey(orm['labster.category'], null=False))
        ))
        db.create_unique('labster_problem_categories', ['problem_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Scale'
        db.delete_table('labster_scale')

        # Deleting model 'Category'
        db.delete_table('labster_category')

        # Deleting field 'Answer.difficulty'
        db.delete_column('labster_answer', 'difficulty')

        # Deleting field 'Problem.is_adaptive'
        db.delete_column('labster_problem', 'is_adaptive')

        # Deleting field 'Problem.answer_type'
        db.delete_column('labster_problem', 'answer_type')

        # Deleting field 'Problem.number_of_destractors'
        db.delete_column('labster_problem', 'number_of_destractors')

        # Deleting field 'Problem.content'
        db.delete_column('labster_problem', 'content')

        # Deleting field 'Problem.feedback'
        db.delete_column('labster_problem', 'feedback')

        # Deleting field 'Problem.time'
        db.delete_column('labster_problem', 'time')

        # Deleting field 'Problem.sd_time'
        db.delete_column('labster_problem', 'sd_time')

        # Deleting field 'Problem.discrimination'
        db.delete_column('labster_problem', 'discrimination')

        # Deleting field 'Problem.guessing'
        db.delete_column('labster_problem', 'guessing')

        # Deleting field 'Problem.image_url'
        db.delete_column('labster_problem', 'image_url')

        # Removing M2M table for field scales on 'Problem'
        db.delete_table('labster_problem_scales')

        # Removing M2M table for field categories on 'Problem'
        db.delete_table('labster_problem_categories')


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
        'labster.answer': {
            'Meta': {'ordering': "('order', 'created_at')", 'unique_together': "(('problem', 'hashed_text'),)", 'object_name': 'Answer'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'difficulty': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hashed_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.Problem']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'labster.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'labster.deviceinfo': {
            'Meta': {'object_name': 'DeviceInfo'},
            'cores': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'device_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'fill_rate': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'frame_rate': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'gpu': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab_proxy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.LabProxy']"}),
            'machine_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'memory': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'misc': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'os': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'processor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'quality': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'ram': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'shader_level': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'labster.errorinfo': {
            'Meta': {'object_name': 'ErrorInfo'},
            'browser': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab_proxy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.LabProxy']"}),
            'message': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'os': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'user_agent': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'labster.lab': {
            'Meta': {'object_name': 'Lab'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'demo_course_id': ('xmodule_django.models.CourseKeyField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'engine_file': ('django.db.models.fields.CharField', [], {'default': "'labster.unity3d'", 'max_length': '128', 'blank': 'True'}),
            'engine_xml': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['labster.LanguageLab']", 'symmetrical': 'False'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'questions': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'quiz_block_file': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'quiz_block_last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'screenshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'screenshot_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '120', 'blank': 'True'}),
            'use_quiz_blocks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verified_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wiki_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '120', 'blank': 'True'})
        },
        'labster.labproxy': {
            'Meta': {'object_name': 'LabProxy'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.Lab']", 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'labster.labstercourselicense': {
            'Meta': {'unique_together': "(('user', 'course_id'),)", 'object_name': 'LabsterCourseLicense'},
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'labster.labsteruserlicense': {
            'Meta': {'unique_together': "(('course_id', 'email'),)", 'object_name': 'LabsterUserLicense'},
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'expired_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'labster.languagelab': {
            'Meta': {'object_name': 'LanguageLab'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'language_name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'labster.problem': {
            'Meta': {'ordering': "('order', 'created_at')", 'unique_together': "(('quiz_block', 'element_id'),)", 'object_name': 'Problem'},
            'answer_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['labster.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'correct_message': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'discrimination': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'element_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'feedback': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'guessing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hashed_sentence': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_adaptive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'max_attempts': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'no_score': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'number_of_destractors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quiz_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.QuizBlock']"}),
            'randomize_option_order': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'scales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['labster.Scale']", 'symmetrical': 'False', 'blank': 'True'}),
            'sd_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sentence': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wrong_message': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        'labster.problemproxy': {
            'Meta': {'object_name': 'ProblemProxy'},
            'correct_answer': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lab_proxy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.LabProxy']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.Problem']", 'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'question_text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'quiz_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'labster.quizblock': {
            'Meta': {'ordering': "('order', 'created_at')", 'unique_together': "(('lab', 'element_id'),)", 'object_name': 'QuizBlock'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'element_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.Lab']"}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'time_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'labster.scale': {
            'Meta': {'object_name': 'Scale'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'labster.token': {
            'Meta': {'object_name': 'Token'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'labster.unitylog': {
            'Meta': {'object_name': 'UnityLog'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab_proxy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.LabProxy']", 'null': 'True', 'blank': 'True'}),
            'log_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'request_method': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'default': "'INFO'", 'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'labster.useranswer': {
            'Meta': {'object_name': 'UserAnswer'},
            'answer_string': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'attempt_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'completion_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'correct_answer': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_correct': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_view_theory_clicked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab_proxy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.LabProxy']", 'null': 'True', 'blank': 'True'}),
            'play_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.Problem']", 'null': 'True', 'blank': 'True'}),
            'problem_proxy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.ProblemProxy']", 'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'quiz_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'labster.userattempt': {
            'Meta': {'object_name': 'UserAttempt'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab_proxy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.LabProxy']"}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'labster.usersave': {
            'Meta': {'unique_together': "(('lab_proxy', 'user'),)", 'object_name': 'UserSave'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab_proxy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labster.LabProxy']"}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'play_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'save_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['labster']