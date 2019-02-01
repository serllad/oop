from xmlrpc.client import ServerProxy, Fault
from random import choice
from string import ascii_lowercase
from server import Node,ListableNode, UNHANDLED
from threading import Thread
from time import sleep
import tkinter as tk
HEAD_START = 0.1 # 单位为秒
SECRET_LENGTH = 100
def random_string(length):
    """
    返回一个指定长度的由字母组成的随机字符串
    """
    chars = []
    letters = ascii_lowercase[:26]
    while length > 0:
        length -= 1
        chars.append(choice(letters))
    return ''.join(chars)
class Client(tk.Frame):
    """
    一个基于文本的界面,用于访问Node类
    """
    def __init__(self,master, url, dirname, urlfile):
        """
        设置url、dirname和urlfile,并在一个独立的线程中启动Node服务器
        """
        super().__init__(master)
        self.node_setup(url, dirname, urlfile)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input = input = tk.Entry(self)
        input.pack(side='left')
        self.submit = submit = tk.Button(self)
        submit['text'] = "Fetch"
        submit['command'] = self.fetch_handler
        submit.pack()
        self.files = files = tk.Listbox()
        files.pack(side='bottom', expand=True, fill=tk.BOTH)
        self.update_list()

    def node_setup(self, url, dirname, urlfile):
        self.secret = random_string(SECRET_LENGTH)

        n = ListableNode(url, dirname, self.secret)
        t = Thread(target=n._start)
        t.setDaemon(1)
        t.start()
        # 让服务器先行一步:
        sleep(HEAD_START)
        self.server = ServerProxy(url)
        for line in open(urlfile).readlines():
            line=line.strip()
            self.server.hello(line)

    def fetch_handler(self):
        query = self.input.get()

        try:
            self.server.fetch(query, self.secret)
        except Fault as f:
            if f.faultCode != UNHANDLED: raise
            print("Couldn't find the file", query)

    def update_list(self):
        self.files.delete(0, tk.END)
        for item in self.server.list():

            self.files.insert(tk.END, item)

def main():
    #urlfile, directory, url = sys.argv[1:]
    #client = Client(url, directory, urlfile)
    root=tk.Tk()
    root.title('File Sharing Client')
    client=Client(root,'http://localhost:8881','file1','url.txt')
    client.mainloop()
if __name__ == '__main__':
    main()