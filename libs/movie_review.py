import urllib2
import re

def remove_string (pattern, content):
    m = re.sub (pattern, "", content)
    return m

class MovieReview:
    def __init__ (self, link):
        self.link = link
        self.parser = PttReviewParser(link); #PttReviewParser, EyesOpenReviewParser or others

    @property
    def content (self):
        return self.parser.content

class ReviewParser:
    def __init__ (self, link):
        self.link = link

    @property
    def content (self):
        pass

class PttReviewParser(ReviewParser):
    def __init__ (self, link):
        self.link = link
        response = urllib2.urlopen(link)
        self.html = response.read()

    @property
    def content (self):
        m = re.search('.*article-meta-value.*?<\/div\>(.*)\xe2\x80\xbb \xe7\x99\xbc\xe4\xbf\xa1\xe7\xab\x99', str(self.html), re.DOTALL)
        cont = remove_string ("<.*?>", m.group(1))
        cont = remove_string ("http[\w\/:\.-]*", cont)
        return cont

class EyesOpenReviewParser(ReviewParser):
    def __init__ (self, link):
        self.link = link

    @property
    def content (self):
        return ""
