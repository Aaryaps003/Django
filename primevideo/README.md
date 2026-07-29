# Prime Video Clone

This Django project is a starting point for an Amazon Prime Video-style clone.

## Setup

1. Install the required Python dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

2. Apply migrations:

   ```bash
   python manage.py migrate
   ```

3. Run the development server:

   ```bash
   python manage.py runserver
   ```

4. Open http://127.0.0.1:8000/ in your browser.

## What was added

- Fixed project settings and application routing.
- Added `app` as the main Django app.
- Added a `Movie` model and admin registration.
- Added a dynamic homepage using `templates/Home.html`.
- Added a movie detail page at `/movies/<id>/`.
- Added a JSON endpoint for movie data at `/movies/`.
