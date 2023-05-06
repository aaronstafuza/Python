from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))] #random.choice / random.randint
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password) #sirve para copiar directamente sin tener que seleccionar todo con el mouse. 
    #una vez que apreto Generate Password puedo copiarla directamente. 

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(): #Esta funcion de save va a escribir en un archivo que se llama data.txt

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0: #Si no se ingresa el nombre de la web o la password genera un error.
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        #MessageBox genera un popup. 
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        #genera un popup que pregunta si los datos ingresados son correctos, y si ponemos que si los agrega, 
        if is_ok:
            with open("data.txt", "a") as data_file: #abre el archivo y "a" va agregando en ese archivo (append)
                data_file.write(f"{website} | {email} | {password}\n") #La manera en que va a escribir en el archivo
                website_entry.delete(0, END)
                    #Delete (delete(first, last=None)): first: start of range | last: Optional end of range. If omitted, only a single character is removed. 
                    #Me borra lo que pongo como data, es decir una vez que carga el archivo borra del entry. 
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "stafuzaa@gmail.com") #para que siemore que se inicie quede puesto el mail, asi no hay que ponerlo siempre que guardemos una contraseña con ese mail. 
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()