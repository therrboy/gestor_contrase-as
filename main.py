from tkinter import *
from tkinter import messagebox  # con import * importamos todo menos los modulos de codigo
from random import choice, randint, shuffle
import pyperclip
import json


# Recordar borrar todos los archivos ya creados para evitar un mal funcionamiento
# ---------------------------- PASSWORD GENERATOR    ------------------------------- #
# Boton search

def search_botton():
    website_search = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)  # este metodo es json.load() sirve para leer datos con print
    except FileNotFoundError:
        messagebox.showinfo(title="Opps", message="El sitio no existe")
    else:
        if website_search in data:
            web_elegida = website_search.capitalize()
            cuenta_elegida = data[website_search]["emaill"]
            password_elegido = data[website_search]['passwordd']
            messagebox.showinfo(title="Search data", message=f"Web: {web_elegida}\nCuenta: {cuenta_elegida}\n Password:{password_elegido}")
        else:
            messagebox.showinfo(tittle="Error", message=f"No hay detalles para {website_search}")

# Password Generator Project
def generar_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    var_letras = [choice(letters) for _ in range(randint(8, 10))]  # Usamos _ para no usar una letra
    var_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    var_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    var_password = var_letras + var_numbers + var_symbols
    shuffle(var_password)

    new_password = "".join(var_password)  # El join, junta todas las variables que usamos
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)  # Este modulo pyperclip copia la contraseña que generamos


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Guardar datos sitio WEB, Facebook, Google, Instagram, etc.

# Boton Add

def click_boton_add():
    website = website_entry.get()
    email = datos_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "emaill": email,
            "passwordd": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="No dejes campos vacios")
    else:
        # messagebox tiene varias aplicaciones, en este caso vamos a usarlo para abrir una ventana y contestar si o no
        # is_ok = messagebox.askokcancel(title=website, message=f"Esta es la informacion introducida: \nEmail: {email} \nPassword: {password}"
        #                                                       f"\nEsta bien?")
        try:
            with open("data.json", "r") as data_file:  # Archivo abierto como lectura
                # Leer datos viejos
                data = json.load(data_file)  # este metodo es json.load() sirve para leer datos con print
                # Actualizar datos viejos con datos nuevos
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)  # Actualizamos los datos del diccionario con datos nuevos.

            with open("data.json", "w") as data_file:  # Archivo abierto como escritura
                # Guardamos los datos actualizados
                json.dump(data, data_file, indent=4)  # este metodo es json.dump() sirve para escribir
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Gestor de contraseña")
window.config(padx=40, pady=70, bg="white")  # el tamaño entre la ventana y los widgets

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
imagen_candado = PhotoImage(file="logo.png")  # Con PhotoImage vamos a ubicar el archivo/foto a usar
canvas.create_image(100, 100, image=imagen_candado)  # Ubicar la imagen en el centro.
canvas.grid(column=1, row=0)

# Texto Website y su cuadrado
texto_website = Label(text="Website:", font=("Arial", 15, "bold"), bg="white")
texto_website.grid(row=1, column=0)
# Texto Email/Username y su cuadrado
texto_datos = Label(text="Email/Username:", font=("Arial", 15, "bold"), bg="white")
texto_datos.grid(column=0, row=2)
# Texto Password y su cuadrado. Boton "Generador"
texto_password = Label(text="Password:", font=("Arial", 15, "bold"), bg="white")
texto_password.grid(column=0, row=3)

# Entry
website_entry = Entry(width=39)  # Entry viene del modulo tkinter
website_entry.grid(column=1, row=1)
website_entry.focus()
# Entry
datos_entry = Entry(width=60)  # Entry viene del modulo tkinter
datos_entry.grid(column=1, row=2, columnspan=2)
datos_entry.insert(0, "correoelectronico@hotmail.com")
# Entry
password_entry = Entry(width=39)  # Entre viene del modulo tkinter
password_entry.grid(column=1, row=3)  # sticky = "W" mueve el cuadrado a la izquierda

# Botones

boton_password = Button(text="Password generator", command=generar_password, width=15)
boton_password.grid(column=2, row=3)

boton_add = Button(text="Add", command=click_boton_add, width=51)
boton_add.grid(column=1, row=4, columnspan=2, padx=5, pady=5)

boton_search = Button(text="Search", command=search_botton, width=15)
boton_search.grid(column=2, row=1, columnspan=2, padx=5, pady=5)

window.mainloop()