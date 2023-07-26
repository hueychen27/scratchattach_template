import os

# import some libraries you want to improt

from server import server

os.system("pip install scratchattach")
os.system("pip install requests")

import scratchattach as scratch3

server()
# ! do not change what's above except add libraries and stuff
session = scratch3.Session("put your session id here", username="put your username here")
conn = session.connect_cloud("put your scratch project id here")
client = scratch3.CloudRequests(conn)


@client.request
def foo(argument1, argument2):
    return f"Arg1: {argument1}. Arg2: {argument2}" # what is returned is what your scratch project receives

# ! do not change what's below
@client.event
def on_ready():
    print("Request handler is ready")


client.run()
