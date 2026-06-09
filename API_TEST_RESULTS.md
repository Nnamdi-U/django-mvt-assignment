# API Testing Notes

I tested the API on June 8, 2026 using Docker and curl.

## Departments

- `GET /api/departments/` returned 200.
- `POST /api/departments/` created a department and returned 201.
- `GET /api/departments/<id>/` returned the department and its courses.

## Courses

- `GET /api/courses/` returned 200 and used pagination.
- Filtering by department returned only courses from that department.
- Searching for a course title returned the matching course.
- `POST /api/courses/` returned 201 for valid course data.
- `PATCH /api/courses/<id>/` updated the course.

I also tested invalid course data:

- Credits set to `0` returned 400 with `Credits must be greater than 0.`
- Level set to `999` returned 400 with
  `Level must be 100, 200, 300, 400, or 500.`

## Students

- `GET /api/students/` returned 200.
- Searching by student number returned the correct student.
- `POST /api/students/` returned 201 for valid student data.
- `PATCH /api/students/<id>/` updated the enrollment year.
- Reusing the same email returned 400 because email must be unique.

## Enrollments

- `GET /api/enrollments/` returned 200.
- `POST /api/enrollments/` created an enrollment and returned 201.
- `PATCH /api/enrollments/<id>/` changed the status to completed.
- Posting the same student and course again returned 400.
- Trying to enroll in an inactive course returned 400.

Duplicate enrollment response:

```json
{
  "non_field_errors": [
    "This student is already enrolled in this course."
  ]
}
```

Inactive course response:

```json
{
  "course": [
    "Students cannot enroll in an inactive course."
  ]
}
```

## Audit Logs

After creating courses, students, and enrollments, I checked:

```text
GET /api/audit-logs/
```

The API contained automatically created logs. The enrollment log included the
student number and course code.

I also tried `POST /api/audit-logs/`. It returned 405 because audit logs are
read-only through the API.

The temporary department, courses, student, and enrollment used during testing
were deleted after the tests.
