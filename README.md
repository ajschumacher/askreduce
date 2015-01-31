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
