import pymssql
import os
from dotenv import load_dotenv
import datetime

"""
Manages db connections using pymssql
"""

load_dotenv()


class DBLogic():
    def __init__(self):
        pass

    def connect_to_db(self):
        db_connection = pymssql.connect(
            server=f"{os.getenv('DBSERVERNAME')}",
            user=f"{os.getenv('DBUSERNAME')}",
            password=f"{os.getenv('DBPASSWORD')}",
            database=f"{os.getenv('DATBASENAME')}",
            as_dict=True
        )
        return db_connection

    # APP user operations

    def get_app_users(self):
        with self.connect_to_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute('EXEC UserSchema.spUser_Get')
                return cursor.fetchall()

    def get_app_user(self, username):
        with self.connect_to_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    f"EXEC UserSchema.spUser_Get @userName = '{username}'")
                return cursor.fetchone()

    def add_app_user(self, username, pasword) -> bool:
        with self.connect_to_db() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(f'''
                        EXEC UserSchema.spUser_Add
                        @userName = "{username}", @password = "{pasword}",
                        @createDate = "{datetime.date.today()}", @lastUpdates = "{datetime.date.today()}"
                    ''')
                    ouput = cursor.fetchone()
                    conn.commit()
                    if ouput["Username"] == username:
                        return True
                except pymssql.exceptions.OperationalError as err:
                    return False

    # Password operations

    def add_password_entry(self, account, username, password, link, note) -> bool:
        with self.connect_to_db() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(
                        f"""EXEC PasswordSchema.spPasswords_Add
                    @account='{account}', @username ='{username}',
                    @password='{password}',@link='{link}', @note='{note}'
                    """)
                    output = cursor.fetchone()
                    conn.commit()
                    if output["Account"] == account:
                        return True
                except pymssql.exceptions.OperationalError as err:
                    return False

    def get_passwords(self):
        with self.connect_to_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute("EXEC PasswordSchema.spPasswords_Get")
                return cursor.fetchall()

    def get_password(self, account):
        with self.connect_to_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    f"EXEC PasswordSchema.spPasswords_Get @account='{account}'")
                return cursor.fetchone()

    def update_password(self, id, account, username, password, link, note) -> bool:
        with self.connect_to_db() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(f"""
                        EXEC PasswordSchema.spPasswords_Update
                        @id= {id}, @account = '{account}', @username = '{username}',
                        @password = '{password}', @link='{link}', @note = '{note}'
                    """)
                    output = cursor.fetchone()
                    conn.commit()
                    if output["Account"] == account:
                        return True
                except pymssql.exceptions.OperationalError as err:
                    return False

    def delete_password(self, id):
        with self.connect_to_db() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(
                        f"EXEC PasswordSchema.spPasswords_Delete @id={id}")
                    output = cursor.fetchone()
                    conn.commit()
                    if output['id'] == id:
                        return True
                except pymssql.exceptions.OperationalError as err:
                    return False

    # Transaction operations

    def add_transaction_entry(self, amount, event, tag, note):
        with self.connect_to_db() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(f""" EXEC TransactionRecordSchema.spTransactionsAdd
                    @amount={amount},@type='{event}',@tag='{tag}',@note='{note}',@createDate='{datetime.date.today()}',@updateDate='{datetime.date.today()}' """)
                    output = cursor.fetchone()
                    conn.commit()
                    if output["id"] is not None:
                        return True
                except Exception as err:
                    return False

    def get_transactions(self):
        with self.connect_to_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'EXEC TransactionRecordSchema.spTransactions_Get')
                return cursor.fetchall()

    def get_transaction(self, id):
        with self.connect_to_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    f'EXEC TransactionRecordSchema.spTransactions_Get @id={id}')
                return cursor.fetchone()
