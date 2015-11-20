import urllib.request
import re

scrape_regex='<script type="text/javascript">var omni_guid="([\w\d-]*)";</script>'

def stupidGuid():
    doc = urllib.request.urlopen("http://forums.asp.net/").read()
    encodedDoc = str(doc, encoding="utf8")
    match = re.search(scrape_regex, encodedDoc)
    return match.group(1);
