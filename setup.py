"""
SQLAlchemy-Versioned
--------------------

Versioning and auditing extension for SQLAlchemy.
"""

from setuptools import setup, Command
import subprocess


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)

setup(
    name='SQLAlchemy-Versioned',
    version='0.1',
    url='https://github.com/kvesteri/sqlalchemy-i18n',
    license='BSD',
    author='Konsta Vesterinen',
    author_email='konsta@fastmonkeys.com',
    description='Versioning and auditing extension for SQLAlchemy.',
    long_description=__doc__,
    packages=['sqlalchemy_versioned'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'SQLAlchemy>=0.8',
        'SQLAlchemy-Utils>=0.12.1'
    ],
    cmdclass={'test': PyTest},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
