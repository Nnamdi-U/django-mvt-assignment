# API Test Results

Date tested: June 8, 2026

The API was tested locally with Docker, PostgreSQL, and `curl`.

```bash
docker compose up --build
docker compose exec web python manage.py migrate
```

## Results

| Test | Request | Expected | Actual |
| --- | --- | --- | --- |
| Department list | `GET /api/departments/` | 200 | 200 |
| Create department | `POST /api/departments/` | 201 | 201 |
| Department detail | `GET /api/departments/12/` | 200 | 200 |
| Create active course | `POST /api/courses/` | 201 | 201 |
| Create inactive course | `POST /api/courses/` | 201 | 201 |
| Course list | `GET /api/courses/` | 200 | 200 |
| Filter courses | `GET /api/courses/?department=12` | 200 | 200 |
| Search courses | `GET /api/courses/?search=Programming%20Test%20232408` | 200 | 200 |
| Course detail | `GET /api/courses/16/` | 200 | 200 |
| Reject zero credits | `POST /api/courses/` | 400 | 400 |
| Reject invalid level | `POST /api/courses/` | 400 | 400 |
| Patch course | `PATCH /api/courses/16/` | 200 | 200 |
| Create student | `POST /api/students/` | 201 | 201 |
| Student list | `GET /api/students/` | 200 | 200 |
| Search students | `GET /api/students/?search=S232408` | 200 | 200 |
| Student detail | `GET /api/students/11/` | 200 | 200 |
| Reject duplicate email | `POST /api/students/` | 400 | 400 |
| Patch student | `PATCH /api/students/11/` | 200 | 200 |
| Create enrollment | `POST /api/enrollments/` | 201 | 201 |
| Enrollment list | `GET /api/enrollments/` | 200 | 200 |
| Enrollment detail | `GET /api/enrollments/5/` | 200 | 200 |
| Reject duplicate enrollment | `POST /api/enrollments/` | 400 | 400 |
| Reject inactive course | `POST /api/enrollments/` | 400 | 400 |
| Patch enrollment status | `PATCH /api/enrollments/5/` | 200 | 200 |
| Audit log list | `GET /api/audit-logs/?action=enrollment_created` | 200 | 200 |
| Audit log detail | `GET /api/audit-logs/7/` | 200 | 200 |
| Reject audit log creation | `POST /api/audit-logs/` | 405 | 405 |

All tests passed. The IDs above belonged to temporary test records. The department,
courses, student, and enrollment were deleted after the test.

## Response Examples

Course list pagination fields:

```json
{
  "count": 8,
  "next": "http://localhost:8000/api/courses/?page=2",
  "previous": null
}
```

Course with zero credits:

```json
{
  "credits": [
    "Credits must be greater than 0."
  ]
}
```

Course with an invalid level:

```json
{
  "level": [
    "Level must be 100, 200, 300, 400, or 500."
  ]
}
```

Duplicate student email:

```json
{
  "email": [
    "student with this email already exists."
  ]
}
```

Duplicate enrollment:

```json
{
  "non_field_errors": [
    "This student is already enrolled in this course."
  ]
}
```

Inactive course enrollment:

```json
{
  "course": [
    "Students cannot enroll in an inactive course."
  ]
}
```

Audit log created by the enrollment signal:

```json
{
  "id": 7,
  "action": "enrollment_created",
  "model_name": "Enrollment",
  "object_id": 5,
  "message": "Student S232408 enrolled in P232408."
}
```

Manual audit log creation:

```json
{
  "detail": "Method \"POST\" not allowed."
}
```
