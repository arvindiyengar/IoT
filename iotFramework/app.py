import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import json
import flask
import random
import logging
from flask import Flask,jsonify,request


app = Flask(__name__)

#Variables
topic="iot/defaultSensorAggregator"
Payload="This is sample Payload"
logging.basicConfig(filename='iotSensor.log',level=logging.INFO,format='%(asctime)s %(levelname)s :%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
dataError={}
msgerror={}
msgerror["ErrorMessage"]="Message Payload should be in JSON format"
msgerror["ErrorCode"]=1
dataError["Error"]=msgerror
@app.route('/request/update', methods=['POST'])
def create_task():
	if not request.json :
		logging.warning(json.dumps(dataError))
		return jsonify({"Error":{"ErrorMessage":"Message Payload should be in JSON format","ErrorCode":1}}),400
		#abort(400)
	else:	
		
		print type(request.json)
		Payload=json.dumps(request.json)
		logging.info(Payload)
		publish.single(topic,payload=Payload,hostname="localhost",port=1883,client_id="SensorPulse")
		#client = mqtt.Client(client_id="SensorPulse",clean_session="False")
		#client.connect("localhost",1883, 60)
		#client.loop_start()
		#client.publish(topic,Payload)
		#time.sleep(3)
		#client.loop_stop(force=True)
		print "Published :",Payload

	return jsonify({"Status":"Sent"}),200
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000)

