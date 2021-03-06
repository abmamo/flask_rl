"""
Flask-RL
-------------

flask rate limiter
"""
from setuptools import setup


setup(
    name='Flask-RL',
    version='1.0',
    url='http://http://github.com/abmamo/flask_rl',
    license='BSD',
    author='Abenezer Mamo',
    author_email='contact@abmamo.com',
    description='flask rate limiter',
    long_description=__doc__,
    py_modules=['flask_rl'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        "Flask==2.0.1",
        "pickleDB==0.9.2",
    ],
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
