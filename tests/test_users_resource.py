"""
    test_users_resource.py
    ----------------------
    TDD test cases built from gherkins for the Users API.
    These functions test the get, post, put and delete methods
    of UsersResource Class which are the units to be built to support url/Users and ur/Users/<id> endpoints
"""

from constants import USERS_ENDPOINT
from .constants_tdd import NUM_USERS_IN_DB, USER_ID_TO_GET, USER_ID_TO_PUT, USER_ID_TO_DELETE,\
    USER_NAME_TO_GET, USER_PHONE_TO_GET, USER_LOC_TO_GET, \
    USER_TIMEZONE_TO_GET, USER_LINKED_TO_GET, INVALID_USERID_1, INVALID_USERID_2, USER_ID_TO_DELETE_NOTEXIST
from constants import MISSING_NAME, MISSING_MAND_DATA, INVALID_DATA, \
    FAILED_TO_CREATE, FAILED_TO_UPDATE


"""
    Test cases for get()
"""


def test_get_all_users(client, valid_auth):
    response = client.get(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth})
    assert len(response.json) == NUM_USERS_IN_DB
    assert response.status_code == 200


def test_get_all_users_unauth_pwd(client, invalid_password):
    response = client.get(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + invalid_password})
    assert response.status_code == 401


def test_get_all_users_unauth_user(client, invalid_user):
    response = client.get(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + invalid_user})
    assert response.status_code == 401


def test_get_all_users_noauth(client):
    response = client.get(f"{USERS_ENDPOINT}")
    assert response.status_code == 401


