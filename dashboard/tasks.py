from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

import dateutil.parser
from datetime import timezone, datetime
from .models import *
import ast, thingspeak, requests

## Global Variable ###
powerAC = 2.1   #in kW, an estimated value with nothing to back this up. To be changed when an accurate figure is obtained.
powerCom = 0.1   #in kW per user per desktop+monitor, results approximated from the previous phase of study
powerLight = 0.028   #in kW per fluorescent tube
numLights = 25*2   #approx number of fluorescent tubes per shared space
billPerkWh = 0.21   #in terms of singapore dollars
tempThres = 25.0   #threshold for which below that means AC is on.
counterDays_Yr = 0  #count the number of days that have passed in this year

light_duration = 0
nobodyDuration = 0
light_duration3 = 0
nobodyDuration3 = 0
light_duration4 = 0
nobodyDuration4 = 0

# Initializing new variables used within function #
userMins = 0
comp_day = 0
light_duration_Yr = 0
nobodyDuration_Yr = 0
totallight_Yr = 0
totalac_Yr = 0
totalcomp_Yr = 0
totalkWh_Yr = 0
totalBill_Yr = 0
estlight_duration_Yr = 0
estnobodyDuration_Yr = 0
esttotallight_Yr = 0
esttotalac_Yr = 0
esttotalcomp_Yr = 0
esttotalkWh_Yr = 0
esttotalBill_Yr = 0
ac_day = 0


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

		#Get data from LBAsense
	r = requests.get("https://api.sap.lbasense.com/CurrentSAPValuePerRegion", params = {'user':'idcproject','pass':'idcproject','siteId':'375'})
	for data in r.json()['sapInformation']:
		if data['regionID'] == 1:
			logger.info('trying numvisitors')
	# 		logger.info('trying numvisitors')
			visLvl1 = max(0,int(data['numVisitors']) - 2)	
	# 		logger.info('success num visitors')
		elif data['regionID'] == 2:
			visLvl3 = max(0,int(data['numVisitors']) - 4)
			
		elif data['regionID'] == 3:
			visLvl4 = max(0,int(data['numVisitors']) - 2)
			
	currentTime = get_current_time()
	currentDateComparison = currentTime.strftime("%B %d %Y")
	logger.info('get current time: %s' %(str(currentTime)))

	current_year = currentTime.year
	counterDays_Yr = len(Level1_Stats.objects.filter(datetime__year=current_year).extra(select={'date':'DATE(datetime)'}).values('date').distinct())

	global light_duration
	global light_duration3
	global light_duration4
	global nobodyDuration
	global nobodyDuration3
	global nobodyDuration4

	global userMins
	global comp_day
	global light_duration_Yr
	global nobodyDuration_Yr
	global totallight_Yr
	global totalac_Yr
	global totalcomp_Yr
	global totalkWh_Yr
	global totalBill_Yr
	global estlight_duration_Yr
	global estnobodyDuration_Yr
	global esttotallight_Yr
	global esttotalac_Yr
	global esttotalcomp_Yr
	global esttotalkWh_Yr
	global esttotalBill_Yr
	global ac_day


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

			############## Addition 1 #####################
			### Total Electricity per Day ###
			light_day = light_duration + nobodyDuration
			totalkWh_day = (light_day*numLights*powerLight + ac_day*powerAC + comp_day*powerCom) * 24 #multiplied by 24hours to give num of kWh
			totalBill_day = totalkWh_day*billPerkWh



			entry = ChartLvl1_DayNew(date=daTi, light_duration=light_duration, nobody_present=nobodyDuration, light_day=light_day, comp_day=comp_day, ac_day=ac_day, totalkWh_day=totalkWh_day, totalBill_day=totalBill_day)
			entry.save()
			
			#reset#
			light_duration = 0
			nobodyDuration = 0 
			ac_day = 0
			comp_day = 0

			#edit: seems all these variables are local, so they wont carry over
			# if currentTime.strftime("%B %d %Y") == "January 01 2017" or currentTime.strftime("%B %d %Y, %H:%M") == "January 01 2018" or currentTime.strftime("%B %d %Y, %H:%M") == "January 01 2019, 00:01":
			# 	counterDays_Yr = 0   #reset counter

			# 	#local variables will not be carried over minute to minute so no need to reset
			# 	annualCO2 = 0
			# 	roundSg = 0
			# 	numTree2Plant = 0
			# 	numTreeinYr = 0
			################ End of Addition 1 #####################

			
		else:

			############# Addition 2 ###################
			#computer duration * num users#
			userMins = visLvl1 * (1/(24*60))
			comp_day = comp_day + userMins

			#ac duration#
			#either sat or sun respectively
			if currentTime.strftime("%w") == "6" or currentTime.strftime("%w") == "0":

				logger.info("addtion2 ac duration")
				if temp <= tempThres or temp2 <= tempThres:
					acOn = 1/(24*60)
				else:
					acOn = 0
				ac_day = ac_day + acOn
			else:
				acOn = 1/(24*60) #edit: acOn needs to be defined no matter what for chartlvl1_min table entry
				ac_day = (11*60)/(24*60)  #AHU always on for 11 hours from mon to fri

			############ End of Addition 2 ###################

						#light duration#
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

			
			# ######## Addition 3 ####################
			
			light_day = light_duration + nobodyDuration
			totalkWh_day = (light_day*numLights*powerLight  + ac_day*powerAC + comp_day*powerCom) * 24 #multiplied by 24hours to give num of kWh
			totalBill_day = totalkWh_day*billPerkWh
			#append acOn & userMins                                   (both contains instantaneous data)     into minute table
			#append ac_day & comp_day & totalkWh_day & totalBill_day  (all contain cumulative addition data) into minute table
			entry = ChartLvl1_Min(date=daTi, acOn=acOn, userMins=userMins, ac_day=ac_day, comp_day=comp_day, totalkWh_day=totalkWh_day, totalBill_day=totalBill_day)
			entry.save()
			#any need for this minute table? like to display the most updated electricity consumption/bill today as of current time

			light_duration_Yr = light_duration_Yr + present
			nobodyDuration_Yr = nobodyDuration_Yr + absent
			totallight_Yr = light_duration_Yr + nobodyDuration_Yr
			totalac_Yr = totalac_Yr + ac_day
			totalcomp_Yr = totalcomp_Yr + comp_day
			totalkWh_Yr = totalkWh_Yr + totalkWh_day
			totalBill_Yr = totalBill_Yr + totalBill_day

			#for display of informational statistics on approx yearly consumption
			estlight_duration_Yr = light_duration_Yr * 365/counterDays_Yr
			estnobodyDuration_Yr = nobodyDuration_Yr * 365/counterDays_Yr
			esttotallight_Yr = estlight_duration_Yr + estnobodyDuration_Yr
			esttotalac_Yr = totalac_Yr * 365/counterDays_Yr
			esttotalcomp_Yr = totalcomp_Yr * 365/counterDays_Yr
			esttotalkWh_Yr = totalkWh_Yr * 365/counterDays_Yr
			esttotalBill_Yr = totalBill_Yr * 365/counterDays_Yr

			# kg of CO2 Emissions
			annualCO2 = esttotalkWh_Yr * 0.5443104
			# Num of round trips around Sg: equivalence of CO2 emissions
			roundSg = (annualCO2 / 0.187)/140
			# Num of trees to plant to offset amt of CO2
			numTree2Plant = (annualCO2 / 907.185)*5
			# Num of mature trees to offset amt of CO2 within a year
			numTreeinYr = (annualCO2 / 22)

			entry = InfoL1(date=daTi, annualCO2=annualCO2, roundSg=roundSg, numTree2Plant=numTree2Plant, tnumTreeinYr=numTreeinYr)
			entry.save()

			
			
			entry = ChartLvl1_Yr(date=daTi, light_duration_Yr=light_duration_Yr, nobodyDuration_Yr=nobodyDuration_Yr, totallight_Yr=totallight_Yr, totalac_Yr=totalac_Yr, totalcomp_Yr=totalcomp_Yr, totalkWh_Yr=totalkWh_Yr, totalBill_Yr=totalBill_Yr, estlight_duration_Yr=estlight_duration_Yr, estnobodyDuration_Yr=estnobodyDuration_Yr, esttotallight_Yr=esttotallight_Yr, esttotalac_Yr=esttotalac_Yr, esttotalcomp_Yr=esttotalcomp_Yr, esttotalkWh_Yr=esttotalkWh_Yr, esttotalBill_Yr=esttotalBill_Yr)
			entry.save()

			logger.info("chart year saved")
			# ######### End of Addition 3 ####################

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


