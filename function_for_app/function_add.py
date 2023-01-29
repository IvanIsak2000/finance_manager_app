def add_data_in_sql(user_service, user_amount):  # add data by name and amount

    import sqlite3
    import dearpygui.dearpygui as dpg

    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        user_query = [(user_service, user_amount)]

        query = '''INSERT INTO service(name,amount) VALUES(?,?) '''
        cursor.executemany(query, user_query)

        print('DATA IS UPDATED!')
