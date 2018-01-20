#-*- coding:utf8 -*-
import tkinter as tk
from password_generator import generate_password, DEFAULT_SYMBOLS

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.winfo_toplevel().title("Password Generator")

        self.password_length_label = tk.Label(self)
        self.password_length_label["text"] = "Length:"
        self.password_length_label.grid(column=0, row=0)
        self.password_length_entry = tk.Entry(self, width=40)
        self.password_length_entry.insert(0, "10")
        self.password_length_entry.grid(column=1, row=0)

        self.symbol_label = tk.Label(self)
        self.symbol_label["text"] = "Symbols:"
        self.symbol_label.grid(column=0, row=1)
        self.symbol_entry = tk.Entry(self, width=40)
        self.symbol_entry.insert(0, DEFAULT_SYMBOLS)
        self.symbol_entry.grid(column=1, row=1)

        self.generated_password_label = tk.Label(self)
        self.generated_password_label["text"] = "Password:"
        self.generated_password_label.grid(column=0, row=2)
        self.result = tk.Entry(self, width=40, state="readonly")
        self.result.readonly = True
        self.result.grid(column=1, row=2)

        self.quit = tk.Button(self, text="Generate", command=self.generate_button_clicked)
        self.quit.grid(column=0, row=3, columnspan=2)
    
    def generate_button_clicked(self):
        # Get generate options from Form
        password_length_str = self.password_length_entry.get()
        symbols = self.symbol_entry.get()

        try:
            password_length = int(password_length_str)
        except ValueError as err:
            self.set_result("length must be number")
            return

        # Generate password
        try:
            password = generate_password(password_length, symbols)
            self.set_result(password)
        except ValueError as err:
            self.set_result(str(err))
    
    def set_result(self, text):
        self.result.configure(state="normal")
        self.result.delete(0, tk.END)
        self.result.insert(0, text)
        self.result.configure(state="readonly")


root = tk.Tk()
app = Application(master=root)
app.mainloop()