from fastapi import APIRouter, HTTPException, Depends
from models import Register, Login
from database import get_db, log_action, redis_client
from services import get_user, SECRET
import bcrypt
import jwt
import datetime

router = APIRouter(prefix="/api")

# REGISTER
@router.post("/register")
def register(data: Register):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE email=%s", (data.email,))
    if cur.fetchone():
        raise HTTPException(400, "User exists")

    hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())

    cur.execute(
        "INSERT INTO users (email, password, name) VALUES (%s,%s,%s)",
        (data.email, hashed.decode(), data.name)
    )
    conn.commit()

    log_action(data.email, "register")
    return {"msg": "Registered"}

# LOGIN
@router.post("/login")
def login(data: Login):
    conn = get_db()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM users WHERE email=%s", (data.email,))
    user = cur.fetchone()

    if not user:
        raise HTTPException(400, "Invalid")

    if not bcrypt.checkpw(data.password.encode(), user["password"].encode()):
        raise HTTPException(400, "Invalid")

    token = jwt.encode({
        "email": data.email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, SECRET, algorithm="HS256")

    redis_client.set(data.email, token)

    log_action(data.email, "login")

    return {"token": token}

# PROFILE
@router.get("/profile")
def profile(email=Depends(get_user)):
    conn = get_db()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT email,name FROM users WHERE email=%s", (email,))
    return cur.fetchone()

# UPDATE PROFILE
@router.put("/profile")
def update_profile(data: dict, email=Depends(get_user)):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET name=%s WHERE email=%s",
        (data.get("name"), email)
    )
    conn.commit()

    log_action(email, "update_profile")

    return {"msg": "Profile updated"}