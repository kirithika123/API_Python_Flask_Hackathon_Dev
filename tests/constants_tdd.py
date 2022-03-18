"""
constants_tdd.py
----------------
constants needed across the TDD test scripts.

"""

# Test DB used during TDD - an empty DB called 'TEST' must be created in DB before running the test scripts
DATABASE_URL_TEST = 'postgresql://postgres:password@localhost/TEST'

# Constants for test_users_resource.py
NUM_USERS_IN_DB = 5
USER_ID_TO_GET = "U01"
USER_ID_TO_PUT = "U05"
USER_ID_TO_DELETE = 'U05'
USER_ID_TO_DELETE_NOTEXIST = 'U2021'
USER_NAME_TO_GET = "Harry,Potter"
USER_PHONE_TO_GET = 1112223333
USER_LOC_TO_GET = "New Jersey"
USER_TIMEZONE_TO_GET = "EST"
USER_LINKED_TO_GET = "https://www.linkedin.com/HarryPotter"
INVALID_USERID_1 = "A@12xy"
INVALID_USERID_2 = "NULL"
INVALID_USER_FIXTURE ="user123"
INVALID_PWD_FIXTURE = "pwd123"

# Constants for test_userskillsmap_resource.py
QUERY_USER_ID = '?user_id=U01'
QUERY_USER_ID_STR = '?user_id=\'U01\''
QUERY_SKILL_ID = '?skill_id=1'
QUERY_SKILL_ID_STR = '?skill_id=\'1\''
QUERY_USER_ID_NOT_EXIST = '?user_id=U1000'
QUERY_SKILL_ID_NOT_EXIST = '?skill_id=1000'

# Constants for test_skills_resource.py
NUM_SKILLS_IN_DB = 5
SKILL_TO_POST = "Git"
SKILL_TO_POST_DUP = "PYTHON"
SKILL_TO_PUT = "TESTING"
SKILL_ID_TO_PUT = 4
SKILL_TO_PUT_DUP = "javascript"
SKILL_ID_TO_PUT_DUP = 1
SKILL_ID_TO_GET = 2
SKILL_ID_TO_TEST_INV = 3
DECIMAL_SKILL_ID = 4.5
SKILL_NAME_TO_TEST_1 = "Selenium"
NON_EXISTING_SKILL_ID = 2021
INVALID_SKILLID = "A@12xy"
SKILL_ID_TO_DELETE = 5
ALPHA_SKILL_ID = "a1b2"


# Constants for test_userskills_resource.py
INVALID_USER = "welcome"
INVALID_PWD = "abc"

NUM_USERSKILLS_IN_DB = 5
USERSKILLID_GET = "US02"
USER_ID_GET = "U01"
SKILL_ID_GET = 4
MONTHS_OF_EXP_GET = 24

USERID_POST = "U03"
SKILL_ID_POST = 2
MONTHS_OF_EXP_POST= 36
USERID_POST_EXIST = "U01"
SKILL_ID_POST_EXIST = 1

USERSKILLID_PUT = "US05"
USER_ID_PUT = "U04"
SKILL_ID_PUT = 1
MONTHS_OF_EXP_PUT = 28

INVAD_MONTHS_OF_EXP_4 = "abc123"

USERSKILLID_DEL = "US05"
INVALID_USERSKILLID = "US1000"


