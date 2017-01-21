from django.db import models
from datetime import datetime

# Create your models here.

class ChartLvl1_DayNew(models.Model):
	date = models.DateTimeField()
	light_duration = models.FloatField()
	nobody_present = models.FloatField()
	light_day = models.FloatField()
	comp_day = models.FloatField()
	ac_day = models.FloatField()
	totalkWh_day = models.FloatField()
	totalBill_day = models.DecimalField(decimal_places=2, max_digits=8)
	class Meta:
		managed = True
		db_table = 'ChartL1_DayNew'


class ChartLvl1_Min(models.Model):
	date = models.DateTimeField()
	acOn = models.FloatField()
	userMins = models.FloatField()
	comp_day = models.FloatField()
	totalkWh_day = models.FloatField()
	ac_day = models.FloatField()
	totalkWh_day = models.FloatField()
	totalBill_day = models.DecimalField(decimal_places=2, max_digits=8)
	class Meta:
		managed = True
		db_table = 'ChartL1_Min'



class InfoL1(models.Model):
	date = models.DateTimeField()
	annualCO2 = models.IntegerField()
	roundSg = models.IntegerField()
	numTree2Plant = models.IntegerField()
	tnumTreeinYr = models.IntegerField()
	class Meta:
		managed = True
		db_table = 'InfoL1'


class ChartLvl1_Yr(models.Model):
	date = models.DateTimeField()
	light_duration_Yr = models.FloatField()
	nobodyDuration_Yr = models.FloatField()
	totallight_Yr = models.FloatField()
	totalac_Yr = models.FloatField()
	totalcomp_Yr = models.FloatField()
	totalkWh_Yr = models.FloatField()
	totalBill_Yr = models.DecimalField(decimal_places=2, max_digits=8)
	estlight_duration_Yr = models.DecimalField(decimal_places=2, max_digits=8)
	estnobodyDuration_Yr = models.DecimalField(decimal_places=2, max_digits=8)
	esttotallight_Yr = models.DecimalField(decimal_places=2, max_digits=8)
	esttotalac_Yr = models.DecimalField(decimal_places=2, max_digits=8)
	esttotalcomp_Yr = models.DecimalField(decimal_places=2, max_digits=8)
	esttotalkWh_Yr = models.DecimalField(decimal_places=2, max_digits=8)
	esttotalBill_Yr = models.DecimalField(decimal_places=2, max_digits=8)
	class Meta:
		managed = True
		db_table = 'ChartL1_Yr'



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

