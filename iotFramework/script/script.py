import os
import sys
import json
import ast
import random
import time
import uuid
from urlparse import parse_qs, urlparse

if(os.path.isfile('last_record.txt') ):
	f=open('last_record.txt','r')
	var=f.read().split(',')
	last_record=var[0]
	counter=int(var[1])
	numberofRecords=int(var[2])
	f.close()
else:
	last_record=1
	counter=0

print type(counter)
print counter
count=0
#Creating Payload
pdata={}
payload={}
sensorName="OBD-II"
sensorID=str(uuid.uuid4())
sensorType="Analog"
sensorTimeStamp=int(time.time())
payload['DeviceName']=sensorName
payload['DeviceID']=sensorID
payload['DeviceType']=sensorType
payload['DeviceTimeStamp']=sensorTimeStamp

with open('webhook_output.json') as data_file:
	data = json.load(data_file)
	#last_record=data['last_cursor']

	extract_data=data['items']
	for row in extract_data[counter:]:

		var="/?"
		var=var+row['query']

		print "-\n"
		dat=parse_qs(urlparse(var).query, keep_blank_values=True)
		payload['unique_id']=str(uuid.uuid4())
		payload['session']=dat['session'][0]
		payload['email']=dat['eml'][0]
		payload['id']=dat['id'][0]
		payload['time']=dat['time'][0]
		if 'kff1005' not in dat:
			count=count+1
			continue;
		payload['Longitude']=dat['kff1005'][0]
		payload['Latitude']=dat['kff1006'][0]
		payload['GPSSpeed']=dat['kff1001'][0]
		payload['kff1007']=dat['kff1007'][0]
		payload['Acceleration']=dat['kff1223'][0]
		payload['Costpermile/km']=dat['kff126d'][0]
		payload['CO2ing/km']=dat['kff1258'][0]
		payload['Distancetoempty']=dat['kff126a'][0]
		payload['k4']=dat['k4'][0]
		payload['kc']=dat['kc'][0]
		pdata['DevicePulse']=payload

		print json.dumps(pdata)
		CurlString=""
		os.system(CurlString)
		#time.sleep(5)

	counter=counter+int(numberofRecords)
	fo=open("last_record.txt","w")
	fo.write(str(last_record)+","+str(counter)+","+str(numberofRecords))
	fo.close()

print "\n",count,"Done"
