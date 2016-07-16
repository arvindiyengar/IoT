# -*- coding: utf-8 -*-
import json 
import os 
import sys
import csv
import random
import time

with open('data.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	counter =1
	data={}
	payload={}
	host='apigw-sbx.vmware.com'
	client_id="3ba0c801eec34bc09fa91bd55fac4593"
	client_secret="dbcb507d74894b68AD6804D4053C1282"
	

	
	for row in reader:
		data={}
		payload={}
		payload['DeviceName']="OBD-II Reader"
		payload['DeviceID']= row['DeviceID']
		payload['DeviceType']="OBD-II"
		payload['DeviceTimeStamp']=str(int(time.time()))
		payload['Longitude']= row['Longitude']
		payload['Latitude']= row['Latitude']
		payload['GPSTime']= row['GPSTime']
		payload['DeviceTime']= row['DeviceTime']
		payload['GPSSpeed']= row['GPSSpeed(Meters/second)']
		payload['HorizontalDilutionofPrecision']= row['HorizontalDilutionofPrecision']


		payload['Altitude']= row['Altitude']
		payload['Bearing']= row['Bearing']
		payload['G(x)']= row['G(x)']
		payload['G(y)']= row['G(y)']
		payload['G(z)']= row['G(z)']


		payload['G(calibrated)']= row['G(calibrated)']
		payload['AccelerationSensor']= row['AccelerationSensor(Total)(g)']
		
		payload['Costpermile/km']= row['Costpermile/km(Instant)(£/km)']
		payload['CO2ing/km']= row['CO2ing/km(Average)(g/km)']


		payload['Distancetoempty']= row['Distancetoempty(Estimated)(km)']
		payload['EngineLoad(%)']= row['EngineLoad(%)']
		payload['EngineRPM']= row['EngineRPM(rpm)']

		data['DevicePulse']=payload



		print json.dumps(data)
		#CurlString='curl -H "Content-Type:application/json" -X POST -d \''+json.dumps(data)+'\' "http://localhost:5000/request/update"'
		CurlString='curl -H "Content-Type:application/json" -X POST -d \''+json.dumps(data)+'\' "https://google.com"'
		os.system(CurlString)
		
		if(counter > 100):
			break
		#print(row['Device Time'], row['Device ID'])
		counter=counter+1

		time.sleep(10)

