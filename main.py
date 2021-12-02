# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
import sqlite3
import telebot
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

contactNumber=["A-79345657","B-7898403","C-7645453"] ## сначала имя потом номер
note=["A","B","w"]
connection=sqlite3.connect("contacts.db")
cursor=connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS contacts(
name TEXT,
contactNumber TEXT)
""")
connection.commit()
class PhoneBook ():
    def __init__(self, contactNumber, note):
        pass
    def getContactByName(self,contactNumber):
        for i in range(len(contactNumber)):
            for j in range (len(contactNumber[i])):
                if contactNumber[i][j]=="-":
                    local_connection = sqlite3.connect("contacts.db")
                    local_cursor = local_connection.cursor()
                    local_cursor.execute(f"INSERT INTO contacts VALUES(?,?);",(contactNumber[i][:j],contactNumber[i][j+1:]))
                    local_connection.commit()




PhoneContact1=PhoneBook(contactNumber, note)


