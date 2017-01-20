from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

import dateutil.parser
from datetime import timezone, datetime
from .models import *
import ast, thingspeak, requests

light_duration = 0
nobodyDuration = 0
light_duration3 = 0
nobodyDuration3 = 0
light_duration4 = 0
nobodyDuration4 = 0


## Convert Thingspeak datetime to Local GMT +8 ###
def get_current_time():
	currentTime = datetime.now()
	return currentTime
	
def utc_to_local(utc_dt):
	return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
	

logger = get_task_logger(__name__)
print('tasks.py')
# @periodic_task(run_every=crontab(hour=7, minute=30, day_of_week="mon"))
# def every_monday_morning():

#     print("This is run every Monday morning at 7:30")

@periodic_task(run_every=(crontab(minute='*/1')), name="some_task", ignore_result=True)
def some_task():
	logger.info('trying to get data')
	a =3
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
			visLvl1 = max(0,int(data['numVisitors']) - 2)
			entry = Floor1(no_of_ppl=int(data['numVisitors']))
			entry.save()
	# 		logger.info('success num visitors')
		elif data['regionID'] == 2:
			visLvl3 = max(0,int(data['numVisitors']) - 4)
			entry = Floor3(no_of_ppl=int(data['numVisitors']))
			entry.save()
		elif data['regionID'] == 3:
			visLvl4 = max(0,int(data['numVisitors']) - 2)
			entry = Floor4(no_of_ppl=int(data['numVisitors']))
			entry.save()

	
	currentTime = get_current_time()
	currentDateComparison = currentTime.strftime("%B %d %Y")
	logger.info('get current time: %s' %(str(currentTime)))

	global light_duration
	global light_duration3
	global light_duration4
	global nobodyDuration
	global nobodyDuration3
	global nobodyDuration4
	luxThres = 500   #set lux threshold here, above which means lights are on. below which means off.
		
		#############
		## TABLE 1 ##
		#############
						
	#MPN1 119590
	ch = thingspeak.Channel(119590)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))
	TSdateTime = latest_entry['feeds'][0]['created_at']
	datadatetime = utc_to_local(dateutil.parser.parse(TSdateTime))

	#IDC1 108723
	ch2 = thingspeak.Channel(108723)	
	latest_entry2 = ast.literal_eval(ch2.get({'results':1}))
	TSdateTime2 = latest_entry2['feeds'][0]['created_at']
	datadatetime2 = utc_to_local(dateutil.parser.parse(TSdateTime2))


	if datadatetime.strftime("%B %d %Y") == currentDateComparison and datadatetime2.strftime("%B %d %Y") == currentDateComparison:
		daTi = datadatetime
		temp = float(latest_entry['feeds'][0]['field1'])
		lux = float(latest_entry['feeds'][0]['field2'])
		humidity = float(latest_entry['feeds'][0]['field3'])
		temp2 = float(latest_entry2['feeds'][0]['field1'])
		lux2 = float(latest_entry2['feeds'][0]['field2'])
		humidity2 = float(latest_entry2['feeds'][0]['field3'])
		logger.info('datatime SUCCESS updated')

	
			
		if currentTime.strftime("%H:%M")  == "23:59": #reset counter
			# daily_light_duration = Level1_Stats.objects.filter(datetime=)
			logger.info('INSIDE RESET CLAUSE')
			entry = ChartLvl1_Day(date=daTi, light_duration=light_duration, nobody_present=nobodyDuration)   #save into a new table for plotting in graph
			entry.save()
			light_duration = 0
			nobodyDuration = 0          #means lights are on, but nobody present

		else:
			if visLvl1 > 0:                 #if number of visitors > 0
				absent = 0
				if lux>=luxThres and lux2>=luxThres:
					present = 1/(24*60)
				elif (lux>= luxThres and lux2<luxThres) or (lux<luxThres and lux2>=luxThres):
					present = 0.5/(24*60)
				else:
					present = 0
				light_duration = light_duration + present
				nobodyDuration = nobodyDuration + absent
			else:                           #if number of visitors = 0
				present = 0
				if lux>=luxThres and lux2>=luxThres:
					absent = 1/(24*60)
				elif lux>= luxThres and lux2<luxThres or lux<luxThres and lux2>=luxThres:
					absent = 0.5/(24*60)
				else:
					absent = 0
				light_duration = light_duration + present
				nobodyDuration = nobodyDuration + absent
	else:
		daTi = datadatetime
		temp = 0
		lux = 0
		humidity = 0
		temp2 = 0
		lux2 = 0
		humidity2 = 0
		light_duration = 0
		nobodyDuration = 0
		present = 0
		absent = 0
		logger.info('SUCCESS dati else clause')

	logger.info('SUCCESS 3')
	avg_lux = (lux + lux2)/2
	max_lux = max(lux,lux2)
	avg_temp = (temp + temp2)/2
	avg_humidity = (humidity + humidity2)/2
			
	entry = Level1_Stats(datetime=daTi, pax_count=visLvl1, lux_value1=lux, lux_value2=lux2, max_lux=max_lux, avg_lux=avg_lux, present=present, absent=absent, light_duration=light_duration, nobody_w_lights=nobodyDuration, temp1=temp, temp2=temp2, avg_temp=avg_temp, humidity1=humidity, humidity2=humidity2, avg_humidity=avg_humidity)
	entry.save()

	logger.info('SUCCESS 4')



		#############
		## TABLE 2 ## For level 3
		#############

	#Gutenberg1 124372
	ch = thingspeak.Channel(124372)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))
	TSdatetime = latest_entry['feeds'][0]['created_at']
	datadatetime = utc_to_local(dateutil.parser.parse(TSdateTime))

	#Gutenberg2 124405
	ch = thingspeak.Channel(124405)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))

	if datadatetime.strftime("%B %d %Y") == currentDateComparison and datadatetime2.strftime("%B %d %Y") == currentDateComparison:
		daTi = datadatetime
		temp = float(latest_entry['feeds'][0]['field1'])
		lux = float(latest_entry['feeds'][0]['field2'])
		humidity = float(latest_entry['feeds'][0]['field3'])
		temp2 = float(latest_entry2['feeds'][0]['field1'])
		lux2 = float(latest_entry2['feeds'][0]['field2'])
		humidity2 = float(latest_entry2['feeds'][0]['field3'])

		if currentTime.strftime("%H:%M")  == "23:59": #reset counter
			if 'light_duration3' in globals() and 'nobodyDuration3' in globals():
				entry = ChartLvl3_Day(date=daTi, light_duration=light_duration3, nobody_present=nobodyDuration3)   #save into a new table for plotting in graph
				entry.save()
				light_duration3 = 0
				nobodyDuration3 = 0
			else:
				light_duration3 = 0
				nobodyDuration3 = 0 #means lights are on, but nobody present
		else:
			if visLvl3 > 0:                 #if number of visitors > 0
				absent = 0
				if lux>=luxThres and lux2>=luxThres:
					present = 1/(24*60)
				elif lux>= luxThres and lux2<luxThres or lux<luxThres and lux2>=luxThres:
					present = 0.5/(24*60)
				else:
					present = 0
				light_duration3 = light_duration3 + present
				nobodyDuration3 = nobodyDuration3 + absent
			else:                           #if number of visitors = 0
				present = 0
				if lux>=luxThres and lux2>=luxThres:
					absent = 1/(24*60)
				elif lux>= luxThres and lux2<luxThres or lux<luxThres and lux2>=luxThres:
					absent = 0.5/(24*60)
				else:
					absent = 0
				light_duration3 = light_duration3 + present
				nobodyDuration3 = nobodyDuration3 + absent
	else:
		daTi = datadatetime
		temp = 0
		lux = 0
		humidity = 0
		temp2 = 0
		lux2 = 0
		humidity2 = 0
		light_duration3 = 0
		nobodyDuration3 = 0
		present = 0
		absent = 0

	avg_lux = (lux + lux2)/2
	max_lux = max(lux,lux2)
	avg_temp = (temp + temp2)/2
	avg_humidity = (humidity + humidity2)/2

	logger.info('lux 1: %f lux2: %f max_lux: %f' %(lux,lux2,max_lux))
	entry = Level3_Stats(datetime=daTi, pax_count=visLvl3, lux_value1=lux, lux_value2=lux2, max_lux=max_lux, avg_lux=avg_lux, present=present, absent=absent, light_duration=light_duration3, nobody_w_lights=nobodyDuration3, temp1=temp, temp2=temp2, avg_temp=avg_temp, humidity1=humidity, humidity2=humidity2, avg_humidity=avg_humidity)
	entry.save()

	logger.info('SUCCESS 5')



		#############
		## TABLE 3 ## For level 4
		#############
	
	#Buckminster1 124408
	ch = thingspeak.Channel(124408)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))
	TSdatetime = latest_entry['feeds'][0]['created_at']
	datadatetime = utc_to_local(dateutil.parser.parse(TSdateTime))

	#Buckminster2 124409
	ch = thingspeak.Channel(124409)	
	latest_entry = ast.literal_eval(ch.get({'results':1}))
	TSdatetime2 = latest_entry2['feeds'][0]['created_at']
	datadatetime2 = utc_to_local(dateutil.parser.parse(TSdateTime2))

	if datadatetime.strftime("%B %d %Y") == currentDateComparison and datadatetime2.strftime("%B %d %Y") == currentDateComparison:
		daTi = datadatetime
		temp = float(latest_entry['feeds'][0]['field1'])
		lux = float(latest_entry['feeds'][0]['field2'])
		humidity = float(latest_entry['feeds'][0]['field3'])
		temp2 = float(latest_entry2['feeds'][0]['field1'])
		lux2 = float(latest_entry2['feeds'][0]['field2'])
		humidity2 = float(latest_entry2['feeds'][0]['field3'])
		logger.info('Table 3 lvl 4')
		if currentTime.strftime("%H:%M")  == "23:59": #reset counter
			if 'light_duration4' in globals() and 'nobodyDuration4' in globals():
				entry = ChartLvl4_Day(date=daTi, light_duration=light_duration4, nobody_present=nobodyDuration4)   #save into a new table for plotting in graph
				entry.save()
				light_duration4 = 0
				nobodyDuration4 = 0
			else:
				light_duration4 = 0
				nobodyDuration4 = 0 #means lights are on, but nobody present
		else:
			if visLvl4 > 0:                 #if number of visitors > 0
				absent = 0
				if lux>=luxThres and lux2>=luxThres:
					present = 1/(24*60)
				elif lux>= luxThres and lux2<luxThres or lux<luxThres and lux2>=luxThres:
					present = 0.5/(24*60)
				else:
					present = 0
				light_duration4 = light_duration4 + present
				nobodyDuration4 = nobodyDuration4 + absent
			else:                           #if number of visitors = 0
				present = 0
				if lux>=luxThres and lux2>=luxThres:
					absent = 1/(24*60)
				elif lux>= luxThres and lux2<luxThres or lux<luxThres and lux2>=luxThres:
					absent = 0.5/(24*60)
				else:
					absent = 0
				light_duration4 = light_duration4 + present
				nobodyDuration4 = nobodyDuration4 + absent
	else:
		daTi = datadatetime
		temp = 0
		lux = 0
		humidity = 0
		temp2 = 0
		lux2 = 0
		humidity2 = 0
		light_duration4 = 0
		nobodyDuration4 = 0
		present = 0
		absent = 0

	avg_lux = (lux + lux2)/2
	max_lux = max(lux,lux2)
	avg_temp = (temp + temp2)/2
	avg_humidity = (humidity + humidity2)/2

	logger.info('SUCCESS 6')
	
					
	entry = Level4_Stats(datetime=daTi, pax_count=visLvl4, lux_value1=lux, lux_value2=lux2, max_lux=max_lux, avg_lux=avg_lux, present=present, absent=absent, light_duration=light_duration4, nobody_w_lights=nobodyDuration4, temp1=temp, temp2=temp2, avg_temp=avg_temp, humidity1=humidity, humidity2=humidity2, avg_humidity=avg_humidity)
	entry.save()        


