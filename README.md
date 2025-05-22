# 📚 FastAPI Books API

This is a RESTful API built using FastAPI and SQLAlchemy to query and filter Project Gutenberg books. It supports filters like book ID, language, MIME type, topic, author, and title with pagination support.

---

## 🌟 Features

- 🔍 Filtering by:
  - Book ID(s)
  - Language(s)
  - MIME Type(s)
  - Author
  - Title
  - Topic (Subject or Bookshelf)
- 📃 Pagination with next/previous page links
- 🧾 Swagger UI at `/docs`
- ✅ Response model validation using Pydantic
- 🐳 Optional Docker-based setup for easy deployment

---

## ⚙️ Option 1: Local Setup (Without Docker)

### 🧱 Prerequisites

- Python 3.8+
- PostgreSQL running locally or remotely
- (Optional) Create a `.env` file for DB URL:

  ```env
  DATABASE_URL=postgresql://<username>:<password>@localhost:5432/gutenberg
  ```

### 🧪 Setup Instructions

1. **Clone the repo**:

   ```bash
   git clone https://github.com/sahil-bukkam/glutenberg.git
   cd your_project
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations and start the app**:

   ```bash
   uvicorn app.main:app --reload
   ```

5. **Visit the API**:

   > http://localhost:8000/docs

---

## 🐳 Option 2: Docker Setup

### 🔧 Prerequisites

- Docker
- Docker Compose

### 🐳 Docker Quick Start

1. **Create a `.env` file** in the root:

   ```env
   POSTGRES_USER=sahil
   POSTGRES_PASSWORD=sahil123
   POSTGRES_DB=gutenberg
   DATABASE_URL=postgresql://sahil:sahil123@db:5432/gutenberg
   ```

2. **Start the containers**:

   ```bash
   docker-compose up --build -d
   ```

3. **Wait for PostgreSQL to initialize**, then access:

   > http://localhost:8000/docs

4. **Stop the app**:

   ```bash
   docker-compose down
   ```

---

## 📥 Importing Data

If you have a SQL dump of the Gutenberg dataset:

```bash
cat path/to/dump.sql | docker exec -i <db_container> psql -U sahil -d gutenberg
```

Replace `<db_container>` with the actual container name (e.g., `your_project_db_1`).

---

## ⚙️ Useful Docker Commands

- View logs:

  ```bash
  docker-compose logs -f app
  ```

- Rebuild everything:

  ```bash
  docker-compose down -v
  docker-compose up --build -d
  ```

---

## 📘 API Usage

Sample endpoint with filters:

```
GET /api/books/?language=en,fr&book_id=123,456&page=2&page_size=20
```

### Swagger Docs

> http://localhost:8000/docs

---

## 📝 License

MIT © Your Name
