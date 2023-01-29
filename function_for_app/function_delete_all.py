def delete_all_in_sql():  # delete all data
    import sqlite3
    import time
    import sys

    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = '''DROP  table service '''
        cursor.execute(query)
        print('All data delete!')
        print(' The program will close!')
        time.sleep(3)
        sys.exit()
