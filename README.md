# Flask User Registration App

A simple Flask web application that provides user registration functionality with MySQL database integration, password hashing, and Bootstrap styling.

## Requirements

- Python 3.7+
- MySQL Server
- pip (Python package manager)

## Setup Guide

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup MySQL Database
Create a MySQL database and table using the provided SQL file:
```bash
mysql -u your_username < setup_db.sql
```
Note: Default username is `root`

### 3. Run the Application
```bash
python app.py
```

Access the application at `http://localhost:5000`

