# University Course Directory

This project started as a Django MVT website for viewing university departments
and courses. Part 2 adds a Django REST Framework API for departments, courses,
students, enrollments, and audit logs.

## Run the project

Start Docker Desktop first, then run:

```bash
docker compose up --build
```

If the Python requirements change, rebuild the image:

```bash
docker compose build
```

The Docker build installs the packages listed in `requirements.txt`, including
Django REST Framework and django-filter.

## Database setup

Create and apply migrations:

```bash
docker compose run --rm web python manage.py makemigrations
docker compose run --rm web python manage.py migrate
```

Create an admin user:

```bash
docker compose run --rm web python manage.py createsuperuser
```

The admin page is available at:

```text
http://localhost:8000/admin/
```

## Website pages

- Home: http://localhost:8000/
- Departments: http://localhost:8000/departments/
- Department detail: `http://localhost:8000/departments/<id>/`
- Courses: http://localhost:8000/courses/
- Course detail: `http://localhost:8000/courses/<id>/`
- Admin: http://localhost:8000/admin/

## API routes

- `/api/departments/`
- `/api/courses/`
- `/api/students/`
- `/api/enrollments/`
- `/api/audit-logs/`

List endpoints use page-number pagination with five records per page. The API
also supports the filtering, searching, and ordering options required by the
assignment.

## Serializers

Serializers convert Django model objects into JSON and validate JSON sent to the
API. Related model IDs are used when creating records. Readable fields such as
department name, course title, and student name are included in responses.

The department detail serializer includes the courses that belong to the
department. The audit log serializer is read-only.

## Signals

Django signals create audit logs when a course, student, or enrollment is
created. The signals are loaded from `registrations/apps.py` when Django starts.

## Enrollment transaction

Enrollment creation uses `transaction.atomic()`. The enrollment and its audit
log are saved together. If audit logging fails, the enrollment is rolled back.

## Example requests

Valid enrollment request:

```json
{
  "student": 1,
  "course": 1,
  "status": "active"
}
```

Example response:

```json
{
  "id": 1,
  "student": 1,
  "student_name": "Samir Yehia",
  "course": 1,
  "course_title": "Introduction to Programming",
  "course_code": "CSC101",
  "status": "active"
}
```

Invalid course request:

```json
{
  "department": 1,
  "title": "Invalid Course",
  "course_code": "CSC000",
  "description": "This course has invalid credits.",
  "credits": 0,
  "level": 100,
  "is_active": true
}
```

This request returns `400 Bad Request` because credits must be greater than
zero.

```json
{
  "credits": [
    "Credits must be greater than 0."
  ]
}
```

## Testing

The browsable API can be opened at:

```text
http://localhost:8000/api/
```

An endpoint can also be tested with curl:

```bash
curl http://localhost:8000/api/courses/
```

The valid and invalid API tests performed for this assignment are recorded in
`API_TEST_RESULTS.md`.
