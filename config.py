import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "library_system"),
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def get_secret_key():
    return os.getenv("FLASK_SECRET", "change_me")
