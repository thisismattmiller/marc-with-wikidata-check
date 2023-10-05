import requests
import json
import xml.etree.ElementTree as elt
import time

 

for x in range(1,500):




	feedurl = f"https://id.loc.gov/authorities/names/activitystreams/feed/{x}.json"
	print("PAGE", x, feedurl)

	data = requests.get(feedurl)
	data = json.loads(data.text)

	for rec in data['orderedItems']:

		# time.sleep(1)

		marcurl = rec['object']['id'] + '.marcxml.xml'


		xml = requests.get(marcurl)
		xmltext = xml.text

		try:
			xml = elt.fromstring(xml.text)
		except:
			print(xmltext)
			print('isssue with parsing xml')
			print(rec['object']['id'])
			continue


		if 'wikidata.org' in xmltext:

			with open('xml/' + rec['object']['id'].split('/')[-1]  + '.xml','w') as outfile:
				outfile.write(xmltext)

			print(marcurl)
			print(xml)


