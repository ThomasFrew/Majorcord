 ''' Copyright 2018 Thomas Frew
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.  '''

#Imports modules
from tkinter import *
from time import *

#Creates class "Server"
class Server:
    ''' A base class for all servers and documents '''
    def __init__( self, name, button_ID, file_location):
        self.name = name
        self.button_ID = button_ID
        self.file_location = file_location

#Creates "Server" objects for future reference
server_1_attributes = Server("Server 1 (G♯)", "server_1_button", "Server 1 (G sharp).txt")
server_2_attributes = Server("Server 2 (C♮)", "server_2_button", "Server 2 (C natural).txt")
server_3_attributes = Server("Server 3 (E♭)", "server_3_button", "Server 3 (E flat).txt")
server_4_attributes = Server("Server 4 (B♭)", "server_4_button", "Server 4 (B flat).txt")
license_attributes = Server("License", "license_button", "LICENSE.txt")

#Lists all elements on different screens of the program (can systematically be removed during transitions
request_server_widgets = [server_1_attributes.button_ID, server_2_attributes.button_ID, server_3_attributes.button_ID, server_4_attributes.button_ID, license_attributes.button_ID]
enter_username_widgets = ["username_entry", "username_button"]
write_messages_widgets = ["message_entry", "message_button"]
        
#Creates vital variables
username = "undefined"
message = "undefined"
chosen_server_attributes = "undefined"


#Creates Tkinter window
window = Tk()
window.title("Majorcord")

#Creates widgets
status = Label(font = ("georgia", 15, "italic"))

server_1_button = Button(text = "Server 1 (G♯)", relief = "groove")
server_2_button = Button(text = "Server 2 (C♮)", relief = "groove")
server_3_button = Button(text = "Server 3 (E♭)", relief = "groove")
server_4_button = Button(text = "Server 4 (B♭)", relief = "groove")
license_button = Button(text = "License", relief = "groove" )

username_entry = Entry(textvariable = username, relief = "groove", width = 60)
username_button = Button(text = "Enter", relief = "groove")

message_entry = Entry(textvariable = message, relief = "groove", width = 60)
message_button = Button(text = "Send", relief = "groove")

#Creates menubar and sub-menus
menu_bar = Menu(window)

settings_menu = Menu(menu_bar, tearoff=0)
settings_menu.add_command(label = "Change Server")
settings_menu.add_command(label = "Change Username")
menu_bar.add_cascade(label = "Settings", menu = settings_menu)

update_menu = Menu(menu_bar, tearoff=0)
update_menu.add_command(label = "Past 1 Message")
update_menu.add_command(label = "Past 5 Messages")
update_menu.add_command(label = "Past 15 Messages")
menu_bar.add_cascade(label = "Reload", menu = update_menu)

menu_bar.add_command(label = "Quit")

window.config(menu = menu_bar)


#Displays a variety of servers and requests one
def request_server():
    status.configure( text = "Welcome to Majorcord! Please select a server." )
    status.grid( row = 1, column = 1, columnspan = 5, padx = 5, pady = 5 )
    
    server_1_button.grid(row = 2, column = 1, padx = 5, pady = 5)
    server_2_button.grid(row = 2, column = 2, padx = 5, pady = 5)
    server_3_button.grid(row = 2, column = 3, padx = 5, pady = 5)
    server_4_button.grid(row = 2, column = 4, padx = 5, pady = 5)
    license_button.grid(row = 2, column = 5, padx = 5, pady = 5)

    for i in enter_username_widgets:
        eval(i).grid_forget()
    for i in write_messages_widgets:
        eval(i).grid_forget()

    settings_menu.entryconfigure("Change Server", state = NORMAL)
    settings_menu.entryconfigure("Change Username", state = DISABLED)
    update_menu.entryconfigure("Past 1 Message", state = DISABLED)
    update_menu.entryconfigure("Past 5 Messages", state = DISABLED)
    update_menu.entryconfigure("Past 15 Messages", state = DISABLED)

#Selects server 1
def choose_server_1():
    global chosen_server_attributes
    chosen_server_attributes = server_1_attributes
    request_username()

#Selects server 2
def choose_server_2():
    global chosen_server_attributes
    chosen_server_attributes = server_2_attributes
    request_username()
    
#Selects server 3
def choose_server_3():
    global chosen_server_attributes
    chosen_server_attributes = server_3_attributes
    request_username()
    
#Selects server 4
def choose_server_4():
    global chosen_server_attributes
    chosen_server_attributes = server_4_attributes
    request_username()

#Prints license document
def open_license():
    status.configure(text = "license opened. Please select a server.")
    with open(license_attributes.file_location, "r") as f:
        lines = f.read().splitlines()

    for i in lines:
        print(i)

