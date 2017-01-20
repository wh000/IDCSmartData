from django.db import models
from datetime import datetime

# Create your models here.

class ChartLvl1_Day(models.Model):
	date = models.DateTimeField()
	light_duration = models.FloatField()
	nobody_present = models.FloatField()
	class Meta:
		managed = True
		db_table = 'ChartL1_Day'

class ChartLvl3_Day(models.Model):
	date = models.DateTimeField()
	light_duration = models.FloatField()
	nobody_present = models.FloatField()
	class Meta:
		managed = True
		db_table = 'ChartL3_Day'

class ChartLvl4_Day(models.Model):
	date = models.DateTimeField()
	light_duration = models.FloatField()
	nobody_present = models.FloatField()
	class Meta:
		managed = True
		db_table = 'ChartL4_Day'

class Level1_Stats(models.Model):
	datetime = models.DateTimeField()
	pax_count = models.IntegerField()
	lux_value1 = models.FloatField()
	lux_value2 = models.FloatField()
	max_lux = models.FloatField()
	avg_lux = models.FloatField()
	present = models.FloatField()
	absent = models.FloatField()
	light_duration = models.FloatField()
	nobody_w_lights = models.FloatField()
	temp1 = models.FloatField()
	temp2 = models.FloatField()
	avg_temp = models.FloatField()
	humidity1 = models.FloatField()
	humidity2 = models.FloatField()
	avg_humidity = models.FloatField()
	class Meta:
		managed = True
		db_table = 'L1_Stats'

class Level3_Stats(models.Model):
	datetime = models.DateTimeField()
	pax_count = models.IntegerField()
	lux_value1 = models.FloatField()
	lux_value2 = models.FloatField()
	max_lux = models.FloatField()
	avg_lux = models.FloatField()
	present = models.FloatField()
	absent = models.FloatField()
	light_duration = models.FloatField()
	nobody_w_lights = models.FloatField()
	temp1 = models.FloatField()
	temp2 = models.FloatField()
	avg_temp = models.FloatField()
	humidity1 = models.FloatField()
	humidity2 = models.FloatField()
	avg_humidity = models.FloatField()
	class Meta:
		managed = True
		db_table = 'L3_Stats'

class Level4_Stats(models.Model):
	datetime = models.DateTimeField()
	pax_count = models.IntegerField()
	lux_value1 = models.FloatField()
	lux_value2 = models.FloatField()
	max_lux = models.FloatField()
	avg_lux = models.FloatField()
	present = models.FloatField()
	absent = models.FloatField()
	light_duration = models.FloatField()
	nobody_w_lights = models.FloatField()
	temp1 = models.FloatField()
	temp2 = models.FloatField()
	avg_temp = models.FloatField()
	humidity1 = models.FloatField()
	humidity2 = models.FloatField()
	avg_humidity = models.FloatField()
	class Meta:
		managed = True
		db_table = 'L4_Stats'

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