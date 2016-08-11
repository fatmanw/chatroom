#! /usr/bin/env python

from time import ctime
from socket import *
from threading import Thread
import Tkinter

class ChatRoomGUI(object):
    def __init__(self):
        self.top = Tkinter.Tk()
        self.top.title('Chat Room')
        self.frame1 = Tkinter.Frame(self.top)
        self.frame1.pack(side=Tkinter.TOP, fill=Tkinter.X)
        self.frame2 = Tkinter.Frame(self.top)
        self.frame2.pack(fill=Tkinter.BOTH)
        self.frame3 = Tkinter.Frame(self.top)
        self.frame3.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
        self.host_text = Tkinter.Entry(self.frame1)
        self.host_text.pack(side=Tkinter.LEFT)
        self.port_text = Tkinter.Entry(self.frame1)
        self.port_text.pack(side=Tkinter.LEFT)
        self.connect_btn = Tkinter.Button(self.frame1, command=self.connect, text='Connect')
        self.connect_btn.pack(side=Tkinter.LEFT)
        self.status_label = Tkinter.Label(self.frame2, text='No Connection')
        self.status_label.pack(side=Tkinter.TOP, fill=Tkinter.X)
        self.chat_text = Tkinter.Text(self.frame2)
        self.chat_text.pack()
        self.send_text = Tkinter.Entry(self.frame3, state='disable')
        self.send_text.pack(side=Tkinter.LEFT)
        self.send_btn = Tkinter.Button(self.frame3, command=self.send, text='Send', state='disable')
        self.send_btn.pack(side=Tkinter.LEFT)

    def connect(self):
        pass

    def send(self):
        pass


class ChatRoom(ChatRoomGUI):
    def __init__(self):
        ChatRoomGUI.__init__(self)
        self.client_socket = socket(AF_INET, SOCK_STREAM)

    def connect(self):
        host = self.host_text.get()
        port = self.port_text.get()
        addr = (host, int(port))
        self.client_socket.connect(addr)
        self.status_label.config(text='Connected')
        self.send_text.config(state='normal')
        self.send_btn.config(state='normal')
        self.host_text.config(state='disable')
        self.port_text.config(state='disable')
        self.connect_btn.config(state='disable', text='Connected')
        t = Thread(target=self.recv_loop)
        t.start()

    def send(self):
        message = self.send_text.get()
        self.send_text.config(text='')
        self.client_socket.send(message)
        self.chat_text.insert(Tkinter.END, ctime()+message+'\n')

    def recv_loop(self):
        while True:
            message = self.client_socket.recv(1024)
            self.chat_text.insert(Tkinter.END, message+'\n')


if __name__ == '__main__':
    win = ChatRoom()
    win.top.mainloop()