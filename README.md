# 🚀 AI Prompt Library

A full-stack web application to manage and organize AI prompts with secure authentication.

---

## 📌 Project Overview

AI Prompt Library is a modern web application that allows users to create, view, update, and delete AI prompts.
It includes secure JWT-based authentication and a clean, responsive UI.

---

## ✨ Features

* 🔐 JWT Authentication (Login & Secure API access)
* ➕ Add new AI prompts
* 📄 View all prompts
* ✏️ Edit existing prompts
* ❌ Delete prompts
* 🔍 Search and filter prompts
* 🎯 Complexity level tagging
* 💻 Responsive and modern UI

---

## 🛠️ Tech Stack

### Frontend

* Angular
* TypeScript
* HTML5 & CSS3

### Backend

* Django
* Django REST Framework
* JWT Authentication (SimpleJWT)

### Database

* SQLite (can be upgraded to PostgreSQL)

---

## 📂 Project Structure

```
ai-prompt-library/
│
├── backend/
│   ├── prompts/
│   ├── config/
│   └── manage.py
│
├── frontend/
│   ├── src/
│   └── angular files
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 Backend Setup

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs on:

```
http://127.0.0.1:8000/
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
ng serve
```

Frontend runs on:

```
http://localhost:4200/
```

---

## 🔐 Authentication (JWT)

* Login API:

```
POST /api/token/
```

* Response:

```
access token + refresh token
```

* Token is used for secure API requests.

---

## 📡 API Endpoints

| Method | Endpoint         | Description     |
| ------ | ---------------- | --------------- |
| GET    | /api/prompts/    | Get all prompts |
| POST   | /api/prompts/    | Create prompt   |
| PUT    | /api/prompts/:id | Update prompt   |
| DELETE | /api/prompts/:id | Delete prompt   |

---

## 🌐 Future Improvements

* ⭐ Favorite prompts feature
* 📊 User dashboard
* 🌍 Deployment (Live hosting)
* 👥 Multi-user support
* 🔎 Advanced filtering

---

## 📸 Screenshots

*Add your UI screenshots here*

---

## 👨‍💻 Author

**Muzammil**

* GitHub: https://github.com/Muzammill44

---

## 📄 License

This project is open-source and free to use.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

---
