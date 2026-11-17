<div align="center">

# 🎓 Student Management System

A simple web-based application for managing student records with **FastAPI**, **SQLite**, and **Jinja2**.

[Features](#-features) · [Installation](#-installation) · [Routes](#-application-routes) · [Project structure](#-project-structure)

</div>

---

## 📌 Overview

The Student Management System provides a centralized interface to create, view, update, and delete student records. It demonstrates CRUD operations, HTML form handling, data validation, SQLite integration, and server-rendered pages.

### Built with

| Technology | Purpose |
| --- | --- |
| Python | Backend programming |
| FastAPI | Web framework and route handling |
| SQLite3 | Database storage |
| Pydantic | Data validation |
| Jinja2 | Dynamic HTML templates |
| HTML5 and CSS3 | Page structure and styling |
| Uvicorn | Development server |

## ✨ Features

- **Add students** with personal and academic information.
- **View all students** on the dashboard and open individual student details.
- **Update student records** through a pre-filled form.
- **Delete student records** from the database.
- **Validate data** with Pydantic models.
- **Manage attendance status** for students.
- **Render dynamic pages** with Jinja2 templates.

## 📂 Project Structure

```text
Student-managment-system/
├── main.py
├── students.db                 # Created/used by the application
├── requirements.txt
├── .gitignore
├── README.md
└── templates/
    ├── create-std.html
    ├── home.html
    ├── single-std.html
    └── update.html
```

## ⚙️ Installation

### Prerequisites

- Python installed and available on your `PATH`.
- Git.

### 1. Clone the repository

```bash
git clone https://github.com/ramcharan18-lab/Student-managment-system.git
cd Student-managment-system
```

### 2. Create and activate a virtual environment

**Windows (Command Prompt):**

```bat
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
uvicorn main:app --reload
```

Open <http://127.0.0.1:8000/> in your browser.

## 🗄️ Database

The application uses SQLite. The database file is `students.db`, and its `students` table is created automatically when the application starts.

| Column | Type | Description |
| --- | --- | --- |
| `id` | INTEGER | Unique, auto-incrementing primary key |
| `name` | TEXT | Student name |
| `age` | INTEGER | Student age |
| `gender` | TEXT | Student gender |
| `marks` | INTEGER | Student marks |
| `course` | TEXT | Student course |
| `image` | TEXT | Student image reference |
| `status` | INTEGER | Student attendance status |

## 🔗 Application Routes

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Display all students |
| `GET` | `/student/add` | Display the student registration form |
| `POST` | `/student/add` | Add a student |
| `GET` | `/students/{std_id}` | Display an individual student's details |
| `GET` | `/sdts/update/{std_id}` | Display the student update form |
| `POST` | `/student/update/{std_id}` | Update a student record |
| `GET` | `/std/{std_id}` | Delete a student record |

> **Please verify the route paths against `main.py` before publishing.** The update and delete paths above are reproduced from the project information provided.

## ✅ Validation

The `Student` Pydantic model is documented with these validation rules:

| Field | Rule |
| --- | --- |
| `name` | 3–30 characters |
| `age` | 18–30 |
| `gender` | Up to 10 characters |
| `marks` | 1–100 |
| `course` | 3–20 characters |
| `image` | String |
| `status` | Integer |

## 🖼️ Screenshots

Add the corresponding image files to a `screenshots/` directory to display them here.

| Screen | Preview |
| --- | --- |
| Student dashboard | `screenshots/dashboard.png` |
| Add student form | `screenshots/add-student.png` |
| Student details | `screenshots/student-details.png` |
| Update student form | `screenshots/update-student.png` |

When those files are present in the repository, you can replace this table with images, for example:

```markdown
![Student dashboard](screenshots/dashboard.png)
```

## 🚀 Possible Improvements

- Add student search and pagination.
- Add authentication and authorization.
- Improve form error handling and validation feedback.
- Enhance the dashboard and attendance management.

## 👨‍💻 Author

**Ramcharan** — Python Full Stack Development Learner

- GitHub: [@ramcharan18-lab](https://github.com/ramcharan18-lab)
- Project: [Student Management System](https://github.com/ramcharan18-lab/Student-managment-system)

## 🙏 Acknowledgements

Thanks to **Saibalaji Sir** for his guidance and support, and to **Innomatics Research Labs** and **Full Stack Experts Academy** for the learning opportunity.

---

<div align="center">

⭐ If you find this project useful, explore the repository and share your feedback.

</div>
