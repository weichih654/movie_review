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

    @property
    def content (self):
        return ""

class EyesOpenReviewParser(ReviewParser):
    def __init__ (self, link):
        self.link = link

    @property
    def content (self):
        return ""
