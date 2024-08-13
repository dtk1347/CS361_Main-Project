import zmq
import json
import os

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


# Assign data file to variable
DATA_FILE = 'submission_status.json'

def load_data():
    """Function to read book submission status data from json file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return

def get_book_status():
    status = load_data()
    return status['book_submissions']

def change_book_deadline(sub_deadline):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as outfile:
            submission_data = json.load(outfile)
            submission_data['book_submissions'][1] = {'deadline': sub_deadline}

    return

while True:

    message = socket.recv()
    print(f"Received request from the client: {message.decode()}")
    if len(message) > 0:
        if message.decode() == 'Q': # Client asked server to quit
            break
    # when get_list request received, call get_books
    if message.decode() == 'get_booksub_status':
        response = get_book_status()[0]
        response = "Book submission status:" + " " + response.get('status')

    if message.decode() == 'get_book_deadline':
        response = get_book_status()
        response = "Book deadline:" + " " + response[1]


    socket.send_string(response)
context.destroy()


#
#

#

#
# # Await request, respond as needed
# while True:
#     message = socket.recv()
#     print(f"Received request from the client: {message.decode()}")
#     if len(message) > 0:
#         if message.decode() == 'Q': # Client asked server to quit
#             break
#     decoded_msg = message.decode()
#
#     # # When submit_books request is received, call add_book
#     # if user_request.get('action') == 'submit_books':
#     #     response = add_book(user_request)
#

#
#     # else:
#
#     #     response = add_book(user_request)


# while True:

#     message = socket.recv()
#     print(f"Received request from the client: {message.decode()}")
#     if len(message) > 0:
#         if message.decode() == 'Q': # Client asked server to quit
#             break
#     decoded_msg = message.decode()

    # # adjust incoming strings to two decial places. 7450 --> 74.50
    # temp_str_array = str(decoded_msg)
    # temp_str_array = temp_str_array.split(',')
    # temp_int_array = [int(i)/100 for i in temp_str_array]


    # #### GRAPHING ####
    # import matplotlib.pyplot as plt
    # import numpy as np

    # # make data:
    # y = temp_int_array
    # x = np.array([i for i in range(len(y))])

    # plt.figure(figsize=(10, 6))
    # plt.plot(x, y)

    # plt.title('Temperatures each day (F)')
    # plt.xlabel('Day')
    # plt.ylabel('Temperature (F)')
    # plt.xticks(ticks=np.arange(len(y)))

    # image_name = 'graph.png'
    # plt.savefig(image_name)

#
#     socket.send_string(response)
# print("process ending")
# context.destroy()