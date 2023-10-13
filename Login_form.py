from tkinter import *
from tkinter import messagebox


def login():
    username = entry1.get()
    password = entry2.get()


    success = False

   # if (username == "" and password == ""):
    #    messagebox.showerror("Error", "Blank fields are not allowed")

    #elif (username == "Gad" and password == "admin"):
     #   messagebox.showinfo("Success", "Login Successful")

    #else:
     #   messagebox.showerror("Error", "Incorrect username and password")*/

    file_path = "C:/Users/Dell/Documents/VS Python/users.txt"
    with open(file_path, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                success = True
                break

    if success:
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Incorrect username or password")


root=Tk()
root.title("Login")
root.geometry("300x200")


Label(root,text="Username").place(x=20, y=20)
Label(root,text="Password").place(x=20, y=70)

entry1 = Entry(root,bd=5)
entry1.place(x=140, y=20)

entry2 = Entry(root,bd=5)
entry2.place(x=140, y=70)

Button(root,text = "Login", command = login, height = 3, width = 13, bd = 6).place(x = 100, y = 120)


root.mainloop()