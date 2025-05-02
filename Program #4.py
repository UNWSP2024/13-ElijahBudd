# Elijah Budd
# 5/2/2025
# Program #4: Access Phonebook

import sqlite3

def main():

    connect = sqlite3.connect('phonebook.db')
    cursor = connect.cursor()

    while True:
        accessInput = input("Would you like to read, update, or delete data(Enter 0 to stop):")

        if accessInput == "read":
            cursor.execute("SELECT * FROM phonebook")
            fetchall = cursor.fetchall()
            for row in fetchall:
                print(row)

        elif accessInput == "update":
            name = input("Add name data to phonebook(name): ")
            phoneNumber = input("Add phone number data to phonebook(PhoneNumber): ")
            access = ('''INSERT INTO Phonebook (PersonName, PhoneNumber) VALUES (?, ?)''')
            connect.execute(access, (name, phoneNumber))

        elif accessInput == "delete":
            delete = input("What would you like to delete?(phoneNumber): ")
            cursor.execute("DELETE FROM Phonebook WHERE PhoneNumber = ?", (delete,))

        elif accessInput == '0':
            break

    connect.commit()
    connect.close()

if __name__ == "__main__":
    main()
