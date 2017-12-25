#!/usr/bin/env python2
# coding:utf-8
import xml.sax
class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData=""
        self.type = ""
        self.format=""
        self.year=""
        self.rating=""
        self.stars=""
        self.description=""
    def startElement(self, name, attrs):
        self.CurrentData=name
        if name=="movie":
            print "******Movie******"
            title = attrs["title"]
            print "Title:",title
    def endElement(self, name):
        if self.CurrentData=="type":
            print "Type:",self.type
        elif self.CurrentData=="format":
            print "Format",self.format
        elif self.CurrentData=="year":
            print "Year:",self,self.format
        elif self.CurrentData=="rating":
            print "Ration:",self.rating
        elif self.CurrentData=="stars":
            print "Stars:",self.stars
        elif self.CurrentData=="description":
            print "Description:",self.description
        self.CurrentData=""
    def characters(self, content):
        if self.CurrentData == "type":
            self.type=content;
        elif(self.CurrentData == "format"):
            self.format=content;
        elif(self.CurrentData == "year"):
            self.year=content;
        elif(self.CurrentData == "rating"):
            self.rating=content
        elif(self.CurrentData=="stars"):
            self.stars=content
        elif(self.CurrentData=="description"):
            self.description=content
if(__name__=="__main__"):
    parser=xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler=MovieHandler()
    parser.setContentHandler(Handler)
    parser.parse("10241.xml")