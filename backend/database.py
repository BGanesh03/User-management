import mysql.connector
from pymongo import MongoClient
import redis
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# -----------------------------
# MySQL (Railway)
# -----------------------------
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_PORT = os.getenv("MYSQL_PORT", 3306)

# -----------------------------
# Redis (Upstash)
# -----------------------------
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

# -----------------------------
# MongoDB (Railway / Atlas)
# -----------------------------
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client[MONGO_DB]
logs = mongo_db["logs"]

# -----------------------------
# Mongo Logging Function
# -----------------------------
def log_action(email, action):
    logs.insert_one({
        "email": email,
        "action": action,
        "time": datetime.datetime.utcnow()
    })

# -----------------------------
# MySQL Connection
# -----------------------------
def get_db():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        port=MYSQL_PORT
    )

# -----------------------------
# Initialize MySQL Tables
# -----------------------------
def init_db():
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