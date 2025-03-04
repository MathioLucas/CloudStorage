
import psycopg2
from database import get_db_connection  

def create_user(name: str, email: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id",
        (name, email, password),
    )
    user_id = cursor.fetchone()[0] 
    conn.commit()
    cursor.close()
    conn.close()
    return user_id
