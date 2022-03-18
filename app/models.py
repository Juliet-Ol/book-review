from urllib import response
from flask_login import UserMixin
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

    def save_review(self):
        Review.all_reviews.append(self)  

    @classmethod  
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):  
        response =[]  
        for review in cls.all_reviews:
            if review.id == id:
                response.append(review)

        return response        




    def __repr__(self):
        return '<User {}>'.format(self.username)