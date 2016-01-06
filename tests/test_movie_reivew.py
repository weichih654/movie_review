if __name__ == "__main__":
    url = "https://www.ptt.cc/bbs/movie/M.1438186905.A.0EF.html"
    review = MovieReview (url)
    print "link = " + url
    print "type = "
    print "content = " + review.content
