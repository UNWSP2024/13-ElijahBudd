# Elijah Budd
# 4/28/2025
# Program #2: Display Data from Cities Database
import sqlite3

def main():
    connect = sqlite3.connect('cities.db')
    cursor = connect.cursor()


    print("How would you like to see the data?")
    print("Enter the number next to the option you would like")

    print("1: Display a list of cities sorted by population, in ascending order.")
    print("2: Display a list of cities sorted by population, in descending order.")
    print("3: Display a list of cities sorted by name.")
    print("4: Display the total population of all the cities.")
    print("5: Display the average population of all the cities.")
    print("6: Display the city with the highest population.")
    print("7: Display the city with the lowest population.")

    option_input = int(input("Enter your choice: "))

    print("----------------------------")

    if option_input == 1:
        display_ascending(cursor)

    elif option_input == 2:
        display_descending(cursor)

    elif option_input == 3:
        display_name(cursor)

    elif option_input == 4:
        display_total_pop(cursor)

    elif option_input == 5:
        display_average_pop(cursor)

    elif option_input == 6:
        display_highest_pop(cursor)

    elif option_input == 7:
        display_lowest_pop(cursor)

    else:
        print("Enter a correct value")
        main()

    connect.close()

def display_ascending(cursor):
    cursor.execute("SELECT * FROM Cities ORDER BY Population ASC")
    print("Cities sorted by Population Ascending:")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

def display_descending(cursor):
    cursor.execute("SELECT * FROM Cities ORDER BY Population DESC")
    print("Cities sorted by Population Descending:")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def display_name(cursor):
    cursor.execute("SELECT * FROM Cities ORDER BY CityName")
    print("Cities sorted by Name:")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

def display_total_pop(cursor):
    cursor.execute("SELECT SUM(Population) FROM Cities")
    total = cursor.fetchone()[0]
    print(f"Total population of all cities: {total}")

def display_average_pop(cursor):
    cursor.execute("SELECT AVG(Population) FROM Cities")
    average = cursor.fetchone()[0]
    print(f"Average population of all cities: {average}")

def display_highest_pop(cursor):
    cursor.execute("SELECT MAX(Population) FROM Cities")
    highest = cursor.fetchone()[0]
    print(f"Highest population of all cities: {highest}")

def display_lowest_pop(cursor):
    cursor.execute("SELECT MIN(Population) FROM Cities")
    lowest = cursor.fetchone()[0]
    print(f"Lowest population of all cities: {lowest}")

if __name__ == "__main__":
    main()
