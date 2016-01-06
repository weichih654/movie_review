from libs.movie_review import MovieReview
from libs.review_searcher import ReviewSeacher
from libs.matcher import Matcher

if __name__ == "__main__":
    searcher = ReviewSeacher("test")
    reviews = []
    reviews = searcher.reviews

    for r in reviews:
        review = MovieReview(r)
        print "link = " + r
        print "content = " + review.content
