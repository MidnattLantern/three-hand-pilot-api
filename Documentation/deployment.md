Flynarc use PostgreSQL as its data storage. https://customer.elephantsql.com/instance
The URL is found inside the details of flyanrc-api. Keep this URL secret!

Flynarc is deployed on Heroku
1. Inside settings, click "Reveal Config Vars", the key is `DATABASE_URL` the value is the URL link from PostgreSQL

2. Back at IDE, run this in terminal:
`
pip3 install dj_database_url==0.5.0 psycopg2
`

3. In settings.py import dj_database_url underneath `import os`
`import dj_database_url`

4. In settings.py update DATABASES to this:
`
if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
`
Connecting to the local database during development, and PostgreSQL for deployment.

5. In IDE env.py add this:
`os.environ['DATABASE_URL'] = "<your PostgreSQL URL here>"`

6. To wire up Flynarc to PostgreSQL, comment-disable `os.environ['DEV'] = '1'`

7. Add a print statement in the else block for DATABASES, then run `python3 manage.py makemigrations --dry-run` if the console says the print string, you're wired.

8. Migrate, create a new superuser

9. Back at PostgreSQL, click Browser, in the table queries list, pick "auth_user (public)", then execute. The superuser name you created should appear.

- Flynarc use gunicorn as part of deployment
10. In terminal, run:
`pip3 install gunicorn django-cors-headers`

11. freeze:
`pip3 freeze > requirements.txt`

12. Create a Procfile and add the content:
`
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn flynarc_api.wsgi
`

13. Add the Heroku link to allowed hosts

14. Add corsheaders to the top of MIDDLEWARE:
`'corsheaders.middleware.CorsMiddleware',`

15. Add the following block underneath the MIDDLEWARE library:
`
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://.*\.gitpod\.io$",
    ]
`

16. Add this underneath (allowing cookies):
`CORS_ALLOW_CREDENTIALS = True`

17. Add to the bottom to the JWT_AUTH group:
`JWT_AUTH_SAMESITE = 'None'`

18. Change the secret key to:
`SECRET_KEY = os.getenv('SECRET_KEY')`
Make up a new secret key that is different from the original. In env.py:
`os.environ.setdefault("SECRET_KEY", "(name of the new secret key)")`

19. Uncomment the 'env = 1' in env.py

20. Ensure the requirements are up to date:
`pip3 freeze > requirements.txt`

21. Add these config variables on Heroku:
1. KEY: `CLOUDINARY_URL`
1. VALUE: `cloudinary://...`

2. KEY: `DATABASE_URL`
2. VALUE: `postgres://...`


3. KEY: `DISABLE_COLLECTSTATIC`
3. VALUE: `1`

4. KEY: `SECRET_KEY`
4. VALUE: (the same from IDE env.py)

5. KEY: `ALLOWED_HOST`
5. VALUE: (url to deployed API)

22. Then connect to Github repository

During front-end devlopment, it can be helpful to keep the debug true to find errors. This isn't recomended however and should be a last plan c thing.