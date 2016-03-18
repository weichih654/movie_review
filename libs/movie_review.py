import urllib2
import re
import time

def remove_string (pattern, content):
    m = re.sub (pattern, "", content)
    return m

class MovieReview:
    def __init__ (self, link):
        self.link = link
        self.parser = None
        if "moviemovie" in link:
            self.parser = MovieMovieReviewParser(link); #PttReviewParser, MovieMovieReviewParser or others
        elif "ptt.cc" in link:
            self.parser = PttReviewParser(link); #PttReviewParser, MovieMovieReviewParser or others

    @property
    def content (self):
        return self.parser.content

    @property
    def type (self):
        return self.parser.type

class ReviewParser:
    def __init__ (self, link):
        self.link = link

    @property
    def content (self):
        pass

    @property
    def type (self):
        pass

class PttReviewParser(ReviewParser):
    def __init__ (self, link):
        time.sleep(1)
        self.link = link
        response = urllib2.urlopen(link)
        self.html = response.read()

    @property
    def content (self):
        m = re.search('.*article-meta-value.*?<\/div\>(.*)\xe2\x80\xbb \xe7\x99\xbc\xe4\xbf\xa1\xe7\xab\x99', str(self.html), re.DOTALL)
        cont = remove_string ("<.*?>", m.group(1))
        cont = remove_string ("http[\w\/:\.-]*", cont)
        return cont

    @property
    def type (self):
        return "PTT"

class MovieMovieReviewParser(ReviewParser):
    def __init__ (self, link):
        time.sleep(1)
        self.link = link
        response = urllib2.urlopen(link)
        self.html = response.read()

    @property
    def content (self):
        m = re.search('.*?<div class=\"article\">(.*?)\.program_db_link', str(self.html), re.DOTALL)
        cont = remove_string ("<.*?>", m.group(1))
        cont = remove_string ("http[\w\/:\.-]*", cont)
        cont = remove_string ("^--$", cont)
        return cont

    @property
    def type (self):
        return "MOVIEMOVIE"
