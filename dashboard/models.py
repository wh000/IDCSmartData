from django.db import models
from datetime import datetime

# Create your models here.

class IDCData(models.Model):

	temp = models.FloatField()
	lux = models.FloatField()
	rel_humidity = models.FloatField()
	time_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.time_added) + ', temp: ' + temp

	class Meta:
		managed = True
		db_table = 'idcdata'

class MPN1(models.Model):

	temp = models.FloatField()
	lux = models.FloatField()
	rel_humidity = models.FloatField()
	time_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.time_added) + ', temp: ' + temp

	class Meta:
		managed = True
		db_table = 'mpn1'


class IDC1(models.Model):

	temp = models.FloatField()
	lux = models.FloatField()
	rel_humidity = models.FloatField()
	time_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.time_added) + ', temp: ' + temp

	class Meta:
		managed = True
		db_table = 'idc1'

class Gutenberg1(models.Model):

	temp = models.FloatField()
	lux = models.FloatField()
	rel_humidity = models.FloatField()
	time_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.time_added) + ', temp: ' + temp

	class Meta:
		managed = True
		db_table = 'gutenberg1'

class Gutenberg2(models.Model):

	temp = models.FloatField()
	lux = models.FloatField()
	rel_humidity = models.FloatField()
	time_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.time_added) + ', temp: ' + temp

	class Meta:
		managed = True
		db_table = 'gutenberg2'

class Buckminster1(models.Model):

	temp = models.FloatField()
	lux = models.FloatField()
	rel_humidity = models.FloatField()
	time_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.time_added) + ', temp: ' + temp

	class Meta:
		managed = True
		db_table = 'buckminster1'

class Buckminster2(models.Model):

	temp = models.FloatField()
	lux = models.FloatField()
	rel_humidity = models.FloatField()
	time_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.time_added) + ', temp: ' + temp

	class Meta:
		managed = True
		db_table = 'buckminster2'						

class SteveJobs1(models.Model):

	temp = models.FloatField()
	lux = models.FloatField()
	rel_humidity = models.FloatField()
	time_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.time_added) + ', temp: ' + temp

	class Meta:
		managed = True
		db_table = 'stevejobs1'

class SteveJobs2(models.Model):

	temp = models.FloatField()
	lux = models.FloatField()
	rel_humidity = models.FloatField()
	time_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.time_added) + ', temp: ' + temp

	class Meta:
		managed = True
		db_table = 'stevejobs2'

class Floor1(models.Model):

	time_added = models.DateTimeField(auto_now_add=True)
	no_of_ppl = models.IntegerField()

	def __unicode__(self):
		return str(self.time_added) + ', no_of_ppl: ' + no_of_ppl

	class Meta:
		managed = True
		db_table = 'floor1'

class Floor3(models.Model):

	time_added = models.DateTimeField(auto_now_add=True)
	no_of_ppl = models.IntegerField()

	def __unicode__(self):
		return str(self.time_added) + ', no_of_ppl: ' + no_of_ppl

	class Meta:
		managed = True
		db_table = 'floor3'

class Floor4(models.Model):

	time_added = models.DateTimeField(auto_now_add=True)
	no_of_ppl = models.IntegerField()

	def __unicode__(self):
		return str(self.time_added) + ', no_of_ppl: ' + no_of_ppl

	class Meta:
		managed = True
		db_table = 'floor4'