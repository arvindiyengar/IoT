# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import time
import uuid
import datetime
import pika
import os

#Creating Intercept
intercept={}
data={}
payloadtype={}
payloadtype["payloadType"]="Sensor"
data['additionalAttributes']=payloadtype
data['alias']=""
data['appName']=""
data['contentType']="application/json"
data['httpHeaders']=""
data['httpMethodType']=""
data['messageVariantType']=""
data['originatingIpAddress']="localhost"
data['serviceType']="REST"
data['source']="Mosquitto"
data['target']="RabbitMQ"
#data['timestamp']=str(datetime.datetime.utcnow())
#data['transactionId']=str(uuid.uuid4())

#Variables
topic="iot/defaultSensorAggregator"
host="localhost"
port=1883
rmqUsername="siuser"
rmqPassword="welcome1"
rmqHost='devrmq.vmware.com'
rmqPort=5672
rmqVirtual_host='dev12_sdp'
rmqExchange='e.analytic.in.topic.request'
rmqRoutingKey='process.analytic.topic.request'
var={}
index_name="iotpoc_car_1"




def on_connect(client, userdata, flags, rc):

	client.subscribe(topic)

def on_message(client, userdata, msg):
	print("Received a new message from : "+msg.topic+" . Message : "+str(msg.payload))

	var=json.loads(msg.payload)

	#data['timestamp']=str(datetime.datetime.utcnow())       
	unique_id=str(uuid.uuid4())

	print "\n",var['DevicePulse']
	abc={}
	abc=var
	main={}
	loc={}
	loc['lat']=float(var['DevicePulse']['Latitude'])
	loc['lon']=float(var['DevicePulse']['Longitude'])

	abc['DevicePulse']['unique_id']=unique_id
	
	#aa="\""+var['DevicePulse']['Latitude']+"\",\""+var['DevicePulse']['Longitude']+"\""

	#aa=str(var['DevicePulse']['Latitude'])+","+str(var['DevicePulse']['Longitude'])

	#print "\n",aa

	abc['DevicePulse']['location']=loc
	
	#abc['DevicePulse']['location'].append(float(var['DevicePulse']['Longitude']))
	#abc['DevicePulse']['location'].append(float(var['DevicePulse']['Latitude']))
	abc['timestamp']=datetime.datetime.now().isoformat()
	main['doc']=abc
	main['doc_as_upsert']=True
	print "Sending ",main
	message=json.dumps(main)
	print 'Message sent to RMQ \n',message
	curlString='curl -X POST -d\''+message+'\' http://fmw-dev-build-2:9200/'+index_name+'/logs/'+unique_id+'/_update'
	print "\n",curlString
	os.system(curlString)
	print "Out connect"



#Connect to MQTT
client = mqtt.Client(client_id="SUB", clean_session=True)
client.on_connect = on_connect
client.on_message = on_message
client.connect(host,port, 60)


run=True
while run:
	client.loop()

