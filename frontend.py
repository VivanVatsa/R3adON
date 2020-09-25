from tkinter import *
import backend


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0,END)
    for row in backend.search(title_next.get(), author_text.get(), year_next.get(), isbn_next.get()):
        list1.insert(END, row)
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

# you need a scroll bar too
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search ENtry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

window.mainloop()
