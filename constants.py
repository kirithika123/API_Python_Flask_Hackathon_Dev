"""
    constants.py
    ------------
    Contains the constants needed for the APIs- Endpoints and a few error messages to be returned in JSON

"""

# Endpoints
USERS_ENDPOINT = "/Users"
SKILLS_ENDPOINT = "/Skills"
USERSKILLS_ENDPOINT = "/UserSkills"
USERSKILLS_MAPPING_ENDPOINT = "/UserSkillsMap"

# Error messages
MISSING_MAND_FIELDS = 'missing mandatory fields'
MISSING_MAND_DATA = 'missing mandatory data-name, phone number, location, time zone or visa status'
MISSING_NAME = 'missing either first or last names'
INVALID_DATA = 'invalid data'

USR_CREATE_SUCCESS = 'User record successfully created'
USR_UPDATE_SUCCESS = 'User record successfully updated'

FAILED_TO_CREATE = 'Failed to create'
FAILED_TO_UPDATE = 'Failed to update'

