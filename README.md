# askreduce

From scratch with Django, following the [tutorial](https://docs.djangoproject.com/en/1.7/intro/tutorial01/).

Steps:

```bash
django-admin.py startproject askreduce
```

This makes `askreduce/askreduce` (the full depth) so I think I don't need another containing directory.

Setting up a Postgres database, `pip` installed [psycopg](http://initd.org/psycopg/) and created database manually as:

```bash
psql -c "create database askreduce;"
```

Edited [settings.py](askreduce/settings.py) to have the right settings for `DATABASES`.

Edited [settings.py](askreduce/settings.py) to have the right setting for `TIME_ZONE`. (Select from [this list](http://en.wikipedia.org/wiki/List_of_tz_database_time_zones); I used "America/New_York".)

Initial database migration for the default Django applications (like `django.contrib.sessions`):

```bash
python manage.py migrate
```

Now there's a bunch of stuff in the `askreduce` database. Can check out the list of tables like this:

```bash
psql
\c askreduce
\d
```

Now there's also a `__pycache__` directory that shows up, so I'll start a [.gitignore](.gitignore).

Sure enough, there's HTTP happening now when you do this:

```bash
python manage.py runserver
```

And now, to make an app where the magic will happen... with a clever (?) name:

```bash
python manage.py startapp shufflesort
```
