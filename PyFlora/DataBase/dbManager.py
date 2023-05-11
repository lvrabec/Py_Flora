import sqlite3

def create_connection(db_file):
    db_connection = None
    try:
        db_connection = sqlite3.connect(db_file)
        return db_connection
    except sqlite3.Error as db_error:
        print(db_error)

def create_table(db_connection, create_table_sql):
    try:
        cursor = db_connection.cursor()
        cursor.execute(create_table_sql)
    
    except sqlite3.Error as db_error:
        print(db_error)

def create_record(db_connection, sql_query):
    try:
        cursor = db_connection.cursor()
        cursor.execute(sql_query)
        db_connection.commit()
    except sqlite3.Error as db_error:
           print(db_error)
   
def update_record(db_connection,sql_query):
    try:    
        cursor = db_connection.cursor()
        cursor.execute(sql_query)
        db_connection.commit()
    except sqlite3.Error as db_error:
           print(db_error)

def delete_record(db_connection, sql_query):
    try:
        cursor = db_connection.cursor()
        cursor.execute(sql_query)
        db_connection.commit()
    except sqlite3.Error as db_error:
           print(db_error)

def delete_all_records(db_connection, sql_query):
    try:
        cursor = db_connection.cursor()
        cursor.execute(sql_query)
        db_connection.commit()
    except sqlite3.Error as db_error:
           print(db_error)


def select_all_records(db_connection, sql_query):
    try:
        cursor = db_connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as db_error:
           print(db_error)

def select_record_by_id(db_connection, sql_query):
    try:
        cursor = db_connection.cursor()
        cursor.execute(sql_query) 
        rows = cursor.fetchall()
        for row in rows:
            return row
    except sqlite3.Error as db_error:
           print(db_error)

def close_connection(db_connection):
    db_connection.close()





























