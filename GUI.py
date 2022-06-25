from tkinter import *
from chatbot import chatbot
import time
 
# GUI
window = Tk()
window.title("Chatbot")
window.geometry('500x650')
 
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
SPACE = "   "

def send():
    user_input = e.get()
    received = '\nYou -> ' + user_input
    txt.insert(END, received)
    e.delete(0, END)
    Bot_res = '\nBot -> ' + chatbot(user_input)
    txt.insert(END, Bot_res, 'bot')

bot_icon = PhotoImage(file='robot.png')
human_icon = PhotoImage(file='Human.png')
bot_icon = bot_icon.subsample(20)
human_icon = human_icon.subsample(20)


lable1 = Label(window, bg=BG_COLOR, fg=TEXT_COLOR, text="Chatbot", font=FONT_BOLD, pady=10, width=10, height=1).place(x=200, y=10)
 
txt = Text(window, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=40)
txt.tag_config('bot', foreground="red")
txt.tag_config('human', foreground="yellow")
txt.config(spacing3=10)
txt.place(x=30, y=60)
txt.image_create(END, image=bot_icon)
txt.insert(END, SPACE+'Well come to Chatbot.\n', 'bot')
txt.image_create(END, image=human_icon)
txt.insert(END, SPACE+'Hello\n', 'human')

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, x=500-30, y=60)
 
e = Entry(window, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=40)
e.place(x = 30, y = 580)

send = Button(window, text="Send", font=FONT_BOLD, bg=BG_GRAY, height=1,
              command=send).place(x = 420, y = 575)
 
window.mainloop()