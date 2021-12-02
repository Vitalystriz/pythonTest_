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
token = "2087683356:AAGZgp67CrWWVIij1iv-rpMyKTcG6KM5es0"
bot = telebot.TeleBot(token)

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
@bot.message_handler(commands=["start"])
def send_start_message(message):
    bot.send_message(message.chat.id, "формат 'имя-0000000'")
@bot.message_handler(content_types=["text"])
def send_start_message(message):
    to_chat_id=message.chat.id
    msg=message.text
    if msg.isalpha()==True:

        local_connection = sqlite3.connect("contacts.db")
        local_cursor = local_connection.cursor()
        local_cursor.execute(f" SELECT * from contacts ;")
        all_fetchall = local_cursor.fetchall()
        for i in range(len(all_fetchall)):
            for j in range(len(all_fetchall[i])):
                if str(all_fetchall[i][j])==msg:
                    number=all_fetchall[i][j+1]

        bot.send_message(to_chat_id,number)
    if msg.isdigit() == True:

        local_connection = sqlite3.connect("contacts.db")
        local_cursor = local_connection.cursor()
        local_cursor.execute(f" SELECT * from contacts ;")
        all_fetchall = local_cursor.fetchall()
        for i in range(len(all_fetchall)):
            for j in range(len(all_fetchall[i])):
                if str(all_fetchall[i][j]) == msg:
                    number = all_fetchall[i][j - 1]

        bot.send_message(to_chat_id, number)
    if msg.isdigit() != True and msg.isalpha != True:
        for j in range(len(msg)):
            if msg[j] == "-":
                local_connection = sqlite3.connect("contacts.db")
                local_cursor = local_connection.cursor()
                local_cursor.execute(f"INSERT INTO contacts VALUES(?,?);",
                                     (msg[:j], msg[j + 1:]))
                local_connection.commit()




        bot.send_message(to_chat_id, number)





PhoneContact1=PhoneBook(contactNumber, note)

bot.polling(none_stop=True, interval=0)
