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
	counter=var[1]
	f.close()
else:
	last_record=1
	counter=0


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

#Variables
var_id="7P8GSbnp"




CurlString='curl -X GET "http://api.webhookinbox.com/i/'+var_id+'/items/?order=created&since=id:'+str(last_record)+'" > temp_webhook_output.json'
print CurlString
os.system(CurlString)


fi=open("temp_webhook_output.json","r")
input_data=json.load(fi)
last_record=input_data['last_cursor']
numberofRecords=len(input_data['items'])
fo=open("webhook_output.json","r+")
input_data_output=json.load(fo)
input_data_output['items']=input_data_output['items']+input_data['items']
fo.seek(0,0)
fo.write(json.dumps(input_data_output))
fo.close()
fi.close()
os.remove("temp_webhook_output.json")


#Reading the file

with open('webhook_output.json') as data_file:
	data = json.load(data_file)
	#last_record=data['last_cursor']
	for row in data['items'][counter:]:

		var="/?"
		var=var+row['query']

		print "-\n"
		dat=parse_qs(urlparse(var).query, keep_blank_values=True)

		payload['session']=dat['session'][0]
		payload['email']=dat['eml'][0]
		payload['id']=dat['id'][0]
		payload['time']=dat['time'][0]
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

	counter=counter+numberofRecords
	fo=open("last_record.txt","w")
	fo.write(str(last_record)+","+str(counter))
	fo.close()



print "Done"

#http://api.webhookinbox.com/i/AgWIzHx8/items/?order=created&since=id:175
