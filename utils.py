"""

utils.py
--------
Contains utility functions mostly validation of incoming json field values

"""

from constants import MISSING_NAME, MISSING_MAND_DATA, MISSING_MAND_FIELDS, INVALID_DATA


# Function check if incoming JSON body fields are invalid, returns True if JSON data is invalid, False if all OK
def invalid_user_fields(json):

    try:
        # Checking if required fields are sent with blank values
        blank_field_check = '' in (str(json['name']), json['phone_number'], str(json['location']), str(json['time_zone']),
                               str(json['visa_status']))
        if blank_field_check:
            return {'invalid': True, 'message':  MISSING_MAND_DATA}

        # Checking if first and last names are sent
        comma_check = ',' not in str(json['name'])

        if comma_check:
            return {'invalid': True, 'message': MISSING_NAME}

        # Checking if linkedin url, time-zome or visa status are invalid
        linkedin = str(json['linkedin_url'])
        linkedin_check = linkedin and 'https://www.linkedin.com/' not in linkedin
        timezone_check = str(json['time_zone']) not in ['PST', 'MST', 'CST', 'EST', 'IST']
        visa_check = str(json['visa_status']) not in ['Not-Specified', 'NA', 'GC-EAD', 'H4-EAD', 'H4',
                                                      'H1B', 'Canada-EAD', 'Indian-Citizen',
                                                      'US-Citizen', 'Canada-Citizen']

        if linkedin_check or timezone_check or visa_check:
            return {'invalid': True, 'message': INVALID_DATA}

        # Checking if invalid alphanumeric name
        alnum_name_check = False

        for c in str(json['name']):
            if c.isdigit():
                alnum_name_check = True
                break

        if alnum_name_check:
            return {'invalid': True, 'message': INVALID_DATA}

        # Checking if invalid phone number
        phone_alnum_check = False
        for c in str(json['phone_number']):
            if c.isalpha():
                phone_alnum_check = True
                break

        phone_len_check = len(str(json['phone_number'])) < 10

        if phone_alnum_check or phone_len_check:
            return {'invalid': True, 'message': INVALID_DATA}
    except KeyError:
        return {'invalid': True, 'message': MISSING_MAND_FIELDS}

    # Incoming data is valid
    return {'invalid': False, 'message': 'All valid'}
