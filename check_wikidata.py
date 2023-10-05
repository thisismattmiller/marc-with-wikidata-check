import requests
import json
import glob
import pymarc
import re
from collections import Counter
# 708
# Counter({True: 577, False: 131}) total: 968

results={}
results_totals = {'024':0,'670':0}
total_xml_with_024 = len(list(glob.glob('xml/*.xml')))




def checkWikidata(file, field):

	# sometimes they do /entity/ and sometimes /wiki/ in the url path
	reg_results = re.findall(r'wikidata\.org/.*/Q[0-9]+',str(field))
	if len(reg_results) == 1:
		qid = reg_results[0].split('/')[-1]

		mediawikid_api = f"https://www.wikidata.org/w/api.php?action=wbgetentities&sites=enwiki&ids={qid}&props=claims&languages=en&format=json"
		data = requests.get(mediawikid_api, headers={"user-agent":"MARC LCCN Bot Test"})
		data = json.loads(data.text)

		p244 = False

		if 'entities' in data:
			if qid in data['entities']:
				for claim in data['entities'][qid]['claims']:
					if claim == 'P244':
						p244 = data['entities'][qid]['claims'][claim][0]['mainsnak']['datavalue']['value']
			else:
				print('qid not found in entities',qid)	
		else:
			print('entities not found in response to ', qid)


		if p244:
			print(p244, qid)
			results[file] = True
		else:	
			print('No lccn', qid)
			results[file] = False


		print(len(results))
		print(results_totals)
		print(Counter(results.values()), 'total:',total_xml_with_024)
		return True


	return False





for file in glob.glob('xml/*.xml'):


	marc = pymarc.parse_xml_to_array(file)[0]
	found_wiki = False

	for field in marc.get_fields():
		if 'wikidata.org' in str(field):

			# look in 024
			if '=024' in str(field):
				found_wiki = checkWikidata(file,field)
				if  found_wiki == True:
					results_totals['024'] = results_totals['024'] + 1
					# if we find it in the 024, don't bother looking in the 670
					break
					
			if '=670' in str(field):
				found_wiki = checkWikidata(file,field)
				if  found_wiki == True:
					results_totals['670'] = results_totals['670'] + 1




	if found_wiki == False:
		print("No Wiki Found", file)
					
