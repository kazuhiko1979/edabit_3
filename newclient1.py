from tkinter import *
import tkinter
import socket
from threading import Thread

def receive():
    
    while True:
        try:
            msg = s.recv(1024).decode("utf-8")
            if msg == "exit":
                s.close()
                break
            else:
                msg_list.insert(END, msg)
        except:
            print("An error occurred!")
            s.close()
            break

def send():
    msg = my_msg.get()
    my_msg.set("")
    if msg == "exit":
        s.send("exit".encode("utf-8"))
        s.close()
        window.quit()
    else:
        s.send(msg.encode("utf-8"))
        
def on_closing():
    my_msg.set("exit")
    send()
    window.quit()

# GUI
window = Tk()
window.title("Chat Room")
window.config(bg="green")
message_frame = Frame(window, height=100, width=100, bg="red")
my_msg = StringVar()
my_msg.set("")
Scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=15, width=100, bg="red", yscrollcommand=Scroll_bar.set)
Scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()
message_frame.pack()
button_label =Label(window, text="Enter your message here", fg="blue", font="Arial", bg="red")
button_label.pack() 
entry_field = Entry(window, textvariable=my_msg, width=100, fg="red")
entry_field.pack()
send_button = Button(window, text="Send", bg="green", font="Aerial", fg="white", command=send)
send_button.pack()
quite_button = Button(window, text="Quit", bg="green", font="Aerial", fg="white", command=on_closing)
quite_button.pack()
window.protocol("WM_DELETE_WINDOW", on_closing)

Host = '127.0.0.1'
Port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))
receive_thread = Thread(target=receive)
receive_thread.start()
mainloop()




