import os
import sys
import time
run = True 
var_id="OdZX3GVv"
while run :
	CurlString="curl -X POST 'http://api.webhookinbox.com/i/"+var_id+"/refresh/'"
	os.system(CurlString)
	time.sleep(900)
