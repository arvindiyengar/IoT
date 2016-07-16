import os
import sys
import json
import ast
import random
import time
import uuid



if(os.path.isfile('last_timestamp.txt') ):
	f=open('last_timestamp.txt','r')
	counter=int(f.read())
else:
	counter=0



sensorName="TemperatureSensor"
sensorID=str(uuid.uuid4())

sensorType="Analog"
sensorTimeStamp=int(time.time())



pdata={}
payload={}
payload['DeviceName']=sensorName
payload['DeviceID']=sensorID

payload['DeviceType']=sensorType
payload['DeviceTimeStamp']=sensorTimeStamp
pdata['DevicePulse']=payload

token="ZqLJiGL9nEBOyWp9RRdO7DMRAcze7u"
var_id="574d55f3762542542b566ac8"
start=0
end="1464687708955"
format_type="json"
page_size=10

CurlString='curl -X GET "http://things.ubidots.com/api/v1.6/variables/'+var_id+'/values/?token='+token+'&format='+format_type+'&start='+str(start)+'" > temp_output.json'

print CurlString

os.system(CurlString)

print "\n\n\n"
latest_ts=start

with open('temp_output.json') as data_file:    
	data = json.load(data_file)
	print len(data['results'])
	#counter=0
	while counter<len(data['results']):
		tempReading=data['results'][counter]['value']
		payload['temperature']=tempReading
		if(data['results'][counter]['timestamp']>latest_ts):
			latest_ts=data['results'][counter]['timestamp']
		CurlString=""
		os.system(CurlString)
		counter=counter+1
		print json.dumps(pdata)
		time.sleep(2)
	fo=open("last_timestamp.txt","w")
	fo.write(str(latest_ts))
	fo.close()
os.remove("temp_output.json")

print "Done"






