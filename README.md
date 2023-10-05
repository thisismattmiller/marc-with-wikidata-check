# marc-with-wikidata-check

A simple script to download the last 50,000 NACO records from id.loc.gov that have a 024 with a Wikidata Q number.

`donwload_from_id_loc_gov.py` - Downloads from id.loc.gov feed, checks each one for a 024 wikidata and saves the MARC if so.

`check_wikidata.py` - Checks the MARC XML downloaded that have 024 with wikidata if the wikdiata record has a P244 reflecting that.

