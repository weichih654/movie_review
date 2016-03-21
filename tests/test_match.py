# -*- coding: utf-8 -*-
from fuzzywuzzy import fuzz
import sys 
import os
sys.path.append(os.path.abspath("../"))
from libs.movie_review import MovieReview
from libs.review_searcher import ReviewSeacher
from libs.matcher import Matcher
import os
from os import path

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

allurl = []
reviews = {}
def match (filename, movie_name):
    searcher = ReviewSeacher (movie_name)
    content = readfile (filename)
    global allurl
    global reviews
    if len(allurl) == 0:
        allurl = searcher.reviews
    i = 0
    print "file = " + filename
    for p in allurl:
        review = None
        if p not in reviews:
            review = MovieReview (p)
            reviews[p] = review
        else:
            review = reviews[p]
        matcher = Matcher()
        ratio = matcher.match (content, review.content)
        if ratio > 50:
            print "ratio = " + str(ratio) + " %"
            print "link = " + p
        i = i + 1
        progress = (i * 100 / len(allurl)) 
        sys.stdout.write("\r%d %%" % progress)
        sys.stdout.flush()
    print "\n"    

if __name__ == "__main__":
    movie_name = sys.argv[1]
    input_path = sys.argv[2]
    print "path " + input_path
    files = [f for f in os.listdir(input_path)]

    for f in files:
        match (input_path + "/" + f, movie_name)

