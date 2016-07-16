import os
import sys
import json
import ast
import random
import time
import uuid
from urlparse import parse_qs, urlparse


#Variables
var_id="OdZX3GVv"


run = True 

while run:

	CurlString='curl -X GET "http://api.webhookinbox.com/i/'+var_id+'/items/?order=created" > temp_webhook_output.json'
	print CurlString
	os.system(CurlString)
	time.sleep(30)

