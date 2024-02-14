import tkinter as tk
import random

class PasswordGenerator():
    def __init__(self):
        self.caracteres = "$#?*%ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
        self.window = tk.Tk()
        self.window.geometry("1280x740")
        self.window.configure(background="black")
        self.window.title("PasswordGenerator")
        self.title = tk.Label(self.window, fg="white", font=("VT323", 48), text="PASSWORD-GENERATOR", bg="black")
        self.title.pack()
        self.title.place(x=400, y=80)
        self.ask = tk.Label(self.window, bg="black", fg="white", font=("VT323", 30), text="Elige la cantidad de carácteres de tu contraseña: ")
        self.ask.pack()
        self.ask.place(x=200, y=270)
        self.entry = tk.Entry(self.window, width=50, font=("VT323", 30))
        self.entry.pack()
        self.entry.place(x=200, y=400)
        self.btn = tk.Button(
            self.window,
            text="Crear contraseña",
            font=("VT323", 30), 
            fg="white",
            bg="green",
            command=self.createPassword
        )
        self.btn.pack()
        self.btn.place(x=450, y=500)
        self.window.mainloop()

    def createPassword(self):
        self.password = ""
        get_int = int(self.entry.get())

        for i in range(get_int):
            x = random.choice(self.caracteres)
            self.password += x
        
        self.text = tk.Label(
            self.window,
            text=f"Su contraseña creada es: {self.password}",
            font=("VT323", 25),
            fg="white",
            bg="black"
        )

        self.text.pack()
        self.text.place(x=100, y=630)
    
        self.entry.delete(0, 'end')

if __name__ == "__main__":
    pg = PasswordGenerator()