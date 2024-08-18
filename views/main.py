import tkinter as _tk
from tkinter import messagebox
from tkinter import ttk
from Data import dbLogic
from Utilities.passwordlogic import PasswordLogic
import pyperclip
import html


class App(_tk.Tk):
    def __init__(self, title: str, app_geometry: tuple):
        super().__init__()

        # ----------- App Window config -----------#
        self.title(title)
        self.geometry(f"{app_geometry[0]}x{app_geometry[1]}")
        self.resizable(width=False, height=True)

        # ----------- Init DB config -----------#
        self.dbLogic = dbLogic.DBLogic()

        # ----------- Sub frames -----------#
        self.login_frame = LoginView(self)
        self.login_frame.grid(row=0, column=0, padx=100, sticky="nsew")

        self.register_frame = RegisterView(self)
        self.register_frame.grid(row=0, column=0, padx=100, sticky="nsew")

        self.app_mainFrame = AppMainFrame(self)
        self.app_mainFrame.grid(row=0, column=0, sticky="nsew")

        # ----------- Default view -----------#
        self.login_frame.render_login_frame(self)
        self.mainloop()


class LoginView(_tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

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
                parent.app_mainFrame.render_app_main_frame(parent)

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
        self.register_button = _tk.Button(self, text="Register", width=11,
                                          command=handle_register_view).grid(
            row=3, column=1, pady=20, rowspan=2)
        self.tkraise()


class RegisterView(_tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

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


# ------------- App services  ------------- #


class AppMainFrame(_tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def render_app_main_frame(self, parent):
        self.options_menu_frame = OptionsMenuFrame(self)
        self.options_menu_frame.pack()
        self.options_menu_frame.pack_propagate(False)
        self.options_menu_frame.configure(width=600, height=38)

        self.content_frame = ContentFrame(self)
        self.content_frame.pack(fill=_tk.BOTH, expand=True)

        self.tkraise()

# ------------- App services subframe  ------------- #


class OptionsMenuFrame(_tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        def set_options_button_active(name):
            for child in self.winfo_children():
                if name == child.winfo_name():
                    child.configure(background="gray",
                                    highlightthickness=4)
                else:
                    child.configure(background="#d9d9d9", highlightthickness=0)

        def handle_home_view(name):
            set_options_button_active(name)
            parent.content_frame.render_home_view()

        def handle_password_view(name):
            set_options_button_active(name)
            parent.content_frame.render_password_view()

        def handle_finance_view(name):
            set_options_button_active(name)
            parent.content_frame.render_finance_view()

        self.home_button = _tk.Button(
            self, text="Home", name="home", activebackground="gray", command=lambda: handle_home_view("home")).place(x=0, y=0, width=125)
        self.password_button = _tk.Button(
            self, text="Passwords", name="password", activebackground="gray", command=lambda: handle_password_view("password")).place(x=125, y=0, width=125)
        self.finance_button = _tk.Button(
            self, text="Finances", name="finance", activebackground="gray", command=lambda: handle_finance_view("finance")).place(x=250, y=0, width=125)


class ContentFrame(_tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.home_frame = HomeView(self)
        self.password_frame = PasswordView(self)
        self.finance_frame = FinanceView(self)

        self.render_home_view()

    def render_home_view(self):
        self.home_frame.render_home_contnet()

    def render_password_view(self):
        self.password_frame.render_password_contnet()

    def render_finance_view(self):
        self.finance_frame.render_finance_contnet()

# ------------- Views / Services  ------------- #


class HomeView(_tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky="nsew")

    def render_home_contnet(self):
        _tk.Label(self, text="This is the home View!").grid(
            row=0, column=0)
        self.tkraise()


class PasswordView(_tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky="nsew")
        self.password_logic = PasswordLogic()

    def render_password_contnet(self):

        # --------------- Functions --------------- #

        def handle_password_generation():
            random_password = self.password_logic.generate_password()
            if len(password_entry.get()) > 0:
                password_entry.delete(0, _tk.END)
            password_entry.insert(_tk.END, string=f"{random_password}")
            pyperclip.copy(random_password)

        def handle_save_password():
            account = account_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            link = link_entry.get()
            note = html.unescape(note_entry.get("1.0", _tk.END))

            password_saved = self.password_logic.record_password(
                account, username, password, link, note)
            if password_saved:
                messagebox.showinfo(
                    title="Success", message="Password saved successfully!")
                account_entry.delete(0, _tk.END)
                username_entry.delete(0, _tk.END)
                password_entry.delete(0, _tk.END)
                link_entry.delete(0, _tk.END)
                note_entry.delete("1.0", _tk.END)
                self.render_password_contnet()
            else:
                messagebox.showerror(
                    title="Error", message="Error saving password. Please try again!")

        def reset_entries():
            account_entry.delete(0, _tk.END)
            username_entry.delete(0, _tk.END)
            password_entry.delete(0, _tk.END)
            link_entry.delete(0, _tk.END)
            note_entry.delete("1.0", _tk.END)

        def update_password_entry():
            selected_item = table.item(table.selection())
            selected_item_info = self.password_logic.get_password(
                selected_item['values'][0])
            user_approve = messagebox.askokcancel(
                title="Caution", message=f"Are you sure you want to update record with account name {selected_item_info['Account']}?")
            if user_approve:
                id = selected_item_info["id"]
                account = account_entry.get()
                username = username_entry.get()
                password = password_entry.get()
                link = link_entry.get()
                note = html.unescape(note_entry.get("1.0", _tk.END))
                account_updated = self.password_logic.update_password(
                    id, account, username, password, link, note)
                if account_updated:
                    messagebox.showinfo(
                        title="Info", message="Account updated successfully!")
                    self.render_password_contnet()
                else:
                    messagebox.showerror(
                        title="Error", message="Error updating account!")

        # --------------- Password Entry view --------------- #
        password_entry_frame = _tk.Frame(self)
        password_entry_frame.grid(row=0, column=0)
        # ----------- Labels ----------- #

        view_label = _tk.Label(password_entry_frame,
                               text="Password View", font=("monospace", 20))
        view_label.grid(row=0, column=0, pady=10, columnspan=2)

        account_label = _tk.Label(
            password_entry_frame, text="Account name:").grid(row=1, column=0)

        username_label = _tk.Label(
            password_entry_frame, text="Username:").grid(row=2, column=0)

        password_label = _tk.Label(
            password_entry_frame, text="Password:").grid(row=3,  column=0)

        link_label = _tk.Label(password_entry_frame,
                               text="Login Link:").grid(row=4, column=0)

        note = _tk.Label(password_entry_frame,
                         text="Note:").grid(row=5, column=0)

        # ----------- Entries ----------- #

        account_entry = _tk.Entry(password_entry_frame, width=25)
        account_entry.grid(row=1, column=1)

        username_entry = _tk.Entry(password_entry_frame, width=25)
        username_entry.grid(row=2, column=1)

        password_entry = _tk.Entry(password_entry_frame, width=25)
        password_entry.grid(row=3, column=1)

        link_entry = _tk.Entry(password_entry_frame, width=25)
        link_entry.grid(row=4, column=1)

        note_entry = _tk.Text(password_entry_frame, height=3, width=25)
        note_entry.grid(row=5, column=1, columnspan=1)

        # ----------- Buttons ----------- #

        generate_password = _tk.Button(
            password_entry_frame, text="Generate", command=handle_password_generation)
        generate_password.grid(row=3, column=2)

        add_password_button = _tk.Button(
            password_entry_frame, text="Add Password", command=handle_save_password)
        add_password_button.grid(row=6, column=0)

        update_button = _tk.Button(
            password_entry_frame, text="Update", command=update_password_entry)

        # --------------- Password Tree view --------------- #
        password_tree_frame = _tk.Frame(self)
        password_tree_frame.grid(row=1, column=0, columnspan=2)

        table = ttk.Treeview(password_tree_frame, columns=(
            'Account', 'Username', 'Link'), show='headings')
        table.heading('Account', text='Account')
        table.heading('Username', text='Username')
        table.heading('Link', text='Login Link')
        table.pack(fill='both', expand=True)

        entry_list = self.password_logic.get_passwords()
        for account in entry_list:
            table.insert(parent='', index=_tk.END, values=(
                account['Account'], account['Username'], account['LoginLink']))

        # ----------- Tree event ----------- #

        def item_select(_):
            selected_item = table.item(table.selection())
            selected_item_info = self.password_logic.get_password(
                selected_item['values'][0])
            reset_entries()
            account_entry.insert(
                _tk.END, string=f"{selected_item_info['Account']}")
            username_entry.insert(
                _tk.END, string=f"{selected_item_info['Username']}")
            password_entry.insert(
                _tk.END, string=f"{selected_item_info['Password']}")
            link_entry.insert(
                _tk.END, string=f"{selected_item_info['LoginLink']}")
            note_entry.insert(_tk.END, f"{selected_item_info['Note']}")
            add_password_button.grid_forget()
            update_button.grid(row=6, column=0)

        def item_delete(_):
            selected_item = table.item(table.selection())
            selected_item_info = self.password_logic.get_password(
                selected_item['values'][0])
            user_approve = messagebox.askokcancel(
                title="Caution", message=f"Are you sure, you want to delete account with name {selected_item_info['Account']}")
            if user_approve:
                password_deleted = self.password_logic.delete_password(
                    selected_item_info['id'])
                if password_deleted:
                    messagebox.showinfo(
                        title="Info", message="Account deleted successfully!")
                    self.render_password_contnet()
                else:
                    messagebox.showerror(
                        title="Error", message="Error deleting account!")

        table.bind('<<TreeviewSelect>>', item_select)
        table.bind('<Delete>', item_delete)

        # Render Password view
        self.tkraise()


class FinanceView(_tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky="nsew")

    def render_finance_contnet(self):
        _tk.Label(self, text="This is the finance view!").grid(row=0, column=0)
        self.tkraise()
