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
name=["A","B","C"]
contactNumber=["A","79345657","B","7898403","C","7645453"] ## сначала имя потом номер
note=["A","B","w"]
class PhoneContact ():
    def __init__(self,name, contactNumber, note):
        self.name=name
        self.contactNumber=contactNumber
        self.note=note
    def convert_name(self,name):
        return "".join(name)
    def convert_contactNumber(self,contactNumber):
        return "".join(contactNumber)
    def convert_note(self,note):
        return "".join(note)

PhoneContact1=PhoneContact(name,contactNumber,note)
print(PhoneContact1.convert_name(name))