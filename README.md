# my_blog
A django blog system deployed on Sina App Engine (SAE).

* Running on [http://www.butteredcat.org](http://www.butteredcat.org)
* Based on Django 1.8.
* Inspired by [Andrew Liu](https://www.gitbook.com/book/andrew-liu/django-blog/details).

## Before Use
* Generate a [`SECRET_KEY`](https://docs.djangoproject.com/en/dev/ref/settings/#secret-key) in `my_blog/settings.py`. As the variable name implies, you should always keep it a secrect.
* Fill the user name and password of your local MySQL database in my_blog/settings.py if you want to debug on localhost, and make sure you do have a MySQL installed.
* Update `ALLOWED_HOSTS` and `STATIC_URL` in `my_blog/settings.py`.
* Change `short_name` in `templates/duoshuo.html` to your own. You can get one in [Duoshuo](http://duoshuo.com).
