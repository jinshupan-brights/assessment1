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


def fetch_db_data(a):
    cursor = connect_db().cursor()
    cursor.execute(f"SELECT * FROM assessment1_7;")
    db_data = cursor.fetchall()
    cursor.close()
    return db_data


def disconnect():
    connect_db().close()
    print("Disconnected from the database. Good bye!")

connect_db()
print('''Welcome to the assessment database!\n
Type [list] to list all data.
Or type [quit] to exit the databse''')

connected_to_db = True
while connected_to_db:
    a = input("Please enter your command: ").lower().strip()
    if a == "list":
        db_data_list = fetch_db_data(connect_db)
        for row in db_data_list:
            print(row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + row[3])
    elif a == "quit":
        disconnect()
        connected_to_db = False
    