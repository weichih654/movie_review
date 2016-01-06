class MovieReview:
    def __init__ (self, link):
        self.link = link
        self.parser = None; #PttReviewParser, EyesOpenReviewParser or others

    @property
    def content (self):
        return self.parser.content

class ReviewParser:
    def __init__ (self, link):
        self.link = link

class PttReviewParser(ReviewParser):
    def __init__ (self, link):
        self.link = link

    @property
    def content (self):
        pass

class EyesOpenReviewParser(ReviewParser):
    def __init__ (self, link):
        self.link = link

    @property
    def content (self):
        pass
