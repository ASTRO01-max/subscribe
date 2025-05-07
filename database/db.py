import psycopg2

def add_user(username):
    conn = psycopg2.connect("dbname=subscribe user=postgres password=1234")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS chanel (
            id SERIAL PRIMARY KEY,
            channel VARCHAR(40)
        );
    """)

    cur.execute("INSERT INTO chanel(channel) VALUES (%s);", (username,))

    conn.commit()
    cur.close()
    conn.close()

def get_users():
    conn = psycopg2.connect("dbname=subscribe user=postgres password=1234")
    cur = conn.cursor()

    cur.execute("SELECT * FROM chanel;")
    users = cur.fetchall()

    cur.close()
    conn.close()

    return users
