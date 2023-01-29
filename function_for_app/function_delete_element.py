def delete_element_in_sql(name_to_delete):
    import sqlite3
    with sqlite3.connect('database.db') as db:  # DELETE ELEMENT
        cursor = db.cursor()
        query = ''' DELETE FROM service WHERE name = ?'''
        cursor.execute(query, (name_to_delete,))

    print(
        f"The data named '{name_to_delete}' was deleted if it was in the database!")
