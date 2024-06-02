from client import StuftCraftClient
from server import StuftCraftServer

import threading

Client = StuftCraftClient()
Server = StuftCraftServer()

Client.elements = Server.elements
Client.lock = Server.lock

ClientThread = threading.Thread(target=Client.play)

ServerThread = threading.Thread(target=Server.run)


ServerThread.start()
ClientThread.start()

ServerThread.join()
ClientThread.join()