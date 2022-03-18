"""
    test_utils.py
    ------------
    TDD test cases to test utility functions mostly validation of incoming json field values

"""

from utils import invalid_user_fields
from constants import MISSING_NAME, MISSING_MAND_DATA, MISSING_MAND_FIELDS, INVALID_DATA


def test_invalid_user_fields_allvalid():
   
    json = {"name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
            "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates",
            "education_ug": "BTech", "education_pg": "Master in SE", "visa_status": "US-Citizen",
            "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == False
    assert result['message'] == 'All valid'


def test_invalid_user_fields_miss_keys():
    json = {"name": "Bill,Gates", "location": "Silicon Valley",
            "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
            "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == MISSING_MAND_FIELDS


def test_invalid_user_fields_blankname():

    json = {"name": "", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == MISSING_MAND_DATA


def test_invalid_user_fields_blankphone():

    json = {"name": "Bill,Gates", "phone_number": "", "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == MISSING_MAND_DATA


def test_invalid_user_fields_blanklocation():

    json = {"name": "Bill,Gates", "phone_number": 1112223333, "location": "",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == MISSING_MAND_DATA


def test_invalid_user_fields_blanktimezone():

    json = {"name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == MISSING_MAND_DATA


def test_invalid_user_fields_blankvisastatus():

    json = {"name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == MISSING_MAND_DATA


def test_invalid_user_fields_nocommaname():

    json = {"name": "Bill", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == MISSING_NAME


def test_invalid_user_fields_alnumname():

    json = {"name": "Bill123,G222", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == INVALID_DATA


# def test_invalid_user_fields_alnumloc():
#
#     json = {"name": "Tom,Cruise", "phone_number": 1112223333, "location": "Silicon Valley111",
#                        "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
#                        "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
#     result = invalid_user_fields(json)
#     assert result is True


def test_invalid_user_fields_inv_linkedin():

    json = {"name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
            "time_zone": "PST", "linkedin_url": "https://www.linkedin.co", "education_ug": "BTech",
            "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == INVALID_DATA


def test_invalid_user_fields_inv_timezone():

    json = {"name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
            "time_zone": "hello", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
            "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == INVALID_DATA


def test_invalid_user_fields_inv_visastatus():

    json = {"name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
            "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
            "education_pg": "Master in SE", "visa_status": "hello", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == INVALID_DATA


def test_invalid_user_fields_inv_phonelen():

    json = {"name": "Bill,Gates", "phone_number": 1112223, "location": "Silicon Valley",
            "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
            "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == INVALID_DATA


def test_invalid_user_fields_alnum_phone():
    json = {"name": "Bill,Gates", "phone_number": "abc123hi", "location": "Silicon Valley",
            "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
            "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    result = invalid_user_fields(json)
    assert result['invalid'] == True
    assert result['message'] == INVALID_DATA

