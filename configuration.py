"""
configuration.py
-----------
Contains the configurable parameters for our APIs like database path and API authentication credentials.
To make flask app run, please configure database path, API username and API password below.
"""

"""
DATABASE_URL_DEV - Insert a string like postgresql://username:password@localhost/LMS_DB inside the empty string
E.g -
DATABASE_URL_DEV = 'postgresql://username:password@localhost/LMS_DB'
where 'LMS_DB' is name of local postgreSQL DB  and <username> and <password> are the DB credentials
"""

DATABASE_URL_DEV = ''

"""
USER_NAME - Needed for HTTP Basic auth. Insert the API username inside the empty string
E.g -
USER_NAME = 'admin'
"""

USER_NAME = ''

"""
PASSWORD - Needed for HTTP Basic auth. Insert the API password inside the empty string
E.g -
PASSWORD = 'password'
"""

PASSWORD = ''




