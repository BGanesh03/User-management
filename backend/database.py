import mysql.connector
from pymongo import MongoClient
import redis
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

# Redis
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["user_db"]
logs = mongo_db["logs"]

def log_action(email, action):
    logs.insert_one({
        "email": email,
        "action": action,
        "time": datetime.datetime.utcnow()
    })

# MySQL
def get_db():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

def init_db():
    conn = mysql.connector.connect(host="localhost", user="root", password="")
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS user_db")
    conn.close()

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(100) UNIQUE,
        password VARCHAR(255),
        name VARCHAR(100)
    )
    """)
    conn.commit()
    conn.close()