#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
	print "Root element :%s" % collection.getAttribute("shelft")

movies = collection.getElementsByTagName("movie")

for movie in movies:
	print "*****Movie*****"
	if movie.hasAttribute("title"):
		print "Title: %s" % movie.getAttribute("title")

	type = movie.getElementsByTagName('type')[0]
	print "Type: %s" % type.childNodes[0].data
	format = movie.getElementsByTagName("format")[0]
	print "Format: %s" % format.childNodes[0].data
	rating = movie.getElementsByTagName('rating')[0]
	print "Rating: %s" % rating.childNodes[0].data
	year = movie.getElementsByTagName('year')[0]
	print "Year: %s" % year.childNodes[0].data
	stars = movie.getElementsByTagName("stars")[0]
	print "Star: %s" % stars.childNodes[0].data
	description = movie.getElementsByTagName('description')[0]
	print "Description: %s" % description.childNodes[0].data