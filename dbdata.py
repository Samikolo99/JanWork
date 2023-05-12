import pandas as pd

# Create tables
create_customers_stmt='''CREATE TABLE IF NOT EXISTS customers 
             (id INTEGER PRIMARY KEY,
             first_name TEXT,
             last_name TEXT,
             postcode TEXT,
             house_number TEXT,
             phone_number TEXT)'''

create_bouncycastles_stmt='''CREATE TABLE IF NOT EXISTS bouncy_castles
             (id INTEGER PRIMARY KEY,
             dimensions TEXT,
             main_color TEXT,
             name TEXT,
             max_occupants INTEGER,
             hire_price REAL)'''

create_bookings_stmt='''CREATE TABLE IF NOT EXISTS bookings
             (id INTEGER PRIMARY KEY,
             customer_id INTEGER,
             bouncy_castle_id INTEGER,
             booking_date TEXT,
             additional_notes TEXT,
             FOREIGN KEY (customer_id) REFERENCES customers(id)
             ON DELETE CASCADE,
             FOREIGN KEY (bouncy_castle_id) REFERENCES bouncy_castles(id)
             ON DELETE CASCADE)'''

create_statements=(create_customers_stmt, create_bouncycastles_stmt, create_bookings_stmt)

# Insert initial data
insert_bcastles=[("INSERT INTO bouncy_castles VALUES (1, '10ft x 10ft', 'Red', 'Castle 1', 6, 50.00)",),
("INSERT INTO bouncy_castles VALUES (2, '12ft x 12ft', 'Blue', 'Castle 2', 8, 75.00)",)]



# Functions for CRUD operations

def add_customer(first_name, last_name, postcode, house_number, phone_number, c, conn):
    c.execute("INSERT INTO customers (first_name, last_name, postcode, house_number, phone_number) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, postcode, house_number, phone_number))
    conn.commit()

def view_customers(conn):
    stmt="SELECT * FROM customers"
    print(pd.read_sql_query(stmt, conn))


def update_customer(customer_id, first_name, last_name, postcode, house_number, phone_number, c, conn):
    c.execute("UPDATE customers SET first_name = ?, last_name = ?, postcode = ?, house_number = ?, phone_number = ? WHERE id = ?", (first_name, last_name, postcode, house_number, phone_number, customer_id))
    conn.commit()


def delete_customer(customer_id, c, conn):
    c.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
    conn.commit()

def add_bouncy_castle(dimensions, main_color, name, max_occupants, hire_price, c, conn):
    c.execute("INSERT INTO bouncy_castles (dimensions, main_color, name, max_occupants, hire_price) VALUES (?, ?, ?, ?, ?)", (dimensions, main_color, name, max_occupants, hire_price))
    conn.commit()

def view_bouncy_castle(conn):
    stmt="SELECT * FROM bouncy_castles"
    print(pd.read_sql_query(stmt, conn))

def update_bouncy_castle(bouncy_castle_id, dimensions, main_color, name, max_occupants, hire_price, c, conn):
    c.execute("UPDATE bouncy_castles SET dimensions=?, main_color=?, name=?, max_occupants=?, hire_price=? WHERE id=?", (dimensions, main_color, name, max_occupants, hire_price, bouncy_castle_id))
    conn.commit()

def delete_bouncy_castle(bouncy_castle_id, c, conn):
    c.execute("DELETE FROM bouncy_castles WHERE id = ?", (bouncy_castle_id,))
    conn.commit()

def add_booking(customer_id, bouncy_castle_id, booking_date, additional_notes, c, conn):
    c.execute("INSERT INTO bookings (customer_id, bouncy_castle_id, booking_date, additional_notes) VALUES (?, ?, ?, ?)", (customer_id, bouncy_castle_id, booking_date, additional_notes))
    conn.commit()

def view_booking(conn):
    stmt="SELECT * FROM bookings"
    print(pd.read_sql_query(stmt, conn))

def update_booking(booking_id, customer_id, bouncy_castle_id, booking_date, additional_notes, c, conn):
    c.execute("UPDATE bookings SET customer_id=?, bouncy_castle_id=?, booking_date=?, additional_notes=? WHERE id=?", (customer_id, bouncy_castle_id, booking_date, additional_notes, booking_id))
    conn.commit()

def delete_booking(booking_id, c, conn):
    c.execute("DELETE FROM booking WHERE id=?", (booking_id,))
    conn.commit()
