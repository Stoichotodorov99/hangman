from tkinter import *
from tkinter import ttk
import random
from PIL import ImageTk, Image

root = Tk()
root.title("hangman")
root.geometry("400x200")
canvas = Canvas(root, width=80, height=80)
canvas.grid(column=1, row=0)
canvas.place(x=220, y=80)
img = (Image.open("1.png"))
resize_img = img.resize((80, 80), Image.ANTIALIAS)
photo_img = ImageTk.PhotoImage(resize_img)
canvas.create_image(10, 10, anchor=NW, image=photo_img)

head = (Image.open("2.png"))
resize_img2 = head.resize((30, 30), Image.ANTIALIAS)
photo_img2 = ImageTk.PhotoImage(resize_img2)

left_arm = (Image.open("3.png"))
resize_img3 = left_arm.resize((20, 20), Image.ANTIALIAS)
photo_img3 = ImageTk.PhotoImage(resize_img3)

right_arm = (Image.open("4.png"))
resize_img4 = right_arm.resize((20, 20), Image.ANTIALIAS)
photo_img4 = ImageTk.PhotoImage(resize_img4)

right_leg = (Image.open("5.png"))
resize_img5 = right_leg.resize((20, 20), Image.ANTIALIAS)
photo_img5 = ImageTk.PhotoImage(resize_img5)

left_leg = (Image.open("6.png"))
resize_img6 = left_leg.resize((20, 20), Image.ANTIALIAS)
photo_img6 = ImageTk.PhotoImage(resize_img6)

eyes = (Image.open("7.png"))
resize_img7 = eyes.resize((7, 7), Image.ANTIALIAS)
photo_img7 = ImageTk.PhotoImage(resize_img7)


text = StringVar()
lose = ttk.Label(root, width=60, textvariable=text, font=70)
text.set("Sorry you fail")

text2 = StringVar()
gain = ttk.Label(root, width=60, textvariable=text2, font=70)
text2.set("Congratulations you won ")

word = "abcdefghijklmnopqrstuvwxyz"
s = []
m = []
mylist = ["random", "tuples", "numbers", "python"]
guess_word = random.choice(mylist)

varcolumn = 0
varrow = 0
var = StringVar()

guess_letter = ""
serch_word = ttk.Label(root, width=10, textvariable=var)
serch_word.grid(column=1, row=0)
serch_word.place(x=100, y=120)
attempts = 6
let = ""
win = 2
for d in range(len(guess_word)):

    if d == 0:
        guess_letter += guess_word[d]
        let += guess_word[d]

    elif d == (len(guess_word) - 1):
        guess_letter += guess_word[d]
        let += guess_word[d]

    else:
        guess_letter += "_ "

var.set(guess_letter)

for i in word:
    s.append(i)


def check(x):
    global attempts
    global let
    global win

    guess_letter = ""

    p = 0

    for i in s:
        if i == x:
            if x in guess_word and x not in let:
                win += 1
                print(win)

                pass
            else:

                attempts -= 1
            m[p]['state'] = DISABLED

            let += i
            for letter in guess_word:
                if letter in let:
                    guess_letter += letter

                else:
                    guess_letter += "_ "

                var.set(guess_letter)

        p += 1
    if attempts == 5:
        canvas.create_image(55, 22, anchor=NW, image=photo_img2)

    elif attempts == 4:
        canvas.create_image(60, 30, anchor=NW, image=photo_img3)

    elif attempts == 3:
        canvas.create_image(62, 29, anchor=NW, image=photo_img4)

    elif attempts == 2:
        canvas.create_image(62, 35, anchor=NW, image=photo_img5)

    elif attempts == 1:
        canvas.create_image(60, 35, anchor=NW, image=photo_img6)

    elif attempts == 0 and win != len(guess_word):
        canvas.create_image(67, 24, anchor=NW, image=photo_img7)
        lose.grid(column=1, row=0)
        lose.place(x=165, y=160)

    if win == len(guess_word) and attempts > 0:
        print("yes")
        gain.grid(column=1, row=0)
        gain.place(x=165, y=160)

for varrow in range(1):

    for name in s:

        if name == "j":

            name = ttk.Button(root, text=name, width=5, command=lambda x=name: check(str(x)))
            name.grid(column=varcolumn, row=varrow)
            varrow += 1
            m.append(name)
            varcolumn -= 9

        elif name == "t":
            name = ttk.Button(root, text=name, width=5, command=lambda x=name: check(str(x)))
            name.grid(column=varcolumn, row=varrow)
            varrow += 1
            m.append(name)
            varcolumn -= 9

        else:
            name = ttk.Button(root, text=name, width=5, command=lambda x=name: check(str(x)))
            name.grid(column=varcolumn, row=varrow)
            varcolumn += 1
            m.append(name)

root.mainloop()
