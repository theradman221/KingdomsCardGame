import pygame
import sys
from tkinter import *

from pygame.locals import *


def func():
    print("Button is clicked")

def delete1():
    my_listbox.delete(ANCHOR)


def delete2():
    my_listbox2.delete(ANCHOR)

def select():
    my_label.config(text=my_listbox.get(ANCHOR))

def deckBuilder():

    root = Tk()
    root.title('ListTesting')
    root.geometry("800x800")

    my_listbox = Listbox(root, height=25 )
    my_listbox.pack(side=LEFT,padx=25)

    my_listbox2 = Listbox(root, height=25)
    my_listbox2.pack(side=RIGHT,padx=25)


    for i in range(0,51):
        my_listbox2.insert(END,"Card "+str( i))

    #add items to the list box

    my_listbox.insert(END, "This is an item")
    my_listbox.insert(END, "This is an item")
    my_listbox.insert(END, "This is an item")
    #adding a list of items
    my_list=["One", "Two", "Three"]

    for i in my_list:
        my_listbox.insert(END, i)

    my_listbox.insert(2, "A new thing")

    my_button = Button(root, text="Delete", command=delete1)
    my_button.pack(side=BOTTOM,pady=10)

    my_button2 = Button(root, text="Select", command=select)
    my_button2.pack(side=BOTTOM, pady=10)

    my_label = Label(root, text='')
    my_label.pack(side=BOTTOM,pady=5)


    root.mainloop()
