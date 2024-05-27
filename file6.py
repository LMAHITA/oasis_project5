from tkinter import *
import socket
import threading

def send():
    message = e.get().lower()
    e.delete(0, END)
    txt.insert(END, "\nYou -> " + message)
    client_socket.send(message.encode('utf-8'))

    # Bot responses based on user input
    if message == "hello":
        txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")
    elif message in ["hi", "hii", "hiiii"]:
        txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")
    elif message == "how are you":
        txt.insert(END, "\n" + "Bot -> fine! and you")
    elif message in ["fine", "i am good", "i am doing good"]:
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.")
    elif message in ["thanks", "thank you", "now its my time"]:
        txt.insert(END, "\n" + "Bot -> My pleasure !")
    elif message in ["what do you sell", "what kinds of items are there", "have you something"]:
        txt.insert(END, "\n" + "Bot -> We have coffee and tea")
    elif message in ["tell me a joke", "tell me something funny", "crack a funny line"]:
        txt.insert(END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")
    elif message in ["goodbye", "see you later", "see yaa"]:
        txt.insert(END, "\n" + "Bot -> Have a nice day!")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")


def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                txt.insert(END, "\n" + message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

root = Tk()
root.title("Chat Application")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

label1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to Chat", font=FONT_BOLD, pady=10, width=20, height=1)
label1.grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send_button = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send)
send_button.grid(row=2, column=1)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

threading.Thread(target=receive_messages).start()

root.mainloop()
