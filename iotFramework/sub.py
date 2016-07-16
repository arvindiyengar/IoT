# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import time
import uuid
import datetime
import pika

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

def connect_rmq(var):
	#client.loop_start()
	print "In connect"
	#var=json.loads(input_var)
	credentials = pika.PlainCredentials(rmqUsername,rmqPassword)
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=rmqHost,port=rmqPort,virtual_host=rmqVirtual_host,credentials=credentials))
	channel = connection.channel()
	#channel.exchange_declare(exchange=rmqExchange,type='topic')

	data['payload']=var
	intercept['InterceptData']=data
	message=str(intercept)
	print 'Message sent to RMQ \n',message
	channel.basic_publish(exchange='e.analytic.in.topic.request',routing_key=rmqRoutingKey,body=message)
	connection.close()
	print "Out connect"
	#client.loop_stop()


def on_connect(client, userdata, flags, rc):
	#print("Connected with result code "+str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe(topic)

def on_message(client, userdata, msg):
	print("Received a new message from : "+msg.topic+" . Message : "+str(msg.payload))
	#print "abc"
	#print "-",msg.payload
	var=json.loads(msg.payload)
	#connect_rmq(var)
        credentials = pika.PlainCredentials(rmqUsername,rmqPassword)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rmqHost,port=rmqPort,virtual_host=rmqVirtual_host,credentials=credentials))
        channel = connection.channel()
        #channel.exchange_declare(exchange=rmqExchange,type='topic')
	#print "Thi is the payload \n ",var
	data['timestamp']=str(datetime.datetime.utcnow())       
	data['transactionId']=str(uuid.uuid4())
	data['payload']=var
        intercept['InterceptData']=data
        message=json.dumps(intercept)
        print 'Message sent to RMQ \n',message
        channel.basic_publish(exchange='e.analytic.in.topic.request',routing_key=rmqRoutingKey,body=message)
        connection.close()
        print "Out connect"



#Connect to MQTT
client = mqtt.Client(client_id="SUB", clean_session=True)
client.on_connect = on_connect
client.on_message = on_message
client.connect(host,port, 60)


run=True
while run:
	client.loop()

