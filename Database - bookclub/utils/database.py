#used to store and retrieve books from a list
import sqlite3

books_file = "books.json"

def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

    connection.commit()
    connection.close()


def _load_book():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    connection.close()

    return books


def add_book():
    name = input("Enter book name:")
    author = input('Enter book Author:')

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()


    cursor.execute('INSERT INTO books VALUES(?, ?, 0)',(name, author))

    connection.commit()
    connection.close()



def list_books():
    books = _load_book()
    for i in books:
        print(f"{i['name']} by {i['author']}")
        read = 'YES' if i['read'] else 'NO'
        print(f"Has been Read? {read}\n")

def read_book():

    name = input("Which book have you read?")

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read=1 WHERE name = ?',(name,))

    connection.commit()
    connection.close()



def delete_book():

    name = input("Which book would you like to delete?")

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name = ?', (name,))

    connection.commit()
    connection.close()
