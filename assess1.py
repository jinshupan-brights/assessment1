import psycopg2

def connect_db():
    assessment_db_connect = psycopg2.connect(
        host="localhost",
        database="assessment1",
        user="postgres",
        password="password",
        port = "5432" 
    )
    return assessment_db_connect


def fetch_db_data():
    cursor = connect_db().cursor()
    cursor.execute(f"SELECT * FROM contacts;")
    db_data = cursor.fetchall()
    cursor.close()
    return db_data


def insert_db_data(f_name, l_name):
    cursor = connect_db().cursor()
    cursor.execute(f"INSERT INTO contacts (first_name, last_name, title, organization) VALUES ('{f_name}','{l_name}', null, null);")
    cursor.execute("COMMIT;")
    cursor.close()
    print(f"{f_name},{l_name} has been inserted into the database! ")


def delete_db_data(l_name):
    cursor = connect_db().cursor()
    cursor.execute(f"DELETE FROM contacts WHERE last_name = '{l_name}';")
    cursor.close()
    print(f"The contact {l_name} has been removed! ")


def disconnect():
    connect_db().close()
    print("Disconnected from the database. Good bye!")


connect_db()
print('''Welcome to the assessment database!
Type [list] to list all data.
Type [insert] to add new entry to the database.
Type [delete] to remove an entry from the database.
Or type [quit] to exit the databse..
''')

connected_to_db = True
while connected_to_db:
    a = input('''Please enter your command - 
    available commands are [list], [insert], [delete], and [quit]: ''').lower().strip()

    if a == "list":
        db_data_list = fetch_db_data()
        for row in db_data_list:
            print(str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[4]))
    elif a == "quit":
        connect_db().cursor().execute("COMMIT;") # commits all changes before quitting
        disconnect() 
        connected_to_db = False
    elif a == "insert":
        f_name = input("please enter the first name: ").capitalize().strip()
        l_name = input("please enter the last name: ").capitalize().strip()
        insert_db_data(f_name, l_name)
    elif a == "delete":
        l_name = input("please enter the contact's last name: ").capitalize().strip()
        delete_db_data(l_name)