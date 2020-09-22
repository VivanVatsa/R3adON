from tkinter import *

window = Tk()

# for the labels title author etc
l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

# this is for the space provided to enter and perform operations
title_next = StringVar()
e1 = Entry(window, textvariable=title_next)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_next = StringVar()
e3 = Entry(window, textvariable=year_next)
e3.grid(row=1, column=1)

isbn_next = StringVar()
e4 = Entry(window, textvariable=isbn_next)
e4.grid(row=1, column=3)


# this is to create the display part of display the list
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
window.mainloop()
