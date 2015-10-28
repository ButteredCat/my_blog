# my_blog
A django blog system deployed on Sina App Engine (SAE).

* Running on [http://www.butteredcat.org](http://www.butteredcat.org)
* Based on Django 1.8.
* Inspired by [Andrew Liu](https://www.gitbook.com/book/andrew-liu/django-blog/details).

## Before Use
* Create a `sensitive.py` in `my_blog`, in which you define 3 variables: [`SECRET_KEY`](https://docs.djangoproject.com/en/dev/ref/settings/#secret-key), `LOCAL_DB_USER` and `LOCAL_DB_PASS`.
* Customise `ALLOWED_HOSTS` and `STATIC_URL` in `my_blog/settings.py`.
* Change `short_name` in `templates/duoshuo.html` to your own. You can get one in [Duoshuo](http://duoshuo.com).
