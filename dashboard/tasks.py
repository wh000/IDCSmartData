from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *
import ast, thingspeak, requests

# @shared_tasks
# ch = thingspeak.Channel(119590)	
# latest_entry = ast.literal_eval(ch.get({'results':1}))
# temp = latest_entry['feeds'][0]['field1']
# lux = latest_entry['feeds'][0]['field2']
# print (lux)
# humidity = latest_entry['feeds'][0]['field3']
# context['mpn1']={'temp': temp, 'lux': lux, 'humidity': humidity}
# entry = IDCData(temp=temp, lux=lux, rel_humidity=humidity)
# entry.save()

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

# @periodic_task(run_every=crontab(hour=7, minute=30, day_of_week="mon"))
# def every_monday_morning():
#     print("This is run every Monday morning at 7:30")

@periodic_task(run_every=(crontab(minute='*/2')), name="some_task", ignore_result=True)
def some_task():
	logger.info('trying to get data')
	#MPN1 119590
	ch = thingspeak.Channel(119590)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))
	temp = latest_entry['feeds'][0]['field1']
	lux = latest_entry['feeds'][0]['field2']
	humidity = latest_entry['feeds'][0]['field3']
	entry = MPN1(temp=temp, lux=lux, rel_humidity=humidity)
	entry.save()

	#IDC1 108723
	ch = thingspeak.Channel(108723)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))
	temp = latest_entry['feeds'][0]['field1']
	lux = latest_entry['feeds'][0]['field2']
	humidity = latest_entry['feeds'][0]['field3']
	entry = IDC1(temp=temp, lux=lux, rel_humidity=humidity)
	entry.save()

	#Gutenberg1 124372
	ch = thingspeak.Channel(124372)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))
	temp = latest_entry['feeds'][0]['field1']
	lux = latest_entry['feeds'][0]['field2']
	humidity = latest_entry['feeds'][0]['field3']
	entry = Gutenberg1(temp=temp, lux=lux, rel_humidity=humidity)
	entry.save()

	#Gutenberg2 124405
	ch = thingspeak.Channel(124405)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))
	temp = latest_entry['feeds'][0]['field1']
	lux = latest_entry['feeds'][0]['field2']
	humidity = latest_entry['feeds'][0]['field3']
	entry = Gutenberg2(temp=temp, lux=lux, rel_humidity=humidity)
	entry.save()

	#Buckminster1 124408
	ch = thingspeak.Channel(124408)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))
	temp = latest_entry['feeds'][0]['field1']
	lux = latest_entry['feeds'][0]['field2']
	humidity = latest_entry['feeds'][0]['field3']
	entry = Buckminster1(temp=temp, lux=lux, rel_humidity=humidity)
	entry.save()

	#Buckminster2 124409
	ch = thingspeak.Channel(124409)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))
	temp = latest_entry['feeds'][0]['field1']
	lux = latest_entry['feeds'][0]['field2']
	humidity = latest_entry['feeds'][0]['field3']
	entry = Buckminster2(temp=temp, lux=lux, rel_humidity=humidity)
	entry.save()

	#SJobs1 124406
	ch = thingspeak.Channel(124406)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))
	temp = latest_entry['feeds'][0]['field1']
	lux = latest_entry['feeds'][0]['field2']
	humidity = latest_entry['feeds'][0]['field3']
	entry = SteveJobs1(temp=temp, lux=lux, rel_humidity=humidity)
	entry.save()

	#SJobs2 124407
	ch = thingspeak.Channel(124407)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))
	temp = latest_entry['feeds'][0]['field1']
	lux = latest_entry['feeds'][0]['field2']
	humidity = latest_entry['feeds'][0]['field3']
	entry = SteveJobs2(temp=temp, lux=lux, rel_humidity=humidity)
	entry.save()



	#Get data from LBAsense
	r = requests.get("https://api.sap.lbasense.com/CurrentSAPValuePerRegion", params = {'user':'idcproject','pass':'idcproject','siteId':'375'})
	for data in r.json()['sapInformation']:
		if data['regionID'] == 1:
			logger.info('trying numvisitors')
	# 		logger.info('trying numvisitors')
			entry = Floor1(no_of_ppl=int(data['numVisitors']))
			entry.save()
	# 		logger.info('success num visitors')
		elif data['regionID'] == 2:
			entry = Floor3(no_of_ppl=int(data['numVisitors']))
			entry.save()
		elif data['regionID'] == 3:
			entry = Floor4(no_of_ppl=int(data['numVisitors']))
			entry.save()

	logger.info('numvisitors SUCCESS 2')


