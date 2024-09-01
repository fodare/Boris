from Data import dbLogic


class TransactionLogic:
    def __init__(self):
        self.db_logic = dbLogic.DBLogic()

     # Transaction operations
    def record_transaction(self, amount, event, tag, note):
        return self.db_logic.add_transaction_entry(amount, event, tag, note)

    def get_transactions(self):
        return self.db_logic.get_transactions()

    def get_transaction(self,  id):
        return self.db_logic.get_transaction(id)