def test_get_one_user(client, valid_auth):
    response = client.get(f"{USERS_ENDPOINT}/{USER_ID_TO_GET}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 200
    assert response.json['user_id'] == USER_ID_TO_GET
    assert response.json['name'] == USER_NAME_TO_GET
    assert response.json['phone_number'] == USER_PHONE_TO_GET
    assert response.json['location'] == USER_LOC_TO_GET
    assert response.json['time_zone'] == USER_TIMEZONE_TO_GET
    assert response.json['linkedin_url'] == USER_LINKED_TO_GET


def test_get_invalid_userid1(client, valid_auth):
    response = client.get(f"{USERS_ENDPOINT}/{INVALID_USERID_1}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'User Not Found'


def test_get_invalid_userid2(client, valid_auth):
    response = client.get(f"{USERS_ENDPOINT}/{INVALID_USERID_2}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'User Not Found'


def test_get_decimal_userid(client, valid_auth):
    response = client.get(f"{USERS_ENDPOINT}/3.14", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'User Not Found'


def test_get_blank_userid(client, valid_auth):
    response = client.get(f"{USERS_ENDPOINT}/", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404


"""
    Test cases for post()
"""


def test_post_user(client, valid_auth):
    new_user_json = {"name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates",
                       "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_user_json)

    assert response.status_code == 201
    assert (response.json['user_id']).index('U') == 0
    assert response.json['name'] == "Bill,Gates"
    assert response.json['phone_number'] == 1112223333
    assert response.json['location'] == "Silicon Valley"
    assert response.json['time_zone'] == "PST"
    assert response.json['linkedin_url'] == "https://www.linkedin.com/Bill Gates"
    assert response.json['education_ug'] == "BTech"
    assert response.json['education_pg'] == "Master in SE"
    assert response.json['visa_status'] == "US-Citizen"
    assert response.json['comments'] == "CEO of Microsoft"
    assert response.json['message'] == "User record successfully created"


def test_post_user_blank_nullable_fields(client, valid_auth):
    new_user_json = {"name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "", "education_ug": "",
                       "education_pg": "", "visa_status": "US-Citizen", "comments": ""}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_user_json)

    assert response.status_code == 201
    assert (response.json['user_id']).index('U') == 0
    assert response.json['name'] == "Bill,Gates"
    assert response.json['phone_number'] == 1112223333
    assert response.json['location'] == "Silicon Valley"
    assert response.json['time_zone'] == "PST"
    assert response.json['linkedin_url'] == ""
    assert response.json['education_ug'] == ""
    assert response.json['education_pg'] == ""
    assert response.json['visa_status'] == "US-Citizen"
    assert response.json['comments'] == ""
    assert response.json['message'] == "User record successfully created"


def test_post_user_unauth_pwd(client, invalid_password):
    new_user_json = {"name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates",
                       "education_ug": "BTech", "education_pg": "Master in SE", "visa_status": "US-Citizen",
                       "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + invalid_password},
                           json=new_user_json)

    assert response.status_code == 401


def test_post_user_unauth_user(client, invalid_user):
    new_user_json = {"name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates",
                       "education_ug": "BTech", "education_pg": "Master in SE", "visa_status": "US-Citizen",
                       "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + invalid_user},
                           json=new_user_json)

    assert response.status_code == 401


def test_post_user_noauth(client):
    new_user_json = {"name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", json=new_user_json)

    assert response.status_code == 401


def test_post_user_blank_name(client, valid_auth):
    new_user_json = {"name": "", "phone_number": 1112223333, "location": "",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_CREATE}-{MISSING_MAND_DATA}"


def test_post_user_nocomma_name(client, valid_auth):
    new_user_json = {"name": "Bill", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_CREATE}-{MISSING_NAME}"


def test_post_user_alphanumeric_name(client, valid_auth):
    new_user_json = {"name": "Bill123,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_CREATE}-{INVALID_DATA}"


def test_post_user_alphanumeric_loc(client, valid_auth):
    new_user_json = {"name": "Tom,Cruise", "phone_number": 1112223333, "location": "Silicon Valley123",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_user_json)

    assert response.status_code == 201
    assert (response.json['user_id']).index('U') == 0
    assert response.json['name'] == "Tom,Cruise"
    assert response.json['phone_number'] == 1112223333
    assert response.json['location'] == "Silicon Valley123"
    assert response.json['time_zone'] == "PST"
    assert response.json['linkedin_url'] == "https://www.linkedin.com/Bill Gates"
    assert response.json['education_ug'] == "BTech"
    assert response.json['education_pg'] == "Master in SE"
    assert response.json['visa_status'] == "US-Citizen"
    assert response.json['comments'] == "CEO of Microsoft"
    assert response.json['message'] == "User record successfully created"


def test_post_user_blank_phone(client, valid_auth):
    new_user_json = {"name": "Tom,Cruise", "phone_number": '', "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_CREATE}-{MISSING_MAND_DATA}"


def test_post_user_blank_timezone(client, valid_auth):
    new_user_json = {"name": "Brad,Pitt", "phone_number": 99988887777, "location": "Silicon Valley",
                       "time_zone": "", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_CREATE}-{MISSING_MAND_DATA}"


def test_post_user_blank_visa(client, valid_auth):
    new_user_json = {"name": "Brad,Pitt", "phone_number": 99988887777, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "", "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_CREATE}-{MISSING_MAND_DATA}"


def test_post_user_inv_linkedin(client, valid_auth):
    new_user_json = {"name": "Brad,Pitt", "phone_number": 99988887777, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.google.com", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_CREATE}-{INVALID_DATA}"


def test_post_user_inv_timezone(client, valid_auth):
    new_user_json = {"name": "Brad,Pitt", "phone_number": 99988887777, "location": "Silicon Valley",
                       "time_zone": "PST123", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_CREATE}-{INVALID_DATA}"


def test_post_user_inv_visa(client, valid_auth):
    new_user_json = {"name": "Brad,Pitt", "phone_number": 99988887777, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "Golden-Visa", "comments": "CEO of Microsoft"}
    response = client.post(f"{USERS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_CREATE}-{INVALID_DATA}"


"""
    Test Cases for put()
"""


def test_put_user(client, valid_auth):
    update_user_json = {"user_id": USER_ID_TO_PUT, "name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.put(f"{USERS_ENDPOINT}/{USER_ID_TO_PUT}", headers={"Authorization": "Basic " + valid_auth},
                           json=update_user_json)

    assert response.status_code == 201
    assert response.json['user_id'] == USER_ID_TO_PUT
    assert response.json['name'] == "Bill,Gates"
    assert response.json['phone_number'] == 1112223333
    assert response.json['location'] == "Silicon Valley"
    assert response.json['time_zone'] == "PST"
    assert response.json['linkedin_url'] == "https://www.linkedin.com/Bill Gates"
    assert response.json['education_ug'] == "BTech"
    assert response.json['education_pg'] == "Master in SE"
    assert response.json['visa_status'] == "US-Citizen"
    assert response.json['comments'] == "CEO of Microsoft"
    assert response.json['message'] == "User record successfully updated"


def test_put_user_alphanumeric_name(client, valid_auth):
    update_user_json = {"user_id": USER_ID_TO_PUT, "name": "Bill123,Gates", "phone_number": 1112223333,
                        "location": "Silicon Valley", "time_zone": "PST",
                        "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                        "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}

    response = client.put(f"{USERS_ENDPOINT}/{USER_ID_TO_PUT}", headers={"Authorization": "Basic " + valid_auth},
                           json=update_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_UPDATE}-{INVALID_DATA}"


def test_put_user_invalid_phone(client, valid_auth):
    update_user_json = {"user_id": USER_ID_TO_PUT, "name": "Martha,Gates", "phone_number": "abc123fff",
                        "location": "Silicon Valley", "time_zone": "PST",
                        "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                        "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}

    response = client.put(f"{USERS_ENDPOINT}/{USER_ID_TO_PUT}", headers={"Authorization": "Basic " + valid_auth},
                           json=update_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_UPDATE}-{INVALID_DATA}"


def test_put_user_alphanumeric_loc(client, valid_auth):
    update_user_json = {"user_id": USER_ID_TO_PUT, "name": "Tom,Cruise", "phone_number": 1112223333, "location": "Silicon Valley123",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Tom Cruise", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.put(f"{USERS_ENDPOINT}/{USER_ID_TO_PUT}", headers={"Authorization": "Basic " + valid_auth},
                           json=update_user_json)

    assert response.status_code == 201
    assert response.json['name'] == "Tom,Cruise"
    assert response.json['phone_number'] == 1112223333
    assert response.json['location'] == "Silicon Valley123"
    assert response.json['time_zone'] == "PST"
    assert response.json['linkedin_url'] == "https://www.linkedin.com/Tom Cruise"
    assert response.json['education_ug'] == "BTech"
    assert response.json['education_pg'] == "Master in SE"
    assert response.json['visa_status'] == "US-Citizen"
    assert response.json['comments'] == "CEO of Microsoft"
    assert response.json['message'] == "User record successfully updated"


def test_put_user_inv_timezone(client, valid_auth):
    update_user_json = {"user_id": USER_ID_TO_PUT, "name": "Brad,Pitt", "phone_number": 99988887777,
                        "location": "Silicon Valley", "time_zone": "PST123",
                        "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                        "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.put(f"{USERS_ENDPOINT}/{USER_ID_TO_PUT}", headers={"Authorization": "Basic " + valid_auth},
                           json=update_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_UPDATE}-{INVALID_DATA}"


def test_put_user_inv_linkedin(client, valid_auth):
    update_user_json = {"user_id": USER_ID_TO_PUT, "name": "Brad,Pitt", "phone_number": 99988887777,
                        "location": "Silicon Valley", "time_zone": "PST", "linkedin_url": "https://www.google.com",
                        "education_ug": "BTech", "education_pg": "Master in SE", "visa_status": "US-Citizen",
                        "comments": "CEO of Microsoft"}
    response = client.put(f"{USERS_ENDPOINT}/{USER_ID_TO_PUT}", headers={"Authorization": "Basic " + valid_auth},
                           json=update_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_UPDATE}-{INVALID_DATA}"


def test_put_user_inv_visa(client, valid_auth):
    update_user_json = {"user_id": USER_ID_TO_PUT, "name": "Brad,Pitt", "phone_number": 99988887777,
                     "location": "Silicon Valley", "time_zone": "PST",
                     "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                     "education_pg": "Master in SE", "visa_status": "Golden-Visa", "comments": "CEO of Microsoft"}
    response = client.put(f"{USERS_ENDPOINT}/{USER_ID_TO_PUT}", headers={"Authorization": "Basic " + valid_auth},
                           json=update_user_json)

    assert response.status_code == 400
    assert response.json['message'] == f"{FAILED_TO_UPDATE}-{INVALID_DATA}"


def test_put_user_notexist(client, valid_auth):
    update_user_json = {"user_id": INVALID_USERID_1, "name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.put(f"{USERS_ENDPOINT}/{INVALID_USERID_1}", headers={"Authorization": "Basic " + valid_auth},
                           json=update_user_json)

    assert response.status_code == 404
    assert response.json['message'] == 'User Not Found'


def test_put_user_unauth_pwd(client, invalid_password):
    update_user_json = {"user_id": USER_ID_TO_PUT, "name": "Bill,Gates", "phone_number": 1112223333, "location": "Silicon Valley",
                       "time_zone": "PST", "linkedin_url": "https://www.linkedin.com/Bill Gates", "education_ug": "BTech",
                       "education_pg": "Master in SE", "visa_status": "US-Citizen", "comments": "CEO of Microsoft"}
    response = client.put(f"{USERS_ENDPOINT}/{USER_ID_TO_PUT}", headers={"Authorization": "Basic " + invalid_password},
                           json=update_user_json)

    assert response.status_code == 401


"""
    Test cases for delete()
"""


def test_delete_user_existing(client, valid_auth):
    response = client.delete(f"{USERS_ENDPOINT}/{USER_ID_TO_DELETE}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 200
    assert response.json['message'] == 'User record successfully deleted'


def test_delete_user_existing_noauth(client):
    response = client.delete(f"{USERS_ENDPOINT}/{USER_ID_TO_DELETE}", headers={"Authorization": "Basic "})
    assert response.status_code == 401


def test_delete_user_nonexisting(client, valid_auth):
    response = client.delete(f"{USERS_ENDPOINT}/{USER_ID_TO_DELETE_NOTEXIST}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'Failed to delete-user not found'


def test_delete_user_invalid(client, valid_auth):
    response = client.delete(f"{USERS_ENDPOINT}/{INVALID_USERID_1}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'Failed to delete-user not found'





