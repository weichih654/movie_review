# -*- coding: utf-8 -*-
from fuzzywuzzy import fuzz
import sys 
import os
sys.path.append(os.path.abspath("../"))
from libs.movie_review import MovieReview
from libs.review_searcher import ReviewSeacher
from libs.matcher import Matcher

def readfile(filename): 
    f = open(filename, "r")
    content = ""
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        content = content + line
    f.close()
    return content

if __name__ == "__main__":
    content = readfile (sys.argv[1])
    movie_name = "不可能的任務5"
    searcher = ReviewSeacher (movie_name)
    allurl = searcher.reviews
    for p in allurl:
        review = MovieReview (p)
        print "link = " + p
        #print "type = " + review.type
        #print "content = " + review.content
        matcher = Matcher()
        ratio = matcher.match (content, review.content)
        print "ratio = " + str(ratio) + " %"

