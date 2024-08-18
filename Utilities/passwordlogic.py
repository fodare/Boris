from random import randint, shuffle, choice
import json
from Data import dbLogic


class PasswordLogic:
    def __init__(self):
        self.db_logic = dbLogic.DBLogic()

    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                   'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = randint(8, 10)
        nr_symbols = randint(2, 4)
        nr_numbers = randint(2, 4)

        password_letters = [choice(letters) for _ in range(nr_letters)]
        password_symbols = [choice(symbols) for _ in range(nr_symbols)]
        password_numbers = [choice(numbers) for _ in range(nr_numbers)]

        password_list = password_letters+password_symbols+password_numbers
        shuffle(password_list)

        password = "".join(password_list)
        return password

    def record_password(self, account, username, password,  link, note):
        return self.db_logic.add_password_entry(account, username, password, link, note)

    def get_passwords(self):
        return self.db_logic.get_passwords()

    def get_password(self, account):
        return self.db_logic.get_password(account)

    def update_password(self, id, account, username, password, link, note):
        return self.db_logic.update_password(id, account, username, password, link, note)

    def delete_password(self, id):
        return self.db_logic.delete_password(id)
