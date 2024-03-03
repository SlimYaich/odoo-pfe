#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from os.path import join, dirname


exec(open(join(dirname(__file__), 'odoo', 'release.py'), 'rb').read())  # Load release variables
lib_name = 'odoo'

setup(
    name='odoo',
    version=version,
    description=description,
    long_description=long_desc,
    url=url,
    author=author,
    author_email=author_email,
    classifiers=[c for c in classifiers.split('\n') if c],
    license=license,
    scripts=['setup/odoo'],
    packages=find_packages(),
    package_dir={'%s' % lib_name: 'odoo'},
    include_package_data=True,
    install_requires=[
        'babel >= 1.0',
        'chardet',
        'cryptography',
        'decorator',
        'docutils',
        'ebaysdk',
        'freezegun',  # Ajout de freezegun
        'geoip2',
        'gevent',
        'greenlet',
        'idna',
        'Jinja2',
        'libsass',
        'lxml',
        'MarkupSafe',
        'num2words',
        'ofxparse',
        'passlib',
        'Pillow',
        'polib',
        'psutil',
        'psycopg2',
        'pydot',
        'pyopenssl',
        'PyPDF2',
        'pypiwin32',
        'pyserial',
        'python-dateutil',  # Modification de la version
        'python-ldap',
        'python-stdnum',
        'pytz',
        'pyusb',
        'qrcode',
        'reportlab',
        'rjsmin',
        'requests',
        'urllib3',
        'vobject',
        'Werkzeug',
        'xlrd',
        'XlsxWriter',
        'xlwt',
        'zeep',
    ],
    python_requires='>=3.10',
    extras_require={
        'ldap': ['python-ldap'],
    },
    tests_require=[
        'freezegun',
    ],
)
