from tkinter import *
from sys import platform

window = Tk()
window.wm_title("Website Blocker")
hosts_path = " "
redirect = "127.0.0.1"

if platform == "linux" or platform == "linux1":
    hosts_path = "/etc/hosts"
elif platform == "win32":
    hosts_path = "C:\Windows\System32\drivers\etc\hosts"

def block_process(websites_list):
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for websites in websites_list:
            if websites in content:
                pass
            else:
                file.write(redirect + " " + websites + '\n')


def unblock_process(websites_list):
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites_list):
                file.write(line)
                file.truncate()

def block():
    block_process([window_text.get()])
    list1.insert(1, "Website Blocked!!")


def unblock():
    unblock_process([window_text.get()])
    list1.insert(1,"Website Unblocked!!")


l1 = Label(window, text="Website To Block")
l1.grid(row=0, column=0)

window_text = StringVar()
e1 = Entry(window, textvariable=window_text)
e1.grid(row=0, column=1)

b1 = Button(window, text="Block", width=12, command=block)
b1.grid(row=2, column=3)

b2 = Button(window, text="Close", width=12, command=window.destroy)
b2.grid(row=4, column=3)

b3 = Button(window, text="Unblock", width=12, command=unblock)
b3.grid(row=3, column=3)

list1=Listbox(window, height=2,width=20)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

window.mainloop()
