from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='moira-python-client',
    version='2.6.0',
    description='Client for Moira - Alerting system based on Graphite data',
    keywords='moira monitoring client metrics alerting',
    long_description="""
        Moira is a real-time alerting tool, based on Graphite data.
        moira-client is a python client for Moira API.
        Key features:
        - create, update, delete, manage triggers
        - create, delete, update subscriptions
        - manage tags, patterns, notifications, events, contacts
    """,
    author = 'Alexander Lukyanchenko',
    author_email = 'al.lukyanchenko@gmail.com',
    packages=[
        'moira_client',
        'moira_client.models'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

        'Operating System :: OS Independent',
        'Intended Audience :: Developers',

        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Topic :: System :: Monitoring',

        "License :: OSI Approved :: MIT License"
    ],
    url='https://github.com/moira-alert/python-moira-client',
    install_requires=required
)
