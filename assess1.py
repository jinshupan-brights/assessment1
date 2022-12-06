import psycopg2

assessment_db_connect = psycopg2.connect(
    host="localhost",
    database="assessment1",
    user="postgres",
    password="password",
    port = "5432" 
)

connected_to_db = True
while connected_to_db:
    print("Welcome to the assessment database! \n")
    a = input("type 'quit' to exit the databse: ").lower().strip()
    if a == "quit":
        assessment_db_connect.close()
        connected_to_db = False