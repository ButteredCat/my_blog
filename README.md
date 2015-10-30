# my_blog
A django blog system deployed on Sina App Engine (SAE).

* Running on [http://www.butteredcat.org](http://www.butteredcat.org)
* Based on Django 1.8.
* Inspired by [Andrew Liu](https://www.gitbook.com/book/andrew-liu/django-blog/details).

## Installation
    git clone https://github.com/ButteredCat/my_blog.git
    cd my_blog
    git submodule init
    git submodule update

## Debug on localhost
* Create your local MySQL database.
* Create a `sensitive.py` in `my_blog`, in which you define 4 variables: [`SECRET_KEY`](https://docs.djangoproject.com/en/dev/ref/settings/#secret-key), `LOCAL_DB`, `LOCAL_DB_USER` and `LOCAL_DB_PASS`.
* Customise `ALLOWED_HOSTS` and `STATIC_URL` in `my_blog/settings.py`.
* Change `short_name` in `templates/duoshuo.html` to your own. You can get one in [Duoshuo](http://duoshuo.com).
* Setup database with django migration tool.
* Runserver.

## Deploy on SAE
* Run `pack.py` to package code and static files.
* Export local database.
* Upload package and database file to SAE.
