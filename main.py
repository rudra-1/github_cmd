__author__ = "s4g4"
__date__ = "$15 May, 2018 1:00:00 PM$"

import requests
import json
import time


with open("keywords.txt") as file:
	keywords = file.readlines()

keywords = [x.strip() for x in keywords]

output = dict()

for keyword in keywords:
	r = requests.get("https://api.github.com/search/repositories?q="+keyword)
	output[keyword] = dict()
	json_resp =  r.text
	resp = json.loads(json_resp)
	try :
		output[keyword]['count'] = resp['total_count']
		if resp['total_count'] != 0 :
			output[keyword]['items'] = resp['items']
			
	except Exception as e:
		##########################################
		##	print exception along with output
		## 	if there is any error from api.
		##########################################
		print e.message
		print json_resp
		print output

		exit() ### if there is an error from api response, exit  

	time.sleep(7)

print output
