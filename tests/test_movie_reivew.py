import sys 
import os
sys.path.append(os.path.abspath("../"))
from libs.movie_review import MovieReview
from libs.review_searcher import ReviewSeacher
from libs.matcher import Matcher

if __name__ == "__main__":
    url = "https://www.ptt.cc/bbs/movie/M.1438186905.A.0EF.html"
    review = MovieReview (url)
    print "link = " + url
    print "type = "
    print "content = " + review.content
