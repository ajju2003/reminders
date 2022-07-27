import psycopg2
DB_NAME='reminders'
DB_user='arjun'



"""
TODO:
1. fix select statement
2. write it in functions
    - connect_to_db
    - create_table
    - add_event
    - remove_event
    - list_events()
"""

# connection= psycopg2.connect(dbname=DB_NAME,user=DB_user)
# cur=connection.cursor()
# cur.execute('CREATE TABLE IF NOT EXISTS reminders(name text,day int,month int); ')
# r = cur.execute("INSERT INTO reminders VALUES('ram',25,7);")
# print(r)
# r = cur.execute('SELECT * FROM reminders;')
# print(r)
# connection.commit()
# connection.close()



if __name__ == "__main__":
    ...