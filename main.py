# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
name="A"
contactNumber=["A-79345657","B-7898403","C-7645453"] ## сначала имя потом номер
note=["A","B","w"]

class PhoneBook ():
    def __init__(self,name, contactNumber, note):
        pass
    def getContactByName(self,contactNumber,name):
        for i in range(len(contactNumber)):
            for j in range (len(contactNumber[i])):
                if contactNumber[i][j]=="-":
                    if contactNumber[i][:j]==name:
                        print(contactNumber[i][j+1:])
                        return contactNumber[i][j+1:]
                    else:
                        raise ValueError("Формат ввода'имя-00000000'")


PhoneContact1=PhoneBook(name, contactNumber, note)

print(PhoneContact1.getContactByName(contactNumber,name))
