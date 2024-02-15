import sqlite3
import uuid
from enum import IntEnum

def DataController():
    class TableIndex(IntEnum):
        AMOUNT = 0
        DATE = 1
        TYPE = 2
        UID = 3
    
    db_connection = sqlite3.connect("MoneyManagementDB")
    cursor = db_connection.cursor()
        
    db_connection.execute(
        '''CREATE TABLE if not exists income_values(
            AMOUNT REAL,
            DATE TEXT
            TYPE TEXT
            UUID TEXT PRIMARY KEY);''')
    db_connection.execute(
        '''CREATE TABLE if not exists expense_values(
            AMOUNT REAL,
            DATE TEXT
            TYPE TEXT
            UUID TEXT PRIMARY KEY);''')
    
    def AddIncomeToDB(amount, date, type):
        new_uuid = uuid.uuid4()
        db_connection.execute(f'''INSERT INTO income_values VALUES(
            {amount}, {date}, {type}, {str(new_uuid)})''')
        return str(new_uuid)
    
    def AddExpenseToDB(amount, date, type):
        new_uuid = uuid.uuid4()
        db_connection.execute(f'''INSERT INTO expense_values VALUES(
            {amount}, {date}, {type}, {str(new_uuid)})''')
        return str(new_uuid)
    
    def GetIncomeFromDB():
        cursor = db_connection.execute('''SELECT * FROM income_value''')
        list_of_income_values = []
        for iterator in cursor:
            list_of_income_values.append([iterator[TableIndex.AMOUNT], iterator[TableIndex.DATE], 
                                          iterator[TableIndex.TYPE], iterator[TableIndex.UID]])
        return list_of_income_values
    
    def GetExpenseFromDB():
        cursor = db_connection.execute('''SELECT * FROM expense_value''')
        list_of_expense_values = []
        for iterator in cursor:
            list_of_expense_values.append([iterator[TableIndex.AMOUNT], iterator[TableIndex.DATE], 
                                          iterator[TableIndex.TYPE], iterator[TableIndex.UID]])
        return list_of_expense_values
    
    def DeleteIncomeFromDB(del_uuid):
        db_connection.execute(f"DELETE FROM income_values WHERE UUID = {str(del_uuid)}")
        
    def DeleteExpenseFromDB(del_uuid):
        db_connection.execute(f"DELETE FROM expense_values WHERE UUID = {str(del_uuid)}")
    