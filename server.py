#! /usr/bin/env python

from time import ctime
from socket import *
from threading import Thread


class ChatRoomServer(object):
    def __init__(self, host, port):
        self.client_list = []
        self.addr = (host, int(port))
        self.server_sockect = socket(AF_INET, SOCK_STREAM)
        self.server_sockect.bind(self.addr)
        self.server_sockect.listen(5)

    def start(self):
        while True:
            client, addr = self.server_sockect.accept()
            self.client_list.append(client)
            print addr, 'Connected'
            t = Thread(target=self.recv_loop, args=(client,))
            t.start()

    def recv_loop(self, client):
        while True:
            message = client.recv(1024)
            for i in self.client_list:
                if client is not i:
                    i.send(ctime()+': '+message)



if __name__ == '__main__':
    server = ChatRoomServer('', 8889)
    server.start()