import socket
import subprocess
from tkinter import ttk
import tkinter

class StuftCraft:
    def __init__(self):
        self.client = None
        self.server = None
        self.window = tkinter.Tk()
        self.window.wm_title("Stuft Craft")
        self.window.wm_minsize(300,300)

        self.name_var = tkinter.StringVar(value="Player1")
        self.name_entry = ttk.Entry(self.window, textvariable=self.name_var)

        self.start_button = ttk.Button(self.window, text="Start Game", command=self.main)

        self.player_count = tkinter.StringVar(value="2")
        self.player_counter = ttk.Spinbox(self.window, textvariable=self.player_count, values=["2","3","4"])
        self.player_counter.state(["readonly"])

        self.map_name = tkinter.StringVar(value="Plain")
        self.map_selector = ttk.Combobox(self.window, textvariable=self.map_name, values=["Plain", "Desert", "Cave"])
        self.map_selector.state(["readonly"])

        self.port_var = tkinter.StringVar(value="4001")
        self.port_entry = ttk.Entry(self.window, textvariable=self.port_var)

        self.address_out = tkinter.StringVar(value="")
        self.address_output = ttk.Entry(self.window, textvariable=self.address_out)

        self.join_button = ttk.Button(self.window, text="Join Game")

        self.address_var = tkinter.StringVar(value="")
        self.address_entry = ttk.Entry(self.window, textvariable=self.address_var)

        ttk.Label(self.window, text="Name:").place(x=5, y=10)
        self.name_entry.place(x=5, y=30)

        self.player_counter.place(x=5, y=55, width=50)
        self.map_selector.place(x=60, y=55, width=70)

        ttk.Label(self.window, text="Port:").place(x=5, y=80)
        self.port_entry.place(x=60, y=80, width=70)

        self.start_button.place(x=5, y=105, width=130)

        ttk.Label(self.window, text="Hosting Address:").place(x=5, y=135)
        self.address_output.place(x=5, y=155)

        self.join_button.place(x=5, y=180, width=130)

        ttk.Label(self.window, text="Host's Address:").place(x=5, y=210)
        self.address_entry.place(x=5, y=230)

        self.join_button.state(statespec=["disabled"])
        self.address_output.state(statespec=["readonly"])

        self.name_entry.bind("<KeyRelease>", self.entry_change, add='')
        self.address_entry.bind("<KeyRelease>", self.entry_change, add='')

        self.start_button.bind("<ButtonPress>", self.start_button_pressed, add='')
        self.join_button.bind("<ButtonPress>", self.join_button_pressed, add='')

        #self.window.protocol("WM_DELETE_WINDOW", self.exit)

    #def exit(self):
       # if self.client is not None:
       #     self.client.exit()
       # if self.server is not None:
       #     self
    def entry_change(self, event: tkinter.Event):
        if self.name_var.get() == "":
            self.join_button.state(statespec=["disabled"])
            self.start_button.state(statespec=["disabled"])
        else:
            if self.address_var.get() == "":
                self.join_button.state(statespec=["disabled"])
            else:
                self.join_button.state(statespec=["!disabled"])
            self.start_button.state(statespec=["!disabled"])

    def start_button_pressed(self, event):
        '''player_count = int(self.player_count.get())
        self.server = StuftCraftServer(player_count, self.map_name.get())
        self.address_out.set(self.server.get_address())
        server_thread = threading.Thread(target=self.server.run)
        server_thread.start()'''


        subprocess.Popen(["pythonw", "server.py", self.player_count.get(), self.map_name.get(), self.port_var.get()])


        '''self.client = StuftCraftClient(self.name_var.get())
        ipAddress, port = self.server.get_address().split(":")
        port = int(port)
        address = (ipAddress, port)
        self.client.connect(address)
        self.client_thread = threading.Thread(target=self.client.play)
        self.client_thread.start()
        self.has_client = True'''

        ipAddress = socket.gethostbyname(socket.gethostname())
        subprocess.Popen(["pythonw", "client.py", self.name_var.get(), ipAddress, self.port_var.get()])

        self.address_out.set(f"{ipAddress}:{self.port_var.get()}")

    def join_button_pressed(self, event):
        '''self.client = StuftCraftClient(self.name_var.get())'''
        ipAddress, port = self.address_var.get().split(":")
        '''port = int(port)
        address = (ipAddress, port)
        self.client.connect(address)
        self.client_thread = threading.Thread(target=self.client.play)
        self.client_thread.start()
        self.has_client = True'''

        subprocess.Popen(["pythonw", "client.py", self.name_var.get(), ipAddress, port])

    def main(self):
        self.window.mainloop()

if __name__ == "__main__":
    stuft_craft = StuftCraft()
    stuft_craft.main()

