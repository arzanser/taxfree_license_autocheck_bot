import sqlite3

from bot.config import *


db = sqlite3.connect(DB_PATH)
cursor = db.cursor()


def connect_to_db() -> None:
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Clients(
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_name TEXT, 
                client_phone_number TEXT, 
                client_car_number TEXT,
                region TEXT,
                inn_number TEXT,
                status TEXT
                )
                """)
    
    cursor.execute("SELECT * FROM Clients")

        
def insert_to_db(client_data) -> None:
    cursor = db.cursor()
    cursor.execute("""
                   INSERT 
                   INTO Clients(client_name, client_phone_number, client_car_number)
                   VALUES(?,?,?)"""
                   , (client_data))
    db.commit()


def delete_record_from_db(client_id) -> None:
    connect_to_db()
    client_id = int(str(client_id).strip())
    cursor.execute("""
                   DELETE 
                   FROM Clients 
                   WHERE client_id=?"""
                   , (client_id, ))
    db.commit()


def clean_table() -> None:
    connect_to_db()
    cursor.execute("""DELETE FROM Clients""")
    db.commit()


def close_db() -> None:
    cursor.close()
    db.close()


def show_db() -> list:
    connect_to_db()
    db_records = cursor.fetchall()
    return db_records


def add_to_db(data) -> None: 
    connect_to_db()
    client_data = tuple(value for value in data.values())
    insert_to_db(client_data)


def add_region_to_db(region, car_number) -> None:
    id = get_id_client(car_number)
    connect_to_db()
    cursor.execute("""
                   UPDATE Clients
                   SET region=? 
                   WHERE client_id=?"""
                   , (region, id))
    db.commit()


def add_inn_to_db(inn_number, car_number) -> None:
    id = get_id_client(car_number)
    connect_to_db()
    cursor.execute("""
                   UPDATE Clients 
                   SET inn_number=?
                   WHERE client_id=?"""
                   , (inn_number, id))
    db.commit()

def add_license_status(car_number, status) -> None:
    id = get_id_client(car_number)
    connect_to_db()
    cursor.execute("""
                   UPDATE Clients 
                   SET status=?
                   WHERE client_id=?"""
                   , (status, id))
    db.commit()

def get_id_client(car_number) -> str:
    connect_to_db()
    cursor.execute("""
                   SELECT * 
                   FROM Clients 
                   WHERE client_car_number=?"""
                   , (car_number,))
    data = cursor.fetchall()
    db.commit()
    return data[0][0]


def get_car_numbers() -> list:
    connect_to_db()
    cursor.execute("""
                   SELECT client_car_number 
                   FROM Clients""")

    return cursor.fetchall()

# def get_region(car_number, region):
#     connect_to_db()
#     cursor.execute("""
#                    SELECT region 
#                    FROM Clients 
#                    WHERE client_car_number=?"""
#                    , (car_number,))
#     db.commit()

def get_inn_number(car_number):
    try:
        cursor.execute("""
                    SELECT inn_number
                    From Clients
                    WHERE client_car_number=?"""
                    , (car_number,))
        inn_number = cursor.fetchall()[0][0]
        db.commit()
        return inn_number
    except:
        return False
                   



