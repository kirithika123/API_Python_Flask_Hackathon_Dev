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

DATABASE_URL = 'postgres://zobnofgthtlngf:e9ad1f6a91579c6a309aa680ee5fe433bdb8a3ac8b8c12e6aaa7c2a4a80d7e31@ec2-52-201-124-168.compute-1.amazonaws.com:5432/d20mmumha6j046'

"""
USER_NAME - Needed for HTTP Basic auth. Insert the API username inside the empty string
E.g -
USER_NAME = 'admin'
"""

USER_NAME = 'APIPROCESSING'

"""
PASSWORD - Needed for HTTP Basic auth. Insert the API password inside the empty string
E.g -
PASSWORD = 'password'
"""

PASSWORD = '2xx@Success'




