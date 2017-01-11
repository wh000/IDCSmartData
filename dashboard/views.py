from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import *
from chartit import DataPool, Chart
from django.utils.timezone import localtime

locations = ['idc1', 'mpn1', 'gutenberg', 'stevejobs', 'buckminster']
# Create your views here.
def home(request, location):
	context = {}
	temp_data = DataPool(
		series=
			[{'options':{
				'source': Buckminster1.objects.all()
				},
			'terms' : ['temp', 'time_added']

			}]
		)

	cht = Chart(
		datasource=temp_data,
		series_options=[
			{'options':{
				'type':'line',
				'stacking':False},
			 'terms':{'time_added':['temp',]}}
			],
		chart_options={
			'title':{'text':'Temperature Distribution of IDC1'},
			'xAxis':{
				'title':{'text': 'Date'},
				'step':100, 
				}
			},
		x_sortf_mapf_mts=(None,lambda i: i.date(),False)
		)
	
	context['temp_chart']= cht
	return render(request, 'dashboard/home.html', context)


def location_info(request, location):
	if location not in locations:
		raise Http404("Sorry, location does not exist!")

	if location == 'idc1':
		source1 = IDC1.objects.all()
	elif location == 'mpn1':
		source1 = MPN1.objects.all()
	elif location == 'stevejobs':
		source1 = SteveJobs1.objects.all()
		source2 = SteveJobs2.objects.all()
	elif location == 'gutenberg':
		source1 = Gutenberg1.objects.all()
		source2 = Gutenberg2.objects.all()
	elif location == 'buckminster':
		source1 = Buckminster1.objects.all()
		source2 = Buckminster2.objects.all()


	context = {}
	charts = []
	#Making the charts from django query set
	#Source 1:

	#Temperature:
	temp_data = DataPool(
		series=
			[{'options':{
				'source': source1
				},
			'terms' : ['temp', 'time_added']

			}]
		)

	temp_cht = Chart(
		datasource=temp_data,
		series_options=[
			{'options':{
				'type':'line',
				'stacking':False},
			 'terms':{'time_added':['temp',]}}
			],
		chart_options={
			'title':{'text':'Temperature Distribution of %s sensor' %(location.upper())},
			'xAxis':{
				'title':{'text': 'Date'},
				'step':100, 
				}
			},
		x_sortf_mapf_mts=(None,lambda i: i.date(),False)
		)

	#Lux
	lux_data = DataPool(
		series=
			[{'options':{
				'source': source1
				},
			'terms' : ['lux', 'time_added']

			}]
		)

	#Lux Chart
	lux_cht = Chart(
		datasource=lux_data,
		series_options=[
			{'options':{
				'type':'line',
				'stacking':False},
			 'terms':{'time_added':['lux',]}}
			],
		chart_options={
			'title':{'text':'Lux Measurements of %s sensor' %(location.upper())},
			'xAxis':{
				'title':{'text': 'Date'},
				'step':100, 
				}
			},
		x_sortf_mapf_mts=(None,lambda i: i.date(),False)
		)

	#Humidity
	hum_data = DataPool(
		series=
			[{'options':{
				'source': source1
				},
			'terms' : ['rel_humidity', 'time_added']

			}]
		)

	#Humidity Chart
	hum_cht = Chart(
		datasource=hum_data,
		series_options=[
			{'options':{
				'type':'line',
				'stacking':False},
			 'terms':{'time_added':['rel_humidity',]}}
			],
		chart_options={
			'title':{'text':'Humidity Measurements of %s sensor' %(location.upper())},
			'xAxis':{
				'title':{'text': 'Date'},
				'step':100, 
				}
			},
		x_sortf_mapf_mts=(None,lambda i: i.date(),False)
		)

	#Add the charts to the context to be sent to the html
	charts.append(temp_cht)
	charts.append(lux_cht)
	charts.append(hum_cht)

	#If the location has a second set of sensors
	if 'source2' in locals():
		temp_data2 = DataPool(
		series=
			[{'options':{
				'source': source2
				},
			'terms' : ['temp', 'time_added']

			}]
		)

		temp_cht2 = Chart(
			datasource=temp_data2,
			series_options=[
				{'options':{
					'type':'line',
					'stacking':False},
				 'terms':{'time_added':['temp',]}}
				],
			chart_options={
				'title':{'text':'Temperature Distribution of %s 2 sensor' %(location.upper())},
				'xAxis':{
					'title':{'text': 'Date'},
					'step':100, 
					}
				},
			x_sortf_mapf_mts=(None,lambda i: i.date(),False)
			)

		#Lux
		lux_data2 = DataPool(
			series=
				[{'options':{
					'source': source2
					},
				'terms' : ['lux', 'time_added']

				}]
			)

		#Lux Chart
		lux_cht2 = Chart(
			datasource=lux_data2,
			series_options=[
				{'options':{
					'type':'line',
					'stacking':False},
				 'terms':{'time_added':['lux',]}}
				],
			chart_options={
				'title':{'text':'Lux Measurements of %s 2 sensor' %(location.upper())},
				'xAxis':{
					'title':{'text': 'Date'},
					'step':100, 
					}
				},
			x_sortf_mapf_mts=(None,lambda i: i.date(),False)
			)

		#Humidity
		hum_data2 = DataPool(
			series=
				[{'options':{
					'source': source2
					},
				'terms' : ['rel_humidity', 'time_added']

				}]
			)

		#Humidity Chart
		hum_cht2 = Chart(
			datasource=hum_data2,
			series_options=[
				{'options':{
					'type':'line',
					'stacking':False},
				 'terms':{'time_added':['rel_humidity',]}}
				],
			chart_options={
				'title':{'text':'Humidity Measurements of %s 2 sensor' %(location.upper())},
				'xAxis':{
					'title':{'text': 'Date'},
					'step':100, 
					}
				},
			x_sortf_mapf_mts=(None,lambda i: i.date(),False)
			)

		charts.append(temp_cht2)
		charts.append(lux_cht2)
		charts.append(hum_cht2)
		context['second_sensor'] = 'yes'

	context['charts'] = charts

	print (context)
	return render(request, 'dashboard/location.html', context)