import zmq
import sys

string = 'get_booksub_status'

value = sys.argv[1]
context = zmq.Context()
print("Client attempting to connect to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print(f"Sending a request...")
socket.send_string(value)
message = socket.recv()
print(f"Server sent back: {message.decode()}")
socket.send_string("Q")




# # value = sys.argv[1]
# value = 'retrieve'
# context = zmq.Context()
# print("Client attempting to connect to server...")
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5556")
#
# # Retrieve book submission status by username
# def retrieve_booksub_status():
#     request = {
#         'action': 'get_booksub_status'
#     }
#     try:
#         string = 'get_booksub_status'
#         socket.send_string(string)
#         message = socket.recv()
#         print(f"Server sent back: {message.decode()}")
#         socket.send_string("Q")
#     #     if response['status'] == 'success':
#     #         books = response['books']
#     #         if books:
#     #             print (f"{username}'s current books: ")
#     #             for book in books:
#     #                 print(f"Title: {book['title']}")
#
#     #         else:
#     #             print("{username} has no books.")
#     #         return books
#     #     else:
#     #         print(response['message'])
#     #         return []
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []
#
# print(f"Sending a request...")
# if value == "retrieve":
#     retrieve_booksub_status()
# message = socket.recv()
# print(f"Server sent back: {message.decode()}")
# socket.send_string("Q")

