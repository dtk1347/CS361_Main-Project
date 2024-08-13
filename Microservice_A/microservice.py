# Book submission Microservice using REQ/Reply in ZMQ

# imports
import zmq
import json
import os

# ZMQ Port
context = zmq.Context()
socket = context.socket(zmq.REP)

# Change socket as needed
socket.bind("tcp://localhost:5555")

# Assign data file to variable
DATA_FILE = 'bookdata.json'


def load_data():
    '''Function to read book data from json file  '''
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return{}


def save_data(data):
    ''' Function to write data to bookdata.json'''
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)



def add_book(user_request):
    '''Add book function to present/save data by username '''
    try:
        username = user_request['username']
        new_books = user_request['books']

        book_data = load_data()

        # check for existing user, present current list
        if username in book_data:
            user_books = book_data[username]
        # If no books found for user, extend list to add new book(s)
        else:
            user_books = []

        # using extend here to accomodate multiple book entry additions
        user_books.extend(new_books)
        book_data[username] = user_books


        save_data(book_data)

        return{"status":"success", "message": "Book(s) added succesfully!"}

    # exception
    except Exception as e:
        return {"status":"error", "message":  f"An error has occurred: {e}."}
    



def get_books(user_request):
    try:

        username = user_request['username']
        book_data = load_data()

        if username in book_data:
            user_books = book_data[username]
            return {'status': "success", "books": user_books}
        else:
            return {"status": "error", "message": "No books found."}
        
    except Exception as e:
        return{"status": "error", "message": f"Error {e}."}
    


# Await request, respond as needed
while True:
    user_request = socket.recv_json()

    # When submit_books request is received, call add_book
    if user_request.get('action') == 'submit_books':
        response = add_book(user_request)
        
    # when get_list request received, call get_books
    elif user_request.get('action') == 'get_list':
        response = get_books(user_request)
    
    else:

        response = add_book(user_request)



    # ZMQ Actions 
    socket.send_json(response)