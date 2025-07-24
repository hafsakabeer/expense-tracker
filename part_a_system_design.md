# EDTECH ASSIGNMENT TRACKER – PART A: SYSTEM DESIGN

Name: Hafsa K.H  
Role: Full Stack Tech Intern (Applicant)  
Date: July 23, 2025
Email: hafsakabeer369@gmail.com


## 1. Core Entities and Relationships

The system is built using three core entities: `User`, `Assignment`, and `Submission`. These represent teachers, students, tasks assigned by teachers, and the responses submitted by students.

### User Table

| Field      | Type     | Description                |
|-----------|----------|----------------------------|
| id        | Integer  | Primary Key                |
| username  | String   | Unique login name          |
| email     | String   | User's email               |
| password  | String   | Hashed password            |
| role      | String   | 'student' or 'teacher'     |
| created_at| DateTime | Account creation timestamp |

### Assignment Table

| Field       | Type     | Description                        |
|-------------|----------|------------------------------------|
| id          | Integer  | Primary Key                        |
| title       | String   | Title of the assignment            |
| description | Text     | Assignment details                 |
| due_date    | Date     | Deadline for submission            |
| created_by  | FK       | Linked to teacher (User)           |
| created_at  | DateTime | Assignment creation time           |

### Submission Table

| Field         | Type     | Description                            |
|---------------|----------|----------------------------------------|
| id            | Integer  | Primary Key                            |
| assignment_id | FK       | Foreign key to Assignment              |
| student_id    | FK       | Foreign key to Student (User)          |
| file_upload   | File     | Optional uploaded file or content      |
| submitted_at  | DateTime | Time of submission                     |

---

## 2. API Endpoints

| Action                  | Method | Endpoint                           | Who Can Access |
|-------------------------|--------|------------------------------------|----------------|
| Signup                  | POST   | /signup/                           | Everyone       |
| Login                   | POST   | /login/                            | Everyone       |
| Create assignment       | POST   | /assignments/                      | Teacher only   |
| Submit assignment       | POST   | /assignments/<id>/submit/          | Student only   |
| View submissions        | GET    | /assignments/<id>/submissions/     | Teacher only   |

---

## 3. Teacher Creates an Assignment

- Teacher logs in and sends a POST request to `/assignments/`

```json
{
  "title": "Math Homework",
  "description": "Solve 10 problems from Chapter 4",
  "due_date": "2025-07-30"
}
```

---

## 4. Student Submits an Assignment

- Student sends a POST request to `/assignments/1/submit/`

```json
{
  "file": "my_homework.pdf"
}
```

---

## 5. Teacher Views Submissions

- Teacher sends GET request to `/assignments/1/submissions/`

```json
[
  {
    "student": "Ayesha",
    "submitted_at": "2025-07-22T14:30",
    "file_url": "http://..."
  }
]
```

---

## 6. Authentication Strategy

- Role is set during signup (student or teacher)
- Stored in user table
- Backend restricts access based on roles
- Uses session or token-based authentication

---

## 7. Suggestions for Scaling

- Use PostgreSQL instead of SQLite
- Store files in AWS S3 or similar cloud storage
- Switch to JWT token-based auth for APIs
- Use Celery for background tasks like email alerts
- Add Swagger/OpenAPI docs for API testing
- Use React or Vue for frontend scaling
- Deploy via Render, Heroku, or AWS
