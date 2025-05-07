import psycopg2

def add_user(userame):
    conn = psycopg2.connect("dbname=azamjon user=azamjon password=1111")
    cur = conn.cursor()

    cur.execute(f"INSERT INTO users(chanel) VALUES (%s);", (userame,))


    conn.commit()

    cur.close()
    conn.close()

def get_users():
    conn = psycopg2.connect("dbname=azamjon user=azamjon password=1111")
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()

    conn.commit()

    cur.close()
    conn.close()

    return users