# Django MVT Assignment

Beginner University Course Directory project.

## Run the project

Start Docker Desktop first, then run:

```bash
docker compose up --build
```

Open:

- Home: http://localhost:8000/
- Departments: http://localhost:8000/departments/
- Admin: http://localhost:8000/admin/

## Create migrations

Complete the `Student` model in `students/models.py` first, then run:

```bash
docker compose run --rm web python manage.py makemigrations
```

## Apply migrations

```bash
docker compose run --rm web python manage.py migrate
```

## Create a superuser

```bash
docker compose run --rm web python manage.py createsuperuser
```

## Add sample data

Use the admin panel to create at least:

- 3 departments
- 6 courses
- 5 students

## Pages

- `/` - Home page
- `/departments/` - Department list page
- `/departments/<id>/` - Department detail page
- `/courses/<id>/` - Course detail page
- `/admin/` - Django admin panel
