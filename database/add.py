from sqlite3 import connect


def add_data(user_service: str, user_amount: str):
    with connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute(("""INSERT INTO service(name,amount) VALUES(?,?)"""),(user_service,user_amount))
        print("DATA IS UPDATED!")

