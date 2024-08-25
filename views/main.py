import tkinter as _tk
from tkinter import messagebox
from tkinter import ttk
from Data import dbLogic
from Utilities.passwordlogic import PasswordLogic
import pyperclip
import html
from dotenv import load_dotenv
import os

load_dotenv()


class App(_tk.Tk):
    def __init__(self):
        super().__init__()

        # ----------- App Window config -----------#
        app_title = os.getenv(key='APP_TITLE', default="Boris")
        self.title(app_title)
        window_width = os.getenv(key='APP_WINDOW_WIDTH', default=800)
        window_height = os.getenv(key='APP_WINDOW_HEIGHT', default=600)
        self.geometry(f"{window_width}x{window_height}")
        self.resizable(width=False, height=False)

        # ----------- Init DB config -----------#
        self.dbLogic = dbLogic.DBLogic()

        # ----------- Sub frames -----------#
        self.login_frame = LoginView(self)
        self.login_frame.pack(ipadx=window_width, ipady=window_height)

        self.register_frame = RegisterView(self)
        self.register_frame.pack(ipadx=window_width, ipady=window_height)

        self.content_main_frame = ContentMainFrame(self)
        self.content_main_frame.pack(ipadx=window_width, ipady=window_height)

        # ----------- Default view -----------#
        self.login_frame.render_login_frame(self)
        self.mainloop()


class LoginView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.contnet_frame = ttk.Frame(self)
        self.contnet_frame.pack()

    def render_login_frame(self, parent):
        # ------------ Button functions ------------ #
        def handle_register_view():
            parent.login_frame.pack_forget()
            parent.register_frame.pack(ipadx=os.getenv(
                'APP_WINDOW_WIDTH'), ipady=os.getenv('APP_WINDOW_HEIGHT'))
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
                parent.login_frame.pack_forget()
                parent.register_frame.pack_forget()
                parent.content_main_frame.pack(ipadx=os.getenv(
                    'APP_WINDOW_WIDTH'), ipady=os.getenv('APP_WINDOW_HEIGHT'))
                parent.content_main_frame.render_contnet_view(parent)

        # ------------ Widgets ------------ #
        self.view_label = _tk.Label(self.contnet_frame, text="Login", font=(
            "monospace", 35)).grid(row=0, column=0, pady=70, columnspan=2)

        self.username_label = _tk.Label(
            self.contnet_frame, text="Username:", font=("monospace", 20)).grid(row=1, column=0, ipady=20)
        self.username_entry = _tk.Entry(self.contnet_frame, width=27)
        self.username_entry.focus()
        self.username_entry.grid(
            row=1, column=1, columnspan=1)

        self.password_label = _tk.Label(
            self.contnet_frame, text="Password:", font=("monospace", 20)).grid(row=2, column=0)
        self.password_entry = _tk.Entry(self.contnet_frame, width=27)
        self.password_entry.grid(
            row=2, column=1, columnspan=1)

        self.login_button = _tk.Button(
            self.contnet_frame, text="Login", width=11, command=handle_login).grid(row=3, column=0, pady=20,  rowspan=2)
        self.register_button = _tk.Button(self.contnet_frame, text="Register", width=11,
                                          command=handle_register_view).grid(
            row=3, column=1, pady=20, rowspan=2)
        self.tkraise()


class RegisterView(_tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.content_frame = ttk.Frame(self)
        self.content_frame.pack()

    def render_register_frame(self, parent):
        # ------------ Button functions ------------ #
        def handle_login_view():
            parent.register_frame.pack_forget()
            parent.content_main_frame.pack_forget()
            parent.login_frame.pack(ipadx=os.getenv(
                'APP_WINDOW_WIDTH'), ipady=os.getenv('APP_WINDOW_HEIGHT'))

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
            self.content_frame, text="Register", font=("monospace", 35)).grid(row=0, column=0, pady=70, columnspan=2)

        self.username_label = _tk.Label(
            self.content_frame, text="Username:", font=("monospace", 20)).grid(row=1, column=0, ipady=20)
        self.username_entry = _tk.Entry(self.content_frame, width=27)
        self.username_entry.focus()
        self.username_entry.grid(
            row=1, column=1, columnspan=1)

        self.password_label = _tk.Label(
            self.content_frame, text="Password:", font=("monospace", 20)).grid(row=2, column=0)
        self.password_entry = _tk.Entry(self.content_frame, width=27)
        self.password_entry.grid(row=2, column=1, columnspan=1)

        self.cancel_button = _tk.Button(
            self.content_frame, text="Cancel", width=11, command=handle_login_view).grid(row=3, column=0, pady=20,  rowspan=2)
        self.register_button = _tk.Button(
            self.content_frame, text="Register", width=11, command=handle_register).grid(row=3, column=1, pady=20, rowspan=2)

        self.tkraise()


class ContentMainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def render_contnet_view(self, parent):
        notebook = ttk.Notebook(self)

        # View Tabs / Windows
        password_tab = ttk.Frame(notebook)
        finances_tab = ttk.Frame(notebook)

        # Sub frames and views
        password_frame = ttk.Frame(password_tab)
        finance_frame = ttk.Frame(finances_tab)

        password_frame.configure(relief="groove", border=5)
        password_frame.pack(fill="both", ipady=os.getenv('APP_WINDOW_HEIGHT'))

        finance_frame.configure(relief="groove", border=5)
        finance_frame.pack(fill="both", ipady=os.getenv('APP_WINDOW_HEIGHT'))

        label_1 = ttk.Label(password_frame, text="Label1")
        label_1.grid(row=0, column=0)
        entry_1 = ttk.Entry(password_frame)
        entry_1.grid(row=0, column=1)

        label_2 = ttk.Label(finance_frame, text="Label 2")
        label_2.grid(row=0, column=0)
        entry_2 = ttk.Entry(finance_frame)
        entry_2.grid(row=0, column=1)

        # Render tabs
        notebook.add(password_tab, text="Passwords")
        notebook.add(finances_tab, text="Finances")

        notebook.configure(width=os.getenv('APP_WINDOW_WIDTH'),
                           height=os.getenv('APP_WINDOW_HEIGHT'))
        notebook.pack(fill="both")

        self.tkraise()
