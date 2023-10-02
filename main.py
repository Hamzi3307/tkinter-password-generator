from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    ltr_password = [random.choice(letters) for _ in range(random.randint(8,10))]
    num_password = [random.choice(numbers) for _ in range(random.randint(2,4))]
    sym_password = [random.choice(symbols) for _ in range(random.randint(2,4))]
    
    list_password = ltr_password + num_password + sym_password
    random.shuffle(list_password)
    
    str_password = "".join(list_password)
    # print(str_password,"\n", list_password)
    password_entry.delete(0,END)
    password_entry.insert(0,str_password)
    pyperclip.copy(str_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_file():
    web = web_entry.get()
    mail = mail_entry.get()
    password = password_entry.get()
    if len(password) <= 6  and len(web) <= 0:
        messagebox.showwarning(title="Not Enough Info", message="Please Provide Suffocient Information")
        return
    is_ok = messagebox.askokcancel(title=web, message=f"for the mentioned website \n Email= {mail}\nPassword= {password}\n Is it ok ?")
    if is_ok:
        with open("F:\Python\Tkinter Games\\tkinter-password-generator\passwords.txt", "a") as file:
            file.write(f"{web} | {mail} | {password}\n")
        # print(len(password))
        # print(mail)
        web_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200,height=200)
img = PhotoImage(file="F:\Python\Tkinter Games\\tkinter-password-generator\logo.png")
canvas.create_image(100,100, image=img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

mail_label = Label(text="Email/Username:")
mail_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

web_entry =Entry(width=44)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)

mail_entry =Entry(width=44)
mail_entry.insert(index=END, string="hamzi3307@gmail.com")
mail_entry.grid(row=2, column=1, columnspan=2)

password_entry =Entry(width=25)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_file)
add_button.grid(row=4,column=1, columnspan=2)

window.mainloop()