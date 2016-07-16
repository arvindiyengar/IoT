import time
import json
import random
import os

run=True
while run:

	sensorName="Sensor-Temp"
	sensorID=random.randint(1,200)
	tempReading=random.randint(1,200)
	sensorType="Analog"
	sensorTimeStamp=int(time.time())

	data={}
	payload={}
	payload['sensorName']=sensorName
	payload['sensorID']=sensorID
	payload['tempReading']=tempReading
	payload['sensorType']=sensorType
	payload['sensorTimeStamp']=sensorTimeStamp
	data['sensorPulse']=payload
	host='localhost'
	port=5000



	print json.dumps(data)

	CurlString='curl -H "Content-Type:application/json" -X POST -d \''+json.dumps(data)+'\' http://'+host+':'+str(port)+'/request/update'
	print CurlString
	os.system(CurlString)
	time.sleep(30)

