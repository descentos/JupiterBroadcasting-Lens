#!/usr/bin/env python

#Let's get this party started!

import logging
import optparse
import urllib2
import simplejson
import gettext
from gettext import gettext as _
gettext.textdomain('jupiterbroadcasting')

from singlet.lens import SingleScopeLens, IconViewCategory, ListViewCategory

from jupiterbroadcasting import jupiterbroadcastingconfig

class JupiterbroadcastingLens(SingleScopeLens):

    class Meta:
        name = 'Jupiter Broadcasting'
        description = 'Jupiter Broadcasting Lens'
        search_hint = 'Search Jupiter Broadcasting'
        icon = 'jupiterbroadcasting.svg'
        search_on_blank=True

    # Adding Categories
    video_category = ListViewCategory("Videos", 'dialog-information-symbolic')

    def search(self, search, results):
        # Adding search results
        results.append('https://wiki.ubuntu.com/Unity/Lenses/Singlet',
                         'ubuntu-logo',
                         self.video_category,
                         "text/html",
                         'Learn More',
                         'Visit Jupiterbroadcasting!',
                         'http://www.jupiterbroadcasting.com/')
        pass

jbroad = "http://www.jupiterbroadcasting.com/"

def jbroad_query(self, search):
	try:
		search = search.replace(" ", "|")
		url = ("?s=%s" % (self.jbroad, search))
		results = simplejson.loads(urllib2.urlopen(url).read())
		print "Searching Jupiter Broadcasting for %s" % (search)
		return results[1]

	except (IOError, KeyError, urllib2.URLError, urllib2.HTTPError, simplejson.JSONDecodeError):
		print "Error : Unable to search Jupiter Broadcasting"
	return []

#creating searching thing, I guess
def search(self, search, results):
	for video in self.jbroad_query(search):
		results.append("%s/jbroad/%s" % (self.jbroad, video),
			"https://lh4.googleusercontent.com/-x7_dU6yYsfo/AAAAAAAAAAI/AAAAAAAAAFc/ZLPiXYzja_M/s250-c-k/photo.jpg",
			self.video_category,
			"text/html"
			video,
			"Jupiter Broadcasting Videos"
			"%s/jbroad/%s" % (self.jbroad, video))
pass
	results.append (url,
			icon,
			mime-type,
			text,
			comment,
			drag and drop url)



