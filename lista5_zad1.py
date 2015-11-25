import urllib2
import re
from HTMLParser import HTMLParser
import webbrowser
from htmlentitydefs import name2codepoint
from bs4 import BeautifulSoup

#class MyHTMLParser(HTMLParser):
#    def __init__(self):
#        self.reset()
#        self.htmldata = []
#        self.tags =[]
#    def handle_starttag(self, tag, attrs):
#        self.tags.append(tag)
#    def handle_data(self,data):
#        self.htmldata.append(data)
        #text =""
        #if tag=="a":
        #    for (attr,val) in attrs:
        #        text+=attr
        #        text+=" "
        #return text

def zrob_cos_na_stronie(strona):
    zdania_z_pythonem=[]
    zupa = BeautifulSoup(urllib2.urlopen(strona).read())
    #return re.search("[A-Z](\w|\n)*(P|p)ython(\w|\n)*\.",zupa.get_text())
    return re.search("([a-zA-Z]+\.)",zupa.get_text())

    #moj_parser = MyHTMLParser()
    #moj_parser.feed(urllib2.urlopen(strona).read())
    #return moj_parser.htmldata

print zrob_cos_na_stronie("https://www.jeffknupp.com/")

