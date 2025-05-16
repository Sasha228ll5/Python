import tkinter as tk
from tkinter import messagebox


CORRECT_PASSWORD = "1234"

def check_password():

    entered_password = password_entry.get()
    if entered_password == CORRECT_PASSWORD:
        root.destroy()
    else:
        messagebox.showerror("Error", "Incorrect Password")


root = tk.Tk()
root.title("Screen Locked")
root.attributes("-fullscreen", True)
root.configure(bg="black")


label = tk.Label(root, text="Your screen has been locked.\nEnter the password to unlock:",
                 font=("Helvetica", 24), fg="white", bg="black")
label.pack(pady=20)


password_entry = tk.Entry(root, show="*", font=("Helvetica", 18))
password_entry.pack(pady=10)


unlock_button = tk.Button(root, text="Unlock", font=("Helvetica", 18), command=check_password)
unlock_button.pack(pady=20)


root.bind("<Alt-Tab>", lambda e: "break")
root.bind("<Control-Escape>", lambda e: "break")
root.protocol("WM_DELETE_WINDOW", lambda: None)


root.mainloop()