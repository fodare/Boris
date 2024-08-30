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

APP_WINDOW_WIDTH = os.getenv('APP_WINDOW_WIDTH') if os.getenv(
    'APP_WINDOW_WIDTH') is None else 1000
APP_WINDOW_HEIGHT = os.getenv('APP_WINDOW_HEIGHT') if os.getenv(
    'APP_WINDOW_HEIGHT') is None else 700
APP_THEME_NAME = os.getenv('APP_THEME_NAME') if os.getenv(
    'APP_THEME_NAME') is None else "Darkly"
APP_TITLE = os.getenv('APP_TITLE') if os.getenv(
    'APP_TITLE') is None else "Boris"


class App(_tk.Tk):
    def __init__(self):
        super().__init__()

        # ----------- App Window config -----------#
        self.title(APP_TITLE)
        self.geometry(f"{APP_WINDOW_WIDTH}x{APP_WINDOW_HEIGHT}")
        self.resizable(width=False, height=False)

        # ----------- Init DB config -----------#
        self.dbLogic = dbLogic.DBLogic()

        # ----------- Sub frames -----------#
        self.login_frame = LoginView(self)
        self.login_frame.pack(ipadx=APP_WINDOW_WIDTH, ipady=APP_WINDOW_HEIGHT)

        self.register_frame = RegisterView(self)
        self.register_frame.pack(
            ipadx=APP_WINDOW_WIDTH, ipady=APP_WINDOW_HEIGHT)

        self.content_main_frame = ContentMainFrame(self)
        self.content_main_frame.pack(
            ipadx=APP_WINDOW_WIDTH, ipady=APP_WINDOW_HEIGHT)

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
            parent.register_frame.pack(
                ipadx=APP_WINDOW_WIDTH, ipady=APP_WINDOW_HEIGHT)
            parent.register_frame.render_register_frame(parent)

        def handle_login():
            username = self.username_entry.get()
            password = self.password_entry.get()
            try:
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
                parent.content_main_frame.pack(
                    ipadx=APP_WINDOW_WIDTH, ipady=APP_WINDOW_HEIGHT)
                parent.content_main_frame.render_contnet_view(parent)
            except Exception as err:
                messagebox.showerror(
                    title="Error", message=f"Error signing in!. Exception \n{err}")

                # ------------ Widgets ------------ #
        self.view_label = ttk.Label(self.contnet_frame, text="Login", font=(
            "monospace", 35)).grid(row=0, column=0, pady=70, columnspan=2)

        self.username_label = ttk.Label(
            self.contnet_frame, text="Username:", font=("monospace", 20)).grid(row=1, column=0, ipady=20)
        self.username_entry = ttk.Entry(self.contnet_frame, width=27)
        self.username_entry.focus()
        self.username_entry.grid(
            row=1, column=1, columnspan=1)

        self.password_label = ttk.Label(
            self.contnet_frame, text="Password:", font=("monospace", 20)).grid(row=2, column=0)
        self.password_entry = ttk.Entry(self.contnet_frame, width=27)
        self.password_entry.grid(
            row=2, column=1, columnspan=1)

        self.login_button = ttk.Button(
            self.contnet_frame, text="Login", width=11, command=handle_login).grid(row=3, column=0, pady=20,  rowspan=2)
        self.register_button = ttk.Button(self.contnet_frame, text="Register", width=11,
                                          command=handle_register_view).grid(
            row=3, column=1, pady=20, rowspan=2)
        self.tkraise()


class RegisterView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.content_frame = ttk.Frame(self)
        self.content_frame.pack()

    def render_register_frame(self, parent):
        # ------------ Button functions ------------ #
        def handle_login_view():
            parent.register_frame.pack_forget()
            parent.content_main_frame.pack_forget()
            parent.login_frame.pack(
                ipadx=APP_WINDOW_WIDTH, ipady=APP_WINDOW_HEIGHT)

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
        self.view_label = ttk.Label(
            self.content_frame, text="Register", font=("monospace", 35)).grid(row=0, column=0, pady=70, columnspan=2)

        self.username_label = ttk.Label(
            self.content_frame, text="Username:", font=("monospace", 20)).grid(row=1, column=0, ipady=20)
        self.username_entry = ttk.Entry(self.content_frame, width=27)
        self.username_entry.focus()
        self.username_entry.grid(
            row=1, column=1, columnspan=1)

        self.password_label = ttk.Label(
            self.content_frame, text="Password:", font=("monospace", 20)).grid(row=2, column=0)
        self.password_entry = ttk.Entry(self.content_frame, width=27)
        self.password_entry.grid(row=2, column=1, columnspan=1)

        self.cancel_button = ttk.Button(
            self.content_frame, text="Cancel", width=11, command=handle_login_view).grid(row=3, column=0, pady=20,  rowspan=2)
        self.register_button = ttk.Button(
            self.content_frame, text="Register", width=11, command=handle_register).grid(row=3, column=1, pady=20, rowspan=2)

        self.tkraise()


class ContentMainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.notebook = ttk.Notebook(self)

    def render_contnet_view(self, parent):

        # View Tabs / SUb windows
        password_tab = ttk.Frame(self.notebook)
        finances_tab = ttk.Frame(self.notebook)

        # Sub frames and views
        password_frame = PasswordContnet(password_tab)
        finance_frame = FinanceContent(finances_tab)

        password_frame.configure(relief="groove", border=5)
        password_frame.pack(fill="both", ipady=APP_WINDOW_HEIGHT)

        finance_frame.configure(relief="groove", border=5)
        finance_frame.pack(fill="both", ipady=APP_WINDOW_HEIGHT)

        # Render tabs
        self.notebook.add(password_tab, text="Passwords")
        self.notebook.add(finances_tab, text="Finances")

        self.notebook.configure(width=APP_WINDOW_WIDTH,
                                height=APP_WINDOW_HEIGHT)
        self.notebook.pack(fill="both")


class PasswordContnet(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.password_logic = PasswordLogic()

        # Frames /  View layout
        self.form_frame = ttk.Frame(self)
        self.form_frame.configure(relief="groove")
        self.form_frame.pack(side="left", fill="y")

        self.table_frame = ttk.Frame(self)
        self.table_frame.configure(relief='groove')
        self.table_frame.pack(side="left", fill="both")

        # Functions
        def handle_add_password():
            account = self.account_entry.get()
            username = self.username_entry.get()
            password = self.password_entry.get()
            link = self.link_entry.get()
            note = html.unescape(self.note_entry.get("1.0", _tk.END))

            password_saved = self.password_logic.record_password(
                account, username, password, link, note)
            if password_saved:
                messagebox.showinfo(
                    title="Success", message="Password saved successfully!")
                reset_form_entries()
                self.tree_entries = self.password_logic.get_passwords()
                update_table_entries()
            else:
                messagebox.showerror(
                    title="Error", message="Error saving password. Please try again!")

        def reset_form_entries():
            self.account_entry.delete(0, _tk.END)
            self.username_entry.delete(0, _tk.END)
            self.password_entry.delete(0, _tk.END)
            self.link_entry.delete(0, _tk.END)
            self.note_entry.delete("1.0", _tk.END)

        def handle_password_generation():
            random_password = self.password_logic.generate_password()
            if len(self.password_entry.get()) > 0:
                self.password_entry.delete(0, _tk.END)
            self.password_entry.insert(_tk.END, string=f"{random_password}")
            pyperclip.copy(random_password)

        def handle_password_update():
            selected_item = self.password_tree.item(
                self.password_tree.selection())
            selected_item_info = self.password_logic.get_password(
                selected_item['values'][0])
            user_approve = messagebox.askokcancel(
                title="Caution", message=f"Are you sure you want to update record with account name {selected_item_info['Account']}?")
            if user_approve:
                id = selected_item_info["id"]
                account = self.account_entry.get()
                username = self.username_entry.get()
                password = self.password_entry.get()
                link = self.link_entry.get()
                note = html.unescape(self.note_entry.get("1.0", _tk.END))
                account_updated = self.password_logic.update_password(
                    id, account, username, password, link, note)
                if account_updated:
                    self.tree_entries = self.password_logic.get_passwords()
                    messagebox.showinfo(
                        title="Info", message="Account updated successfully!")
                    reset_form_entries()
                    self.add_button.grid(row=6, column=1, pady=5)
                    self.update_button.grid_forget()
                else:
                    messagebox.showerror(
                        title="Error", message="Error updating account!")
                update_table_entries()

        # Form contnet
        self.view_label = ttk.Label(
            self.form_frame, text="Add Password", font=(40))
        self.view_label.grid(row=0, column=0, pady=10, columnspan=2)

        self.account_label = ttk.Label(self.form_frame, text="Account Name:")
        self.account_label.grid(row=1, column=0, pady=10)

        self.account_entry = ttk.Entry(self.form_frame)
        self.account_entry.grid(row=1, column=1, pady=10)

        self.username_label = ttk.Label(self.form_frame, text="Username:")
        self.username_label.grid(row=2, column=0, pady=10)

        self.username_entry = ttk.Entry(self.form_frame)
        self.username_entry.grid(row=2, column=1, pady=10)

        self.password_label = ttk.Label(self.form_frame, text="Password:")
        self.password_label.grid(row=3, column=0, pady=10)

        self.password_entry = ttk.Entry(self.form_frame)
        self.password_entry.grid(row=3, column=1, pady=10)

        self.link_label = ttk.Label(self.form_frame, text="Log-in Link:")
        self.link_label.grid(row=4, column=0, pady=10)

        self.link_entry = ttk.Entry(self.form_frame)
        self.link_entry.grid(row=4, column=1, pady=10)

        self.note_label = ttk.Label(self.form_frame, text="Notes:")
        self.note_label.grid(row=5, column=0, pady=10)

        self.note_entry = _tk.Text(self.form_frame, height=10, width=20)
        self.note_entry.grid(row=5, column=1, pady=10)

        self.generate_password = ttk.Button(
            self.form_frame, text="Generate", command=handle_password_generation)
        self.generate_password.grid(row=3, column=2)

        self.add_button = ttk.Button(
            self.form_frame, text="Add Password", command=handle_add_password)
        self.add_button.grid(row=6, column=1, pady=5)

        self.update_button = ttk.Button(
            self.form_frame, text="Update", command=handle_password_update)

        # Table contnet
        self.password_tree = ttk.Treeview(self.table_frame, columns=(
            'Account', 'Username', 'Link'), show="headings")
        self.password_tree.heading('Account', text="Account")
        self.password_tree.heading('Username', text="Username")
        self.password_tree.heading('Link', text="Link")
        self.password_tree.pack(expand=True, fill="both", ipadx=100)
        self.tree_entries = self.password_logic.get_passwords()
        for account in self.tree_entries:
            self.password_tree.insert(parent='', index=_tk.END, values=(
                account['Account'], account['Username'], account['LoginLink']))

        def update_table_entries():
            if self.password_tree.get_children() == None:
                self.tree_entries = self.password_logic.get_passwords()
                for account in self.tree_entries:
                    self.password_tree.insert(parent='', index=_tk.END, values=(
                        account['Account'], account['Username'], account['LoginLink']))
            else:
                # Remove old enteries
                for account in self.password_tree.get_children():
                    self.password_tree.delete(account)
                # Re- add new db entries
                for account in self.tree_entries:
                    self.password_tree.insert(parent='', index=_tk.END, values=(
                        account['Account'], account['Username'], account['LoginLink']))

        # Table / Table events binding
        def item_select(_):
            selected_item = self.password_tree.item(
                self.password_tree.selection())

            if selected_item["values"] == "":
                pass
            elif selected_item["values"] is not None:
                selected_item_info = self.password_logic.get_password(
                    selected_item['values'][0])
                reset_form_entries()
                self.account_entry.insert(
                    _tk.END, string=f"{selected_item_info['Account']}")
                self.username_entry.insert(
                    _tk.END, string=f"{selected_item_info['Username']}")
                self.password_entry.insert(
                    _tk.END, string=f"{selected_item_info['Password']}")
                self.link_entry.insert(
                    _tk.END, string=f"{selected_item_info['LoginLink']}")
                self.note_entry.insert(
                    _tk.END, f"{selected_item_info['Note']}")
                self.add_button.grid_forget()
                self.update_button.grid(row=6, column=1)

        def item_delete(_):
            selected_item = self.password_tree.item(
                self.password_tree.selection())
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
                    self.tree_entries = self.password_logic.get_passwords()
                else:
                    messagebox.showerror(
                        title="Error", message="Error deleting account!")
                update_table_entries()

        def item_deselect(_):
            selected_item = self.password_tree.item(
                self.password_tree.selection())

            if selected_item["values"] == "":
                pass
            elif selected_item["values"] is not None:
                _ = self.password_logic.get_password(
                    selected_item['values'][0])
                self.password_tree.selection_remove(
                    self.password_tree.selection())
                reset_form_entries()
                self.update_button.grid_forget()
                self.add_button.grid(row=6, column=1, pady=5)

        self.password_tree.bind('<Double-1>', item_select)
        self.password_tree.bind('<Delete>', item_delete)
        self.password_tree.bind('<Escape>', item_deselect)


class FinanceContent(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label2 = ttk.Label(self, text="Label 2:")
        self.label2.grid(row=0, column=0)

        self.entry1 = ttk.Entry(self)
        self.entry1.grid(row=0, column=1)

        self.button2 = ttk.Button(self, text="Button 2")
        self.button2.grid(row=1, column=1, columnspan=2)
