#!/usr/bin/env python

import os


VIRTUALENV = 'env'
SITE_PACKAGES_DST = 'site-packages/'
SITE_PACKAGES_SRC = VIRTUALENV + '/lib/python2.7/site-packages/'
APPS = (
        'pagedown',
        'markdown2.py',
        'django_admin_bootstrapped',
        'solo', 
        'pygments',
       )
LIBS = [SITE_PACKAGES_SRC + EACH_APP for EACH_APP in APPS]


def collect_static():
    os.system('python manage.py collectstatic')

def prepare():
    collect_static()
    for each in LIBS:
        os.system('cp -r %s %s' % (each, SITE_PACKAGES_DST))

def package():
    os.system('tar -zcv --exclude-vcs --exclude-from .tarignore -f ../deploy.tar.gz \
                -C %s .' % (os.getcwd()))
    
def cleanup():
    for each in APPS:
        os.system('rm -rf %s' % (SITE_PACKAGES_DST + each))

def main():
    prepare()
    package()
    cleanup()


if __name__=='__main__':
    main()

