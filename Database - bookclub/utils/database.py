from .database_connection import DatabaseConnection



def create_book_table():

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

def _load_book():

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
        return books

def add_book():

    name = input("Enter book name:")
    author = input('Enter book Author:')

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)',(name, author))

def list_books():

    books = _load_book()
    for i in books:
        print(f"{i['name']} by {i['author']}")
        read = 'YES' if i['read'] else 'NO'
        print(f"Has been Read? {read}\n")

def read_book():

    name = input("Which book have you read?")

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name = ?',(name,))

def delete_book():

    name = input("Which book would you like to delete?")

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name = ?', (name,))


