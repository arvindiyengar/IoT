#Refreshes back to Intial stage

import os 
import sys
import json

os.remove('last_record.txt')
os.remove('temp_webhook_output.json')
os.remove('webhook_output.json')

f=open('last_record.txt','w')
f.write('0,0,0')
f.close()

f=open('webhook_output.json','w')
f.write('{"items":[],"last_cursor":0}')
f.close()


print "Done Refresh"
