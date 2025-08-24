# Library Management System (Flask + MySQL)

A resume-ready web app to manage library books, members, and book transactions.

## Features
- Admin & staff login
- Book management (CRUD)
- Member management (CRUD)
- Issue & return books
- Dashboard KPIs (total books, members, issued books)
- Bootstrap UI, flash messages
- Overdue & fine tracking

## Tech Stack
- Python, Flask
- MySQL
- mysql-connector-python
- python-dotenv

## Setup
1. Clone & setup venv
2. Create MySQL DB using `db.sql`
3. Copy `.env.example` to `.env` and fill credentials
4. Install dependencies: `pip install -r requirements.txt`
5. Run app: `flask --app app run --debug`
6. Create admin via setup route with token

