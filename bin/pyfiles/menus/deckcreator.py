import pygame
import sys
from tkinter import *
from pygame.locals import *


def func():
    print("Button is clicked")

def delete():
    my_listbox.delete(ANCHOR)

def select():
    my_label.config(text=my_listbox.get(ANCHOR))



root = Tk()
root.title('ListTesting')
root.geometry("800x800")

my_listbox = Listbox(root)
my_listbox.pack(pady=150)
#add items to the list box

my_listbox.insert(END, "This is an item")
my_listbox.insert(END, "This is an item")
my_listbox.insert(END, "This is an item")
#adding a list of items
my_list=["One", "Two", "Three"]

for i in my_list:
    my_listbox.insert(END, i)

my_listbox.insert(2, "A new thing")

my_button = Button(root, text="Delete", command=delete)
my_button.pack(pady=10)

my_button2 = Button(root, text="Select", command=select)
my_button2.pack(pady=10)

my_label = Label(root, text='')
my_label.pack(pady=5)


root.mainloop()