# FastAPI Blog API

A simple blog backend built using FastAPI for learning purposes.

## Features
- User authentication (JWT)
- CRUD operations for blogs
- Protected routes
- SQLite database

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- JWT

## Run locally
```bash
pip install -r requirements.txt
uvicorn blog.main:app --reload
