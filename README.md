# User Management System

## Project Overview

This project is a **User Management System** built using **FastAPI (Python)** for the backend and **HTML, CSS, JavaScript, and jQuery AJAX** for the frontend.

The system allows users to register, login, manage profiles, and maintain secure sessions.

The backend integrates multiple databases:

* MySQL for storing user account information
* MongoDB for storing activity logs
* Redis for managing session tokens

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* jQuery (AJAX)

### Backend

* FastAPI (Python)
* Uvicorn

### Databases

* MySQL
* MongoDB
* Redis

### Security

* JWT Authentication
* Password hashing using bcrypt

---

## Features

### User Registration

Users can register using name, email, and password.

Passwords are securely hashed before storing them in the database.

### User Login

Users can login using email and password.
A JWT token is generated after successful login.

### Session Management

Sessions are managed using Redis.
The authentication token is stored in **browser localStorage**.

### Profile Management

Users can:

* View profile information
* Update personal details

### Activity Logging

User actions such as login, logout, and profile updates are logged in MongoDB.

---

## Project Structure

```
project-folder
│
├── backend
│   ├── app.py
│   ├── controller.py
│   ├── models.py
│   ├── services.py
│   └── database.py
│
├── html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── profile.html
│
├── css
│   └── style.css
│
├── js
│   ├── login.js
│   ├── register.js
│   └── profile.js
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repository

```
git clone <your-github-link>
cd project-folder
```

### Install dependencies

```
pip install -r requirements.txt
```

### Start required services

Make sure the following services are running:

* MySQL
* MongoDB
* Redis

### Run the backend server

```
python app.py
```

or

```
uvicorn app:app --reload --port 5000
```

Server will start at:

```
http://localhost:5000
```

---

## API Endpoints

Register User

```
POST /api/register
```

Login User

```
POST /api/login
```

Get Profile

```
GET /api/profile
```

Update Profile

```
PUT /api/profile
```

Logout

```
POST /api/logout
```

---

## Deployment

Deployment has not been completed yet.
Currently the application runs locally using FastAPI.

---

## Author

Ganesh B
