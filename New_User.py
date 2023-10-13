from tkinter import *
from tkinter import messagebox


def sign_up():
    username = entry1.get()
    password = entry2.get()


    if username and password:
        file_path = "C:/Users/Dell/Documents/VS Python/users.txt"
        with open(file_path, "a") as file:
            file.write(f"{username}:{password}\n")
        messagebox.showinfo("Success", "Registration Successful")

    else:
        messagebox.showerror("Error", "Both fields are required")


root=Tk()
root.title("Create Account")
root.geometry("300x200")


Label(root,text="Username").place(x=20, y=20)
Label(root,text="Password").place(x=20, y=70)

entry1 = Entry(root,bd=5)
entry1.place(x=140, y=20)

entry2 = Entry(root,bd=5)
entry2.place(x=140, y=70)

Button(root,text = "Sign Up", command = sign_up, height = 3, width = 13, bd = 6).place(x = 100, y = 120)


root.mainloop()