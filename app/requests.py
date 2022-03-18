import requests
import urllib.request
import json
from app.models import Book
book = Book
random_books_url = 'https://www.googleapis.com/books/v1/volumes?q=isbn'


def get_random_books():
    get_books_url = random_books_url
    with urllib.request.urlopen(get_books_url) as url:
        get_book_data = url.read()
        get_book_response = json.loads(get_book_data)
        if get_book_response:
            book_results = get_book_response
        return book_results


def process_results(book_list):
    book_results = []
    for book_item in book_list:
        id = book_item.get('id')
        image_url = book_item.get('image_url')
        title = book_item.get('title')
        publisher = book_item.get('publisher')
        description = book_item.get('description')

        book = book(id, image_url, title, publisher, description)
        book_results.append(book)
    print('book_results')
    return book_results
