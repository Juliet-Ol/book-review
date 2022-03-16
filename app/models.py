class Book:

    def __init__(self, id,title,author,publisher,description):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.description = description

class Review:
    all_reviews = []
    def __init__(self,book_id,title,image_url,review):
        self.book_id = book_id
        self.title = title
        self.image_url = image_url
        self.review = review

