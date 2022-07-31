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

def add_event(name, day, month):
    cur.execute("INSERT INTO reminders VALUES('{}',{},{});".format(name, day, month))
    print("EVENT ADDED SUCCESSFUL!")
    con.commit()

 # select_event function bascially selects the event with current_date.   

def select_event():
    cur.execute("SELECT name,day,month FROM reminders WHERE extract(day from CURRENT_DATE)=day AND extract(month from CURRENT_DATE)=month;")
    
    con.commit()    

# remove_event function bascially removes an event if already exists in the table
def remove_event():
    cur.execute("IF name,day,month EXISTS DELETE FROM reminders ")
    print("THE EVENT ALREADY EXISTS SO REMOVED")
    con.commit()   

if __name__ == "__main__" :
    con = connect_todatabase('reminders')    
    cur = getcursor(con)
    r = add_event('birthday', 30, 7)
    z = select_event()