#Requests username
def request_username():
    status.configure(text = "I N T E R E S T I N G. Please enter a username.")
    username_entry.grid(row = 2, column = 3, padx = 5, pady = 5)
    username_button.grid(row = 2, column = 4, padx = 5, pady = 5)
    
    for i in request_server_widgets:
        eval(i).grid_forget()
    for i in write_messages_widgets:
        eval(i).grid_forget()

    settings_menu.entryconfigure("Change Server", state = NORMAL)
    settings_menu.entryconfigure("Change Username", state = NORMAL)
    update_menu.entryconfigure("Past 1 Message", state = DISABLED)
    update_menu.entryconfigure("Past 5 Messages", state = DISABLED)
    update_menu.entryconfigure("Past 15 Messages", state = DISABLED)

#Enters username
def enter_username():
    global username
    global chosen_server_attributes
    username = username_entry.get()

    if len(username) < 2 or len(username) > 20:
        username_entry.delete(0, END)
        status.configure(text = "Please enter a username 2-20 characters long.")
    else:
        username_entry.delete(0, END)
        write_messages() 

#Connects to server and retreives messages
def write_messages():
    status.configure(text = "Welcome " + username + "! Type a message below:")
    print("Connection established to " + chosen_server_attributes.name + ".")
    print("Welcome " + username + ". Retreiving past 15 messages...")

    with open(chosen_server_attributes.file_location, "r+") as f:
        lines = f.read().splitlines()

    if len(lines) > 15:
        lines = lines[-15:]
    if len(lines) < 1:
        print("There a currently no messages on " + chosen_server_attributes.name + "!")

    for i in lines:
        print(i)

    message_entry.grid( row = 2, column = 3, padx = 5, pady = 5 )
    message_button.grid( row = 2, column = 4, padx = 5, pady = 5 )
    
    for i in request_server_widgets:
        eval(i).grid_forget()
    for i in enter_username_widgets:
        eval(i).grid_forget()

    settings_menu.entryconfigure("Change Server", state = NORMAL)
    settings_menu.entryconfigure("Change Username", state = NORMAL)
    update_menu.entryconfigure("Past 1 Message", state = NORMAL)
    update_menu.entryconfigure("Past 5 Messages", state = NORMAL)
    update_menu.entryconfigure("Past 15 Messages", state = NORMAL)

def send_message():
    global username
    file = open(chosen_server_attributes.file_location, "a+")

    message = (username + ": " + message_entry.get())
    file.write("\n" + message)
    print(message)
    
    message_entry.delete(0, END)

def update_1():
    status.configure(text = "Loaded Past 1 Message.")
    print("Retreiving past 1 message...")    
    with open(chosen_server_attributes.file_location, "r+") as f:
        lines = f.read().splitlines()

    if len(lines) > 1:
        lines = lines[-1:]
    if len(lines) < 1:
        print("There a currently no messages on " + chosen_server_attributes.name + "!")

    for i in lines:
        print(i)

def update_5():
    status.configure(text = "Loaded Past 5 Messages.")
    print("Retreiving past 5 message...") 
    with open(chosen_server_attributes.file_location, "r+") as f:
        lines = f.read().splitlines()

    if len(lines) > 5:
        lines = lines[-5:]
    if len(lines) < 1:
        print("There a currently no messages on " + chosen_server_attributes.name + "!")

    for i in lines:
        print(i)

def update_15():
    status.configure(text = "Loaded Past 15 Messages.")
    print("Retreiving past 15 message...") 
    with open(chosen_server_attributes.file_location, "r+") as f:
        lines = f.read().splitlines()

    if len(lines) > 15:
        lines = lines[-15:]
    if len(lines) < 1:
        print("There a currently no messages on " + chosen_server_attributes.name + "!")

    for i in lines:
        print(i)
        

#Links buttons to functions
server_1_button.configure(command = choose_server_1)
server_2_button.configure(command = choose_server_2)
server_3_button.configure(command = choose_server_3)
server_4_button.configure(command = choose_server_4)
license_button.configure(command = open_license)

username_button.configure(command = enter_username)

message_button.configure(command = send_message)

#Links sub-menu commands to functions
settings_menu.entryconfigure("Change Server", command = request_server)
settings_menu.entryconfigure("Change Username", command = request_username)

update_menu.entryconfigure("Past 1 Message", command = update_1)
update_menu.entryconfigure("Past 5 Messages", command = update_5)
update_menu.entryconfigure("Past 15 Messages", command = update_15)

menu_bar.entryconfigure("Quit", command = window.destroy)

window.config(menu = menu_bar)


#Begins the process
request_server()

#Creates main loop
window.mainloop()
