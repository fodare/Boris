import tkinter as _tk
from tkinter import messagebox
from tkinter import ttk
from Data import dbLogic
from Utilities.passwordlogic import PasswordLogic
from Utilities.transactionlogic import TransactionLogic
import pyperclip
import html
from dotenv import load_dotenv
import os
from ttkthemes import ThemedTk

load_dotenv()

APP_WINDOW_WIDTH = os.getenv('APP_WINDOW_WIDTH')
APP_WINDOW_HEIGHT = os.getenv('APP_WINDOW_HEIGHT')
APP_THEME_NAME = os.getenv('APP_THEME_NAME')
APP_TITLE = os.getenv('APP_TITLE')
APP_THEME_NAME = os.getenv('APP_THEME_NAME')


class App(ThemedTk):
    def __init__(self):
        super().__init__()
        self.set_theme(APP_THEME_NAME)

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
        self.password_logic = PasswordLogic()

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
            if username == "" or password == "":
                messagebox.showerror(
                    title="Error", message="Username / Password can not be empty!")
            else:
                try:
                    queried_account = parent.dbLogic.get_app_user(username)
                    if queried_account is None:
                        messagebox.showerror(
                            title="Error!", message="\nError loging in.\n \nInvalid credentials!")
                    elif self.password_logic.decrypt_message(queried_account["Password"]) != password:
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
                        title="Error", message=f"Error verifying credentials. Please try again!")

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
        self.password_logic = PasswordLogic()

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
            if username == "" or password == "":
                messagebox.showerror(
                    title="Error", message="Username / Password can not be null!")
            else:
                try:
                    parsed_password = self.password_logic.encrypt_message(
                        password)
                    account_created = parent.dbLogic.add_app_user(
                        username, parsed_password)
                    if account_created:
                        messagebox.showinfo(
                            title="Info!", message="\n Account created successfully!")
                        handle_login_view()
                    else:
                        messagebox.showerror(
                            title="Error!", message="\nError creating account. \nMaybe try with another credentials!")
                except Exception as err:
                    messagebox.showerror(
                        title="Error!", message=f"Unhandled exception while creating account!")

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
        password_frame.configure(relief="groove", border=5)
        password_frame.pack(fill="both", ipady=APP_WINDOW_HEIGHT)

        finance_frame = FinanceContent(finances_tab)
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
        self.table_frame.pack(side="left", fill="both", expand=True)

        # Functions
        def handle_add_password():
            account = self.account_entry.get()
            username = self.username_entry.get()
            password = self.password_entry.get()
            link = self.link_entry.get()
            note = html.unescape(self.note_entry.get("1.0", _tk.END))

            if account == "":
                messagebox.showerror(
                    title="Error", message="Error saving password. Account name can not be empty!")
            else:
                parsed_password = self.password_logic.encrypt_message(
                    password)
                password_saved = self.password_logic.record_password(
                    account, username, parsed_password, link, note)
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
            self.cancel_button.grid_forget()
            self.update_button.grid_forget()
            self.add_button.grid(row=6, column=1, pady=5)

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
                password = self.password_logic.encrypt_message(
                    self.password_entry.get())
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

        def handle_account_search():
            account_name = self.account_entry.get()
            if account_name is None or account_name == "":
                messagebox.showerror(
                    title="Error!", message="Account name can not be null!")
                reset_form_entries()
            else:
                account_info = self.password_logic.get_password(account_name)
                if account_info is None:
                    messagebox.showerror(
                        title="Error", message=f'Can not find account with name {account_name}!')
                    reset_form_entries()
                else:
                    reset_form_entries()
                    self.account_entry.insert(
                        _tk.END, string=f"{account_info['Account']}")
                    self.username_entry.insert(
                        _tk.END, string=f"{account_info['Username']}")
                    self.password_entry.insert(
                        _tk.END, string=f"{self.password_logic.decrypt_message(account_info['Password'])}")
                    self.link_entry.insert(
                        _tk.END, string=f"{account_info['LoginLink']}")
                    self.note_entry.insert(
                        _tk.END, f"{account_info['Note']}")
                    self.add_button.grid_forget()
                    self.cancel_button.grid(row=6, column=1)

        # Form contnet
        self.view_label = ttk.Label(
            self.form_frame, text="Add Password", font=(40))
        self.view_label.grid(row=0, column=0, pady=10, columnspan=2)

        self.account_label = ttk.Label(self.form_frame, text="Account Name:")
        self.account_label.grid(row=1, column=0, pady=10)

        self.account_entry = ttk.Entry(self.form_frame)
        self.account_entry.grid(row=1, column=1, pady=10)

        self.account_search_button = ttk.Button(
            self.form_frame, text="Search", command=handle_account_search)
        self.account_search_button.grid(row=1, column=2)

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

        self.note_entry = _tk.Text(self.form_frame, height=20, width=31)
        self.note_entry.grid(row=5, column=1, columnspan=2, pady=5)

        self.generate_password = ttk.Button(
            self.form_frame, text="Generate", command=handle_password_generation)
        self.generate_password.grid(row=3, column=2)

        self.add_button = ttk.Button(
            self.form_frame, text="Add Password", command=handle_add_password)
        self.add_button.grid(row=6, column=1, pady=5)

        self.update_button = ttk.Button(
            self.form_frame, text="Update", command=handle_password_update)

        self.cancel_button = ttk.Button(
            self.form_frame, text="Cancel", command=reset_form_entries)

        # Table contnet
        self.password_tree = ttk.Treeview(self.table_frame, columns=(
            'Account', 'Username', 'Link', 'Note'), show="headings")

        self.password_tree.column('Account', width=100, stretch=False)
        self.password_tree.column('Username', width=100, stretch=False)
        self.password_tree.column('Link', width=200, stretch=False)
        self.password_tree.column('Note', stretch=True)

        self.password_tree.heading('Account', text="Account")
        self.password_tree.heading('Username', text="Username")
        self.password_tree.heading('Link', text="Link")
        self.password_tree.heading('Note', text="Note")
        self.password_tree.pack(side="left", expand=True, fill="both")
        self.tree_entries = self.password_logic.get_passwords()
        for account in self.tree_entries:
            self.password_tree.insert(parent='', index=_tk.END, values=(
                account['Account'], account['Username'], account['LoginLink'], account['Note']))

        def update_table_entries():
            if self.password_tree.get_children() == None:
                self.tree_entries = self.password_logic.get_passwords()
                for account in self.tree_entries:
                    self.password_tree.insert(parent='', index=_tk.END, values=(
                        account['Account'], account['Username'], account['LoginLink'], account['Note']))
            else:
                # Remove old enteries
                for account in self.password_tree.get_children():
                    self.password_tree.delete(account)
                # Re- add new db entries
                for account in self.tree_entries:
                    self.password_tree.insert(parent='', index=_tk.END, values=(
                        account['Account'], account['Username'], account['LoginLink'], account['Note']))

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
                    _tk.END, string=f"{self.password_logic.decrypt_message(selected_item_info['Password'])}")
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
                    reset_form_entries()
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

        def username_copy(_):
            selected_item = self.password_tree.item(
                self.password_tree.selection())
            if selected_item["values"] == "":
                pass
            elif selected_item["values"] is not None:
                selected_item_info = self.password_logic.get_password(
                    selected_item['values'][0])
                pyperclip.copy(selected_item_info["Username"])

        def password_copy(_):
            selected_item = self.password_tree.item(
                self.password_tree.selection())
            if selected_item["values"] == "":
                pass
            elif selected_item["values"] is not None:
                selected_item_info = self.password_logic.get_password(
                    selected_item['values'][0])
                decrypted_password = self.password_logic.decrypt_message(
                    selected_item_info["Password"])
                pyperclip.copy(decrypted_password)

        self.password_tree.bind('<Double-1>', item_select)
        self.password_tree.bind('<Delete>', item_delete)
        self.password_tree.bind('<Escape>', item_deselect)
        self.password_tree.bind('<Control-b>', username_copy)
        self.password_tree.bind('<Control-c>', password_copy)

        # Vertical table scrolling
        self.vertical_scroll = ttk.Scrollbar(
            self.table_frame, orient="vertical",
            command=self.password_tree.yview
        )
        self.password_tree.configure(
            yscrollcommand=self.vertical_scroll.set)
        self.vertical_scroll.pack(side="left", fill="y")

        self.password_tree.bind('<MouseWheel>', lambda event: self.password_tree.configure(
            yscrollcommand=self.vertical_scroll.set))


