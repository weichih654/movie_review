import movie_review
import searcher
import matcher

if __name__ == "__main__":
    searcher = ReviewSearcher("不可能的任務5")
    reviews = []
    reviews = searcher.reviews

    for r in reviews:
        review = MovieReview(r)
        print "link = " + r
        print "content = " + review.content
