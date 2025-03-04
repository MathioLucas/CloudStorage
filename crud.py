
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
def create_file(file_name: str, file_type: str, file_size: int, file_path: str, owner_id: int, folder_id: int = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO files (file_name, file_type, file_size, file_path, owner_id, folder_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id
        """,
        (file_name, file_type, file_size, file_path, owner_id, folder_id),
    )
    file_id = cursor.fetchone()[0]  
    conn.commit()
    cursor.close()
    conn.close()
    return file_id  
