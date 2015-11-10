#!/usr/bin/env python

import os

SITE_PACKAGES = 'site-packages/'
BUNDLES = 'bundles/'
APPS = (
        ('pagedown', 'django-pagedown/pagedown/'),
        ('markdown2.py', 'python-markdown2/lib/markdown2.py'),
        ('django_admin_bootstrapped',
            'django-admin-bootstrapped/django_admin_bootstrapped/'),
        ('solo', 'django-solo/solo/'),
       )
APP_NAMES = [EACH_APP[0] for EACH_APP in APPS]
LIBS = [BUNDLES + EACH_APP[1] for EACH_APP in APPS]


def collect_static():
    os.system('python manage.py collectstatic')

def prepare():
    collect_static()
    for each in LIBS:
        os.system('cp -r %s %s' % (each, SITE_PACKAGES))

def package():
    os.system('tar -zcv --exclude-from .tarignore -f ../deploy.tar.gz \
                -C %s .' % (os.getcwd()))
    
def cleanup():
    for each in APP_NAMES:
        os.system('rm -rf %s' % (SITE_PACKAGES + each))

def main():
    prepare()
    package()
    cleanup()


if __name__=='__main__':
    main()

