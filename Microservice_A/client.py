# Client model program to test microservice A

import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

BOOK_LIMIT = 3

# Retrieve books by username

def retrieve_books(username):
    request = {
        'action': 'get_list',
        'username': username
    }
    try:
        socket.send_json(request)
        response = socket.recv_json()
        if response['status'] == 'success':
            books = response['books']
            if books:
                print (f"{username}'s current books: ")
                for book in books:
                    print(f"Title: {book['title']}")
                
            else:
                print("{username} has no books.")
            return books
        else: 
            print(response['message'])
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []



def submit_books(username):
    # Check against book limit, notify if limit met.
    current_books = retrieve_books(username)
    if len(current_books) >= BOOK_LIMIT:
            print(f"You have {len(current_books)} books. The maximum allowed is {BOOK_LIMIT}.")
            return


    books_to_add = []

    # Get book input, prompt user limit minus current total times.
    for i in range(BOOK_LIMIT):
        title = input(f"Enter book {i+1}'s title, or press Enter to exit: ")
        if not title:
            break
        author = input(f"Author name: ")
        url = input(f"Enter URL: ")
        description = input(f"Book description: ")

        books_to_add.append({'title': title, 'author': author, 'url': url, 'description': description})

        # Limit to adding 3 in a single session

        if len(books_to_add) >= BOOK_LIMIT:
            print(f"You have entered the maximum number of books for this session.")

    if not books_to_add:
        print("No books to add.")
        return

    request = {
        'action': 'submit_books',
        'username': username,
        'books': books_to_add
    }

    socket.send_json(request)
    response = socket.recv_json()
    print(response)


if __name__ == '__main__':
    username = input("Enter your username: ")
    while True:
        print("1. Submit new book(s)")
        print("2. View books")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3: ")

        if choice == '1':
            submit_books(username)
        elif choice == '2':
            retrieve_books(username)
        
        elif choice == '3':
             break
        # user picks something else
        else:
             print("That is not valid. Please choose 1, 2, or 3.")