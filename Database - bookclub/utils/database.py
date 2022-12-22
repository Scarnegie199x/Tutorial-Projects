#used to store and retrieve books from a list
import json

books_file = "books.json"

def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([],file)

def _save_book(books):
    with open(books_file, 'w') as file_object:
        json.dump(books, file_object, indent=4)

def _load_book():

    with open(books_file, 'r') as file_object:
        return json.load(file_object)

def add_book():
    name = input("Enter book name:")
    author = input('Enter book Author:')
    books = _load_book()
    books.append({'name': name, 'author': author, 'read': False})
    _save_book(books)



def list_books():
    books = _load_book()
    for i in books:
        print(f"{i['name']} by {i['author']}")
        print(f"Has been Read? {i['read']}\n")

def read_book():
    books = _load_book()
    read = input("Which book have you read?")
    for i in books:
        if read == i['name']:
            i['read'] = True
    _save_book(books)

def delete_book():
    books = _load_book()
    delete = input("Which book would you like to delete?")
    for i in books:
        if delete == i['name']:
            books.remove(i)
    _save_book(books)