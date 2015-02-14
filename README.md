# askreduce

distributed questions

---

initial setup with just `intro_python` material

`intro_python.md` is CSQ (Colon-Separated Questions)

`csq2fix.py` converts to Django fixtures format, in JSON

that output goes in `shufflesort/fixtures` to be loaded

to set up fresh:

```bash
python manage.py flush
python manage.py loaddata intro_python
```
