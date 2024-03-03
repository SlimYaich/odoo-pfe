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
        'Babel>=2.9.1',
        'chardet==4.0.0',
        'cryptography==3.4.8',
        'decorator==4.4.2',
        'docutils==0.17',
        'ebaysdk==2.1.5',
        'freezegun==1.1.0',
        'geoip2==2.9.0',
        'gevent==21.8.0 ; python_version == "3.10"',
        'gevent==22.10.2; python_version > "3.10"',
        'greenlet==1.1.2 ; python_version == "3.10"',
        'greenlet==2.0.2 ; python_version > "3.10"',
        'idna==2.10',
        'Jinja2==3.0.3 ; python_version <= "3.10"',
        'Jinja2==3.1.2 ; python_version > "3.10"',
        'libsass==0.20.1',
        'lxml==4.8.0 ; python_version <= "3.10"',
        'lxml==4.9.2 ; python_version > "3.10"',
        'MarkupSafe==2.0.1 ; python_version <= "3.10"',
        'MarkupSafe==2.1.2 ; python_version > "3.10"',
        'num2words==0.5.10',
        'ofxparse==0.21',
        'passlib==1.7.4',
        'Pillow==9.0.1 ; python_version <= "3.10"',
        'Pillow==9.4.0 ; python_version > "3.10"',
        'polib==1.1.1',
        'psutil==5.9.0 ; python_version <= "3.10"',
        'psutil==5.9.4 ; python_version > "3.10"',
        'psycopg2==2.9.2 ; sys_platform != "win32" and python_version <= "3.10"',
        'psycopg2==2.9.5 ; python_version > "3.10" or sys_platform == "win32"',
        'pydot==1.4.2',
        'pyopenssl==21.0.0',
        'PyPDF2==1.26.0 ; python_version <= "3.10"',
        'PyPDF2==2.12.1 ; python_version > "3.10"',
        'pypiwin32 ; sys_platform == "win32"',
        'pyserial==3.5',
        'python-dateutil>=2.8.2',
        'python-ldap==3.4.0 ; sys_platform != "win32"',
        'python-stdnum==1.17',
        'pytz',
        'pyusb==1.2.1',
        'qrcode==7.3.1',
        'reportlab==3.6.8 ; python_version <= "3.10"',
        'reportlab==3.6.12 ; python_version > "3.10"',
        'requests==2.25.1',
        'rjsmin==1.1.0',
        'urllib3==1.26.5',
        'vobject==0.9.6.1',
        'Werkzeug==2.0.2',
        'xlrd==1.2.0',
        'XlsxWriter==3.0.2',
        'xlwt==1.3.*',
        'zeep==4.1.0',
        'nltk==3.8.1',
        'scikit-learn==1.4.1.post1',
        'pandas==2.2.0',
        'tika==2.6.0',
    ],
    python_requires='>=3.10',
    extras_require={
        'ldap': ['python-ldap'],
    },
    tests_require=[
        'freezegun==1.1.0',
    ],
)
