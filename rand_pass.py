import string
from tkinter import *
import random
import pyperclip 

def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_char = string.punctuation

    all = small_alphabets+capital_alphabets+numbers+special_char
    pass_length = int(length_box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets, pass_length))

    if choice.get()==2:
         passwordField.insert(0,random.sample(small_alphabets+capital_alphabets, pass_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all, pass_length))

def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


root = Tk()
root.config(bg='gray20')
choice = IntVar()
font = ('arial', 13, 'bold')

passwordLabel = Label(root, text= 'Password Generator', font=('times new roman', 20, 'bold'), bg= 'gray20',fg='white')
passwordLabel.grid(pady=10)

weakradiobutton = Radiobutton(root, text='Weak', value=1, variable=choice, font= font)
weakradiobutton.grid(pady=8)

mediumradiobutton = Radiobutton(root, text='Medium', value=2, variable=choice, font= font)
mediumradiobutton.grid(pady=8)

strongradiobutton = Radiobutton(root, text='Strong', value=3, variable=choice, font= font)
strongradiobutton.grid(pady=8)

lengthLabel = Label(root, text= 'Password Length', font= font, bg= 'gray20',fg='white')
lengthLabel.grid(pady=8)

length_box = Spinbox(root, from_=5, to_=18, width=5, font = font)
length_box.grid(pady=8)

generatorButton = Button(root, text='Generator', font=font, command=generator)
generatorButton.grid(pady=8)

passwordField = Entry(root,width=25, bd=2, font=font)
passwordField.grid(pady=8)

copyButton = Button(root, text='Copy', font=font, command=copy)
copyButton.grid(pady=8)

root.mainloop()