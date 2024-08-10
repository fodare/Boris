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

    def add_app_user(self, username, pasword):
        with self.connect_to_db() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(f"""
                        EXEC UserSchema.spUser_Add 
                        @userName = '{username}', @password = '{pasword}', 
                        @createDate = '{datetime.date.today()}', @lastUpdates = '{datetime.date.today()}'
                    """)
                    ouput = cursor.fetchone()
                    conn.commit()
                    if ouput["Username"] == username:
                        return True
                except pymssql.exceptions.OperationalError as err:
                    return False
