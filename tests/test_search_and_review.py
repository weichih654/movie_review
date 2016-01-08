# -*- coding: utf-8 -*-
import sys 
import os
sys.path.append(os.path.abspath("../"))
from libs.movie_review import MovieReview
from libs.review_searcher import ReviewSeacher
from libs.matcher import Matcher

if __name__ == "__main__":
    movie_name = "不可能的任務5"
    searcher = ReviewSeacher (movie_name)
    allurl = searcher.reviews
    for p in allurl:
        review = MovieReview (p)
        print "link = " + p
        print "type = " + review.type
        print "content = " + review.content

