import psycopg2

def connect_db():
    assessment_db_connect = psycopg2.connect(
        host="localhost",
        database="assessment1",
        user="postgres",
        password="password",
        port = "5432" 
    )
    print("connected")
    return assessment_db_connect


connected_to_db = True
while connected_to_db:
    connect_db()
    print("Welcome to the assessment database! \n")
    a = input("type 'quit' to exit the databse: ").lower().strip()
    if a == "quit":
        connect_db()
        connected_to_db = False