# marc-with-wikidata-check

A simple script to download the last 50,000 NACO records from id.loc.gov that have a 024 with a Wikidata Q number.

`donwload_from_id_loc_gov.py` - Downloads from id.loc.gov feed, checks each one for a 024 wikidata and saves the MARC if so.

`check_wikidata.py` - Checks the MARC XML downloaded that have 024 with wikidata if the wikdiata record has a P244 reflecting that.

-----
## results
```
50,000 NACO records from 2023-09-09 - 2023-10-04 that were created or modified (from this feed: https://id.loc.gov/authorities/names/activitystreams/feed/1.json) 
943 had a Wikidata URL in it somewhere
707 had one in the 024
236 had one in the 670
793 have a P244
151 do not have a P244
So 16% of MARC records that have a Wikidata URI in them there has not had the LCCN added to Wikidata
```
