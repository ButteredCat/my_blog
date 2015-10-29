#!/usr/bin/env python

import os

SITE_PACKAGES = 'site-packages/'
BUNDLES = 'bundles/'
LIBS = (
        BUNDLES+'django-pagedown/pagedown/',


       )

def main():
    for each in LIBS:
        os.system('cp -r %s %s' % (each, SITE_PACKAGES))
    os.system('tar -zcv --exclude-from .tarignore -f ../deploy.tar.gz \
                -C %s .' % (os.getcwd()))
    os.system('rm -rf %s' % (SITE_PACKAGES + 'pagedown'))


if __name__=='__main__':
    main()