class FinanceContent(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.transaction_logic = TransactionLogic()

        # Frames /  View layout
        self.action_frame = ttk.Frame(self)
        self.action_frame.config(relief="groove")
        self.action_frame.pack(side="left", fill="y")

        self.summation_frame = ttk.Frame(self.action_frame)
        self.summation_frame.configure(relief="groove")
        self.summation_frame.pack(side="top", fill="both", ipady=35)

        self.form_frame = ttk.Frame(self.action_frame)
        self.form_frame.configure(relief="groove")
        self.form_frame.pack(side="top", fill="both", expand=True)

        self.table_frame = ttk.Frame(self)
        self.table_frame.configure(relief='groove')
        self.table_frame.pack(side="left", fill="both", expand=True)

        # Pre - fetch table and amount summary
        transaction_list = self.transaction_logic.get_transactions()
        credit_sum = 0
        debit_sum = 0
        for transaction in transaction_list:
            if transaction["TransactionType"] == "Credit":
                credit_sum += transaction["Amount"]
            elif transaction["TransactionType"] == "Debit":
                debit_sum += transaction["Amount"]
        total_savings = credit_sum-debit_sum

        # Functions
        def reset_form_entries():
            self.amount_entry.delete(0, _tk.END)
            self.event_entry.delete(0, _tk.END)
            self.tag_entry.delete(0, _tk.END)
            self.note_enrty.delete(0, _tk.END)

        def handle_add_transaction():
            amount = self.amount_entry.get()
            event = self.event_entry.get()
            tag = self.tag_entry.get()
            note = self.note_enrty.get()

            if tag == "":
                messagebox.showerror(
                    title="Error", message="Error recording transactions. Amount / tag can not be empty")
            else:
                transaction_added = self.transaction_logic.record_transaction(
                    amount, event, tag, note)
                if transaction_added:
                    reset_form_entries()
                    messagebox.showinfo(
                        title="Success!", message="Recorded transaction successfully!")
                    self.transaction_entries = self.transaction_logic.get_transactions()
                    update_amount_summary(self.transaction_entries)
                    update_transaction_table_entries()
                else:
                    messagebox.showerror(
                        title="Error!", message="Error recording transaction. Please try again!")

        def update_transaction_table_entries():
            if self.transaction_tree.get_children() == None:
                self.transaction_entries = self.transaction_logic.get_transactions()
                for transaction in self.transaction_entries:
                    self.transaction_tree.insert(parent='', index=_tk.END, values=(
                        transaction['CreateDate'], transaction['TransactionType'],
                        transaction['Amount'], transaction['TransactionTag'], transaction['TransactionNote']))
            else:
                # Remove old entries
                for transaction in self.transaction_tree.get_children():
                    self.transaction_tree.delete(transaction)
                # Re-add new db entries
                for transaction in self.transaction_entries:
                    self.transaction_tree.insert(parent='', index=_tk.END, values=(
                        transaction['CreateDate'], transaction['TransactionType'],
                        transaction['Amount'], transaction['TransactionTag'], transaction['TransactionNote']))

        def update_amount_summary(transaction_list):
            credit_sum = 0
            debit_sum = 0
            for transaction in transaction_list:
                if transaction["TransactionType"] == "Credit":
                    credit_sum += transaction["Amount"]
                    self.credit_label.configure(text=f"Credit: {credit_sum}")
                elif transaction["TransactionType"] == "Debit":
                    debit_sum += transaction["Amount"]
                    self.debit_label.configure(text=f"Debit: {debit_sum}")
            total_savings = (credit_sum - debit_sum)
            self.total_label.configure(text=f"Savings €: {total_savings}")

        # Summation contnet
        self.total_label = ttk.Label(
            self.summation_frame, text=f"Savings €: {total_savings}", font=("bold"))
        self.total_label.grid(row=0, column=0, columnspan=2, ipady=10)

        self.credit_label = ttk.Label(
            self.summation_frame, text=f"Credit: {credit_sum}", font=(30))
        self.credit_label.grid(row=1,  column=0, ipady=5)

        self.debit_label = ttk.Label(
            self.summation_frame, text=f"Debit: {debit_sum}", font=(30))
        self.debit_label.grid(row=2, column=0)

        # Form contnet
        self.view_label = ttk.Label(
            self.form_frame, text="Record Transaction",
            font=(40))
        self.view_label.grid(
            row=0, column=0,
            pady=10, columnspan=2)

        self.amount_label = ttk.Label(self.form_frame, text="Amount:")
        self.amount_label.grid(row=1, column=0, ipady=10)

        self.amount_entry = ttk.Spinbox(
            self.form_frame, from_=0,
            wrap=True, width=10)
        self.amount_entry.grid(row=1, column=1, padx=5)

        self.event_label = ttk.Label(self.form_frame, text="Event:")
        self.event_label.grid(row=2, column=0, ipady=10)

        self.event_entry = ttk.Combobox(
            self.form_frame, state="readonly",
            values=["Debit", "Credit"], width=10)
        self.event_entry.set("Credit")
        self.event_entry.grid(row=2, column=1, padx=5)

        self.tag_label = ttk.Label(self.form_frame, text="Tag:")
        self.tag_label.grid(row=3, column=0, ipady=10)

        self.tag_entry = ttk.Entry(self.form_frame)
        self.tag_entry.grid(row=3, column=1, padx=5)

        self.note_label = ttk.Label(self.form_frame, text="Note:")
        self.note_label.grid(row=4, column=0, ipady=10)

        self.note_enrty = ttk.Entry(self.form_frame)
        self.note_enrty.grid(row=4, column=1, padx=5)

        self.add_button = ttk.Button(
            self.form_frame, text="Record", command=handle_add_transaction)
        self.add_button.grid(row=5, column=1, pady=10)

        # Transaction table
        self.transaction_tree = ttk.Treeview(self.table_frame, columns=(
            'Date', 'Event', 'Amount', 'Tag', 'Note'), show="headings")

        self.transaction_tree.column('Date', width=100, stretch=False)
        self.transaction_tree.column('Event', width=100, stretch=False)
        self.transaction_tree.column('Amount', width=110, stretch=False)
        self.transaction_tree.column('Tag', width=110, stretch=False)
        self.transaction_tree.column('Note', stretch=True)

        self.transaction_tree.heading('Date', text="Date")
        self.transaction_tree.heading('Event', text="Event")
        self.transaction_tree.heading('Amount', text="Amount")
        self.transaction_tree.heading('Tag', text="Tag")
        self.transaction_tree.heading('Note', text='Note')
        self.transaction_tree.pack(side="left", expand=True, fill="both")
        self.transaction_entries = transaction_list
        for transaction in self.transaction_entries:
            self.transaction_tree.insert(parent='', index=_tk.END, values=(
                transaction['CreateDate'],
                transaction['TransactionType'],
                transaction['Amount'],
                transaction['TransactionTag'],
                transaction['TransactionNote']))

        # Vertical table scrolling
        self.vertical_scroll = ttk.Scrollbar(
            self.table_frame, orient="vertical", command=self.transaction_tree.yview)
        self.transaction_tree.configure(
            yscrollcommand=self.vertical_scroll.set)
        self.vertical_scroll.pack(side="left", fill="y")

        self.transaction_tree.bind('<MouseWheel>', lambda event: self.transaction_tree.configure(
            yscrollcommand=self.vertical_scroll.set))
