# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
from tkinter.ttk import Label, Style

from tkinter import *

# import filedialog module
from tkinter import filedialog

from tkinter import *
import os


# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()

# Function for opening the
# file explorer window

global abc

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="//",title="Select a File",filetypes=(("Text files",".jpg"),("all files",".")))
    global abc
    abc = str(filename)
    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)


# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,text="File Explorer using Tkinter",width=100, height=4,fg="blue")

button_explore = Button(window,text="Browse Files",command=browseFiles)

button_exit = Button(window,text="Exit")

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

button_exit.grid(column=1, row=3)

# Let the window wait for any events
window.mainloop()
#abc.replace("/","//")
print(abc)
image = cv2.imread(abc)

print("The type of this input is {}".format(type(image)))
print("Shape: {}".format(image.shape))
plt.imshow(image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')

resized_image = cv2.resize(image, (1200, 600))
plt.imshow(resized_image)


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def get_colors(image, number_of_colors, show_chart):
    modified_image = cv2.resize(image, (600, 400), interpolation=cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0] * modified_image.shape[1], 3)

    clf = KMeans(n_clusters=number_of_colors)
    labels = clf.fit_predict(modified_image)

    counts = Counter(labels)
    # sort to ensure correct color percentage
    counts = dict(sorted(counts.items()))

    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]
    print(hex_colors)
    col = ['#f3f2f0', '#f4f3f1', ' #f5f4f3', ' #f6f5f4', ' #f7f7f6', ' #f9f8f7', ' #faf9f9', ' #fbfbfa', ' #fcfcfc',
           '#fdfdfd', ' #ffffff', ' #f0f3f2', '#f2f0f3', '#f9f6f2', ' #f9f6f3', ' #faf7f4', '#faf8f5', ' #fbf9f7',
           '#fcfaf8', '#fcfbf9', '#fdfcfb', ' #fdfdfc', '#fefefd', ' #faf7f4 ', ' #faf8f5', ' #fbf9f7', ' #fcfaf8',
           ' #fcfbf9', ' #fdfcfb', ' #fdfdfc', ' #fefefd', ' #fffafa', ' #fffbfb',
           ' #fffcfc', ' #fffdfd', '#fffefe', '#fefffe', '#fefeff', '#fffffe', '#fffeff','#cccfde','#e7e9ee']
    col = set(col)

    flag = 0


    for i in hex_colors:
        if i in col:
           # print("**NO DEFICIENCY**")
            #text = Label(self, text="No deficiency")
            #text.place(x=70, y=90)
            flag = 1
            break

    def printSomething(a):
        # if you want the button to disappear:
        # button.destroy() or button.pack_forget()
        if a== 1:
            lable=Label(root, text="**No Deficiency**")
            lable.config(font=('Arial',44))
            lable.pack(pady=100)
            #self.style.configure("My.TLabel", font=('Arial', 25))

        else:
            lable = Label(root, text="**VITAMIN D DEFICIENCY**")
            lable.config(font=('Arial', 27))
            lable.pack(pady=60)
            lable1 = Label(root, text="\nSuggested Nutritions \n\nRed meat \nOily Fish Salmon \nsardines \nEgg yolks \nBreakfast cereals")
            lable1.config(font=('Arial', 15))
            lable1.pack(pady=80)

    root = Tk()
    root.title("Vita_Report")
    root.geometry("500x500")

    printSomething(flag)

    root.mainloop()

        # this creates a new label to the GUI
    label.pack()

    root = Tk()

    button = Button(root, text="Report", command=printSomething)
    button.pack()
    root.mainloop()


    if flag == 0:
        print("***Vitamin D Deficiency****")
        #text = Label(self, text="D deficiency")
        #text.place(x=70, y=90)

    if (show_chart):
        plt.figure(figsize=(8, 6))
        plt.pie(counts.values(), labels=hex_colors, colors=hex_colors)

    return rgb_colors


#get_colors(get_image('EYE.jpg'), 15, True)
get_colors(get_image(abc), 10, True)
#get_colors(get_image("N_EYE.jpg"), 10, True)
