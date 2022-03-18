"""

authentication.py
----------------
Contains the user credentials verification function called for implementing basic auth for the APIs
This file is intended to be the placeholder for any configurations or future security enhancements

"""

from flask_httpauth import HTTPBasicAuth
from configuration import USER_NAME, PASSWORD

# Creating an instance of HTTP Basic auth class. This will be used across all APIs to provide security with basic auth
auth = HTTPBasicAuth()


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return username == USER_NAME and password == PASSWORD

