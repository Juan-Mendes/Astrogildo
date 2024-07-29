import tkinter as tk
from process import *

root = tk.Tk()
root.title('Astrogildo')
root.iconbitmap('Icone.bmp')

canvas = tk.Canvas(root, bg='black', height=720, width=1350)
canvas.pack()

title = canvas.create_text(675, 0, text='Astrogildo', anchor="n", font='Arial 30', fill='green')


def respond(reply):
    canvas.move('msg', 0, -30)
    msg = canvas.create_text(10, 680, text=reply, anchor="sw", font='Arial 15', fill='green', tags='msg')
    # message_length = len(reply)
    # canvas.create_rectangle(10, 685, (10 + (message_length * 9.5)), 655, fill='gray', tags='msg')
    canvas.tag_raise(msg)


question_box = tk.Entry(root, width=1250, bg='gray', fg='green', font='Arial 15')
question_box.pack()


def sendQuestion(event):
    canvas.move('msg', 0, -30)
    msg = canvas.create_text(1340, 680, text=question_box.get(), anchor="se", font='Arial 15', fill='green', tags='msg')
    # message_length = len(question_box.get())
    # canvas.create_rectangle(1340, 685, (1340 - (message_length * 9.5)), 655, fill='gray', tags='msg')
    canvas.tag_raise(msg)
    simplified_question = (question_box.get()).lower()
    respond(getQuestion(simplified_question))
    question_box.delete(first=0, last=len(question_box.get()))


root.bind('<Return>', sendQuestion)

root.mainloop()
