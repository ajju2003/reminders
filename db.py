import psycopg2

def connect_todatabase(dbname):
    return  psycopg2.connect(database=dbname, user='arjun',password='')

def getcursor(con):
    return con.cursor()

# create_table function creats a table with coloumns name,day,month

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS reminders(name text, day int, month int);")
    con.commit()

# add _event function basically adds, information to the reminders table

def add_event(cur, event_name, day, month):
    cur.execute("INSERT INTO reminders VALUES('{}',{},{});".format(event_name, day, month))
    print("EVENT ADDED SUCCESSFUL!")
    con.commit()

 # select_event function bascially selects the event with current_date.   

def select_events(cur, within_days):
    query=("SELECT DISTINCT name,day,month FROM reminders WHERE day>extract(day from CURRENT_DATE) AND day<extract(day from CURRENT_DATE)+{} AND extract(month from CURRENT_DATE)=month;".format(within_days))
    cur.execute(query)
    events = cur.fetchall()
    con.commit()
    return events


if __name__ == "__main__" :
    con = connect_todatabase('reminders')    
    cur = getcursor(con)
    r = add_event(cur, 'r_birtday',11,8)
    events = select_events(cur, 2)
    print(events)









