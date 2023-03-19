from sqlite3 import connect


def add_data(user_service: str, user_amount: str):
    with connect("database.db") as db:
        cursor = db.cursor()
        user_query = (user_service, float(user_amount))
        query = """INSERT INTO service(name,amount) VALUES(?,?);"""
        cursor.executemany(query, user_query)
        print("DATA IS UPDATED!")

