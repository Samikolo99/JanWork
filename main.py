
import sqlite3
from datetime import date
import pandas as pd
from dbdata import *


# Create a connection to the database
conn = sqlite3.connect('bouncy_castles.db')

# Create a cursor object
c = conn.cursor()

for statement in create_statements:
    c.execute(statement)

print("Successfully created database tables")

# This is creating 2 customers for the customer table then deleting the second customer
dummy_check = input("Would you like to add dummy data and be given the choice to run Add and Update Operations? (Y/N)")
if dummy_check[0].lower() == 'y':
    add_customer("Samuel", "Fabunmi", "M8 9GF", "17", "07548876857", c, conn)
    add_customer("Yemi", "Waheed", "M7 9TY", "20", "076546977385", c, conn)
    delete_customer(2, c, conn)
    view_customers(conn)

    add_bouncy_castle("Large", "Red", "Volcano Bounce", 16, 75, c, conn)
    view_bouncy_castle(conn)

    add_booking(1, 1, "10/05/2023", "Booked for 7 days", c, conn)
    view_booking(conn)

    insert_check = input("Would you like to update a value on a table? (Y/N)")
    if insert_check[0].lower() == 'y':
        table_check = input("What table would you like to add data to?")
        if table_check.lower() == 'customer':
            first_name = input("what is your first name? - ")
            last_name = input("what is your last name? - ")
            postcode = input("what is your postcode? - ") 
            house_number = input("what is your house number? - ")
            phone_number = input("what is your phobe number? - ")
            add_customer(first_name, last_name, postcode, house_number, phone_number, c, conn)
            view_customers(conn)

        elif table_check.lower() == 'bouncy castle':
            dimensions = input("What is the size of the bouncy castle? - ")
            main_colour = input("What is the main colour of the bouncy castle? - ")
            name = input("What is the name of the bouncy castle? - ")
            max_occupants = input("What is the maximum number of occupants? - ")
            hire_price = input("How much does it cost to hire the bouncy castle per day? - ")
            add_bouncy_castle(dimensions, main_colour, name, max_occupants, hire_price, c, conn)
            view_bouncy_castle(conn)

        elif table_check.lower() == 'booking':
            customer_id = input("what is the customer ID? - ")
            bouncy_castle_id = input("what is the bouncy castle ID- ")
            booking_date = input("what is the booking date? - ")
            additional_notes = input("what else would you like to add? -")
            add_booking( customer_id, bouncy_castle_id, booking_date, additional_notes, c, conn)
            view_booking(conn)
        else:
            print("You have chosen to not add any data")


    update_check = input("Would you like to update a value on a table? (Y/N)")
    if update_check[0].lower() == 'y':
        table_check = input("What table would you like to update?")
        if table_check.lower() == 'customer':
            customer_id = input("what ID would you like to update? - ")
            first_name = input("what is your first name? - ")
            last_name = input("what is your last name? - ")
            postcode = input("what is your postcode? - ") 
            house_number = input("what is your house number? - ")
            phone_number = input("what is your phobe number? - ")
            update_customer(customer_id, first_name, last_name, postcode, house_number, phone_number, c, conn)
            view_customers(conn)

        elif table_check.lower() == 'bouncy castle':
            bouncy_castle_id = input("What ID would you like to update? - ")
            dimensions = input("What is the size of the bouncy castle? - ")
            main_colour = input("What is the main colour of the bouncy castle? - ")
            name = input("What is the name of the bouncy castle? - ")
            max_occupants = input("What is the maximum number of occupants? - ")
            hire_price = input("How much does it cost to hire the bouncy castle per day? - ")
            update_bouncy_castle(bouncy_castle_id, dimensions, main_colour, name, max_occupants, hire_price, c, conn)
            view_bouncy_castle(conn)

        elif table_check.lower() == 'booking':
            booking_id = input("what ID would you like to update? - ")
            customer_id = input("what customer ID would you like to update? - ")
            bouncy_castle_id = input("what bouncy castle ID would you like to update? - ")
            booking_date = input("what date would you like to update? - ")
            additional_notes = input("what else would you like to add? -")
            update_booking(booking_id, customer_id, bouncy_castle_id, booking_date, additional_notes, c, conn)
            view_booking(conn)
        else:
            print("You have chosen to not update any data")
    else:
        print("You have chosen to not add any dummy data")

conn.close()