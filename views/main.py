import tkinter as _tk
from tkinter import messagebox
from Data import dbLogic


class App(_tk.Tk):
    def __init__(self, title: str, app_geometry: tuple):
        super().__init__()
        self.title(title)
        self.geometry(f"{app_geometry[0]}x{app_geometry[1]}")
        self.resizable(width=False, height=True)
        self.dbLogic = dbLogic.DBLogic()

        self.login_frame = LoginView(parent=self)

        # self.login_frame.pack_propagate(False)

        self.register_frame = RegisterView(self)

        # self.register_frame.pack_propagate(False)

        self.login_frame.render_login_frame(self)

        self.mainloop()


class LoginView(_tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, padx=100, sticky="nsew")

    def render_login_frame(self, parent):

        # ------------ Button functions ------------ #

        def handle_register_view():
            parent.register_frame.render_register_frame(parent)

        def handle_login():
            username = self.username_entry.get()
            password = self.password_entry.get()
            queried_account = parent.dbLogic.get_app_user(username)
            if queried_account is None:
                messagebox.showerror(
                    title="Error!", message="\nError loging in.\n \nInvalid credentials!")
            elif queried_account["Password"] != password:
                messagebox.showerror(
                    title="Error!", message="\nError loging in.\n \nInvalid credentials!")
            else:
                messagebox.showinfo(
                    title="Success!", message="Successfully logged in!")

        # ------------ Widgets ------------ #
        self.view_label = _tk.Label(self, text="Login", font=(
            "monospace", 35)).grid(row=0, column=0, pady=70, columnspan=2)

        self.username_label = _tk.Label(
            self, text="Username:", font=("monospace", 20)).grid(row=1, column=0, ipady=20)
        self.username_entry = _tk.Entry(self, width=27)
        self.username_entry.focus()
        self.username_entry.grid(
            row=1, column=1, columnspan=1)

        self.password_label = _tk.Label(
            self, text="Password:", font=("monospace", 20)).grid(row=2, column=0)
        self.password_entry = _tk.Entry(self, width=27)
        self.password_entry.grid(
            row=2, column=1, columnspan=1)

        self.login_button = _tk.Button(
            self, text="Login", width=11, command=handle_login).grid(row=3, column=0, pady=20,  rowspan=2)
        self.register_button = _tk.Button(self, text="Register", width=11, command=handle_register_view).grid(
            row=3, column=1, pady=20, rowspan=2)
        self.tkraise()


class RegisterView(_tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, padx=100, sticky="nsew")

    def render_register_frame(self, parent):

        # ------------ Button functions ------------ #

        def handle_login_view():
            parent.login_frame.render_login_frame(parent)

        def handle_register():
            username = self.username_entry.get()
            password = self.password_entry.get()
            account_created = parent.dbLogic.add_app_user(username, password)
            if account_created:
                messagebox.showinfo(
                    title="Info!", message="\n Account created successfully!")
                handle_login_view()
            else:
                messagebox.showerror(
                    title="Error!", message="\nError creating account. \nMaybe try with another credentials!")

        # ------------ Widgets ------------ #
        self.view_label = _tk.Label(
            self, text="Register", font=("monospace", 35)).grid(row=0, column=0, pady=70, columnspan=2)

        self.username_label = _tk.Label(
            self, text="Username:", font=("monospace", 20)).grid(row=1, column=0, ipady=20)
        self.username_entry = _tk.Entry(self, width=27)
        self.username_entry.focus()
        self.username_entry.grid(
            row=1, column=1, columnspan=1)

        self.password_label = _tk.Label(
            self, text="Password:", font=("monospace", 20)).grid(row=2, column=0)
        self.password_entry = _tk.Entry(self, width=27)
        self.password_entry.grid(row=2, column=1, columnspan=1)

        self.cnacel_button = _tk.Button(
            self, text="Cancel", width=11, command=handle_login_view).grid(row=3, column=0, pady=20,  rowspan=2)
        self.register_button = _tk.Button(
            self, text="Register", width=11, command=handle_register).grid(row=3, column=1, pady=20, rowspan=2)

        self.tkraise()
