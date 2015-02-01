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

Add some model specifications in [models.py](shufflesort/models.py).

Add `shufflesort` to the `INSTALLED_APPS` in [settings.py](askreduce/settings.py).

Yikes; `__pycache__` directories are showing up all over. Time to expand their exclusion in [.gitignore](.gitignore).

Okay; time to make a migration:

```bash
python manage.py makemigrations shufflesort
```

The tutorial includes these diagnostic/interesting commands for reference:

```bash
python manage.py sqlmigrate shufflesort 0001
python manage.py check
```

But now it's time to actually migrate and be ready to do stuff:

```bash
python manage.py migrate
```

This is how you get a local console to play with the database and so on:

```bash
python manage.py shell
```

It's a normal shell, much like the equivalent in Rails (`rails console`)...

```python
from shufflesort.models import Question, Answer
from django.utils import timezone
q = Question(user="Aaron", text="What is the deal?", date=timezone.now())
q.save()
# etc.
```

As recommended by the tutorial, add `__str__` methods to [models.py](shufflesort/models.py).

Wow, there's a good deal of underscore magic.

```python
Question.objects.get(date__year=2015)
q.answer_set.create(text="Something!", user="Aaron", date=timezone.now())
# and things have a `.delete`
```


The tutorial [continues](https://docs.djangoproject.com/en/1.7/intro/tutorial02/) with the Django admin interface...


```bash
python manage.py createsuperuser
```

This seems to only affect the database.

Models show up in the admin after being registered in [admin.py](shufflesort/admin.py).

Wow you can do quite a lot with the admin interface... Could even use it as a general db editing platform for whatever data entry/maintenance you want to do. Hmm! I wonder how it handles contentious editing; is this a concern?


The tutorial [continues](https://docs.djangoproject.com/en/1.7/intro/tutorial03/) with views...


Looks like as a placeholder adding a `HttpResponse` `index` function in [views.py](shufflesort/views.py). Then adding a [urls.py](shufflesort/urls.py) in [shufflesort/](shufflesort/) though we already have [urls.py](askreduce/urls.py) in [askreduce/](askreduce/). Ah, we edit [that one](askreduce/urls.py) as well. Now there's a response at `/shufflesort/`. Yup, can do all the good things with routes.

Sure enough it's easy to grab stuff from the database.

Templating works as expected. A little surprising it's conventional to bury things so deep as [askreduce/shufflesort/templates/shufflesort/](askreduce/shufflesort/templates/shufflesort/). And the `django.shortcuts.render` is nice.
