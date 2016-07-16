import os
import sys
import json
import ast
import random
import time
import uuid
from urlparse import parse_qs, urlparse


fi=open("temp_webhook_output.json","r")
input_data=json.load(fi)
last_record_temp=int(input_data['last_cursor'])
numberofRecords=len(input_data['items'])
fi.close()

f=open('last_record.txt','r')
var=f.read().split(',')
last_record=int(var[0])
counter=var[1]
f.close()

if(last_record_temp>last_record):


	print "Greater"
	# We need to append the contents

	fo=open("webhook_output.json","r+")
	input_data_output=json.load(fo)
	input_data_output['items']=input_data_output['items']+input_data['items']
	fo.seek(0,0)
	fo.write(json.dumps(input_data_output))
	fo.close()

	fo=open("last_record.txt","w")
	fo.write(str(last_record_temp)+","+str(counter)+","+str(numberofRecords))
	fo.close()

	#os.system('python script.py')
else:
	print "lesser"
