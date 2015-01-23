import urllib.request

def stupidGuid():
    doc = urllib.request.urlopen("http://www.newguid.com").read()
    encodedDoc = str(doc, encoding="utf8")
    bindex = encodedDoc.find("<b>");
    bendindex = encodedDoc.find("</b>");

    return encodedDoc[bindex+3:bendindex];
