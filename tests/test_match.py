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
    input_file = sys.argv[1]
    content = readfile (input_file)
    print "check file " + input_file
    movie_name = "新世紀福爾摩斯"
    searcher = ReviewSeacher (movie_name)
    allurl = searcher.reviews
    i = 0
    for p in allurl:
        review = MovieReview (p)
        #print "link = " + p
        #print "type = " + review.type
        #print "content = " + review.content
        matcher = Matcher()
        ratio = matcher.match (content, review.content)
        if ratio > 40:
            print "ratio = " + str(ratio) + " %"
            print "link = " + p
        i = i + 1
        progress = (i * 100 / len(allurl)) 
        sys.stdout.write("\r%d %%" % progress)
        sys.stdout.flush()
    print "\n"    

