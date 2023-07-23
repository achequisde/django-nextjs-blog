# django-nextjs-blog

Test blog using django as a REST API (with djangorestframework) with NextJS in the frontend.

## Requirements

- python
- pipenv
- node

## How to run

- Django server must run on port `8000` and NextJS server must run on port `3000`

### Backend

1. Run `pipenv install` inside the root folder
2. Run `pipenv shell` and then within the virtual environment:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    ```

### Frontend

1. Run `npm install` inside the *front* folder and then `npm run dev`

## Routes

### Authors

- authors/ - Accepts **GET** (get all authors) and **POST** (add new author) requests

### Posts

- posts/ - Accepts **GET** (get all posts) and **POST** (add new posts) requests
- posts/[postId] - Accepts **GET**, **PUT**, and **DELETE** requests

## Models

### Authors

An author object contains an integer `id` and a string `name`

```json
{
    "id": 1,
    "name": "John Smith"
}
```

- POST requests should only specify the `name` attribute

### Posts

A post object contains an integer `id`, a string `title`, a string `extract`, a string `content`, a datetime `created`, and an Author `author`

```json
{
    "id": 1,
    "title": "...",
    "extract": "...",
    "content": "...",
    "created": "2023-07-23T11:47:26.161004Z",
    "author": {
        "id": 1,
        "name": "John Smith"
    }
}
```

- POST requests should only specify `title`, `content`, and `author` attributes

## Adding more posts

- Go to `http://localhost:8000/admin`

