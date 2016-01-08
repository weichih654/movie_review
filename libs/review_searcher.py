# -*- coding: utf-8 -*-
import urllib2
import re
class ReviewSeacher:
    def __init__ (self, movie_name):
        keyword = movie_name + "%20site:ptt.cc"
        url = "http://www.google.com/search?q=" + keyword
        self.__reviews = []
        self.__get_links_by_url (url)

    def __get_links_by_url (self, url):
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,} 
        request=urllib2.Request(url,None,headers)
        response = urllib2.urlopen(request)
        data = response.read()

        self.html = data

        m = re.findall ("https:\/\/www\.ptt\.cc\/bbs\/movie.*?html", self.html)
        self.__reviews.extend (m)

    @property
    def reviews (self):
        l = list(set(self.__reviews))
        return l
