import socket
import threading

class Messenger:
    def __init__(self, Socket):
        self.socket = Socket
        self.socket.settimeout(1)
        self.messages = []
        self.lock = threading.Lock()
        self.socket_lock = threading.Lock()
        self.alive = True
        self.listener = threading.Thread(target=self.listen)
        self.listener.start()

    def get(self):
        self.lock.acquire()
        value = list(self.messages)
        self.messages = []
        self.lock.release()
        return value

    def send(self, message):
        self.socket_lock.acquire()
        self.socket.send(message, 0)
        self.socket_lock.release()

    def kill(self):
        self.alive = False

    def listen(self):
        while self.alive:
            try:
                self.socket_lock.acquire()
                mes = self.socket.recv(1000, 0)
                self.socket_lock.release()
                self.lock.acquire()
                self.messages.append(mes)
                self.lock.release()
            except ConnectionAbortedError:
                pass
