from utils import database
import sqlite3


def menu():
    user_input = '0'
    while user_input != '5':
        user_input = input(USER_CHOICE)
        if user_input in MENU_OPTIONS:
            selected_function = MENU_OPTIONS[user_input]
            selected_function()
        else:
            pass


USER_CHOICE = """
Enter:
1. Add book to list
2. List all books
3. Mark book as read
4. Delete Book
5. Quit

Choice:"""

MENU_OPTIONS = {
    '1': database.add_book,
    '2': database.list_books,
    '3': database.read_book,
    '4': database.delete_book,
}



menu()

