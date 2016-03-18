# -*- coding: utf-8 -*-
import urllib2
import re
import time
class ReviewSeacher:
    def __init__ (self, movie_name):
        keyword = movie_name + "%20site:www.moviemovie.com.tw%20||%20site:ptt.cc"
        self.url = "https://www.google.com/search?q=" + keyword + "&num=1000"
        self.__reviews = []

    def __get_links_by_url (self, url):
        time.sleep(1)
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,} 
        request=urllib2.Request(url,None,headers)
        response = urllib2.urlopen(request)
        data = response.read()

        self.html = data

        m = re.findall ("https:\/\/www\.ptt\.cc\/bbs\/movie.*?html", self.html)
        self.__reviews.extend (list(set(m)))
        m = re.findall ("http:\/\/www.moviemovie.com.tw.*?\.html", self.html)
        self.__reviews.extend (list(set(m)))

    @property
    def reviews (self):
        self.__get_links_by_url (self.url)
        return self.__reviews 
