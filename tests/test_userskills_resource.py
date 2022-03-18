"""
    test_userskills_resource.py
    ---------------------------
    TDD test cases built from gherkins for the UserSkills API.
    These functions test the get, post, put and delete methods
    of UseSkillsResource Class which are the units to be built to support url/UserSkills and ur/UserSkills/<id> endpoints
"""
from constants import USERSKILLS_ENDPOINT
from .constants_tdd import NUM_USERSKILLS_IN_DB, INVALID_USERSKILLID, USERSKILLID_DEL, USERSKILLID_GET, USER_ID_GET, SKILL_ID_GET, \
    MONTHS_OF_EXP_GET, USER_ID_PUT, USERSKILLID_PUT, SKILL_ID_PUT, MONTHS_OF_EXP_PUT, INVAD_MONTHS_OF_EXP_4,\
    USERID_POST, SKILL_ID_POST, MONTHS_OF_EXP_POST, USERID_POST_EXIST, SKILL_ID_POST_EXIST


""" ------------------Test cases for Get method ()---------------------------"""


def test_get_all_userskills_unauth_pwd(client, invalid_password):
    response = client.get(f"{USERSKILLS_ENDPOINT}", headers={"Authorization": "Basic " + invalid_password})
    assert response.status_code == 401


def test_get_all_userskills_unauth_user(client, invalid_user):
    response = client.get(f"{USERSKILLS_ENDPOINT}", headers={"Authorization": "Basic " + invalid_user})
    assert response.status_code == 401


def test_get_all_userskills_noauth(client):
    response = client.get(f"{USERSKILLS_ENDPOINT}")
    assert response.status_code == 401


def test_get_all_userskills(client, valid_auth):
    response = client.get(f"{USERSKILLS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth})
    assert len(response.json['UserSkillMapping']) == NUM_USERSKILLS_IN_DB
    assert response.status_code == 200


def test_get_one_userskills(client, valid_auth):
    response = client.get(f"{USERSKILLS_ENDPOINT}/{USERSKILLID_GET}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 200
    assert response.json['user_skill_id'] == USERSKILLID_GET
    assert response.json['user_id'] == USER_ID_GET
    assert response.json['Skill_id'] == SKILL_ID_GET
    assert response.json['months_of_exp'] == MONTHS_OF_EXP_GET


def test_get_invalid_userskillid(client, valid_auth):
    response = client.get(f"{USERSKILLS_ENDPOINT}/{INVALID_USERSKILLID}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'User Skill Mapping Not Found'


def test_get_decimal_userskillid(client, valid_auth):
    response = client.get(f"{USERSKILLS_ENDPOINT}/9.9", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'User Skill Mapping Not Found'


def test_get_alphanumeric_userskillid(client, valid_auth):
    response = client.get(f"{USERSKILLS_ENDPOINT}/abc123", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'User Skill Mapping Not Found'


""" ------------------Test cases for Post method ()---------------------------"""


def test_post_userskills(client, valid_auth):
    create_userskill_json = {"user_id": USERID_POST, "Skill_id": SKILL_ID_POST, "months_of_exp": MONTHS_OF_EXP_POST}
    response = client.post(f"{USERSKILLS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=create_userskill_json)
    assert response.status_code == 201
    assert (response.json['user_skill_id']).index('US') == 0
    assert response.json['user_id'] == USERID_POST
    assert response.json['Skill_id'] == SKILL_ID_POST
    assert response.json['months_of_exp'] == MONTHS_OF_EXP_POST
    assert response.json['message'] == 'Successfully Created'


def test_post_alphnumkillid(client, valid_auth):
    create_userskill_json = {"user_id": "U09", "Skill_id": "abc123", "months_of_exp": 17}
    response = client.post(f"{USERSKILLS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=create_userskill_json)
    assert response.status_code == 400
    assert response.json['message'] == 'Failed to create due to invalid skill Id'


def test_post_nullskillid(client, valid_auth):
    create_userskill_json = {"user_id": "U09", "Skill_id": "", "months_of_exp": 17}
    response = client.post(f"{USERSKILLS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=create_userskill_json)
    assert response.status_code == 400
    assert response.json['message'] == 'Failed to create due to invalid data'


def test_post_nulluserid(client, valid_auth):
    create_userskill_json = {"user_id": "", "Skill_id": 2, "months_of_exp": 17}
    response = client.post(f"{USERSKILLS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=create_userskill_json)
    assert response.status_code == 400
    assert response.json['message'] == 'Failed to create due to invalid data'


def test_post_alphnumexperience(client, valid_auth):
    create_userskill_json = {"user_id": "U09", "Skill_id": 6, "months_of_exp": "abc123"}
    response = client.post(f"{USERSKILLS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=create_userskill_json)
    assert response.status_code == 400
    assert response.json['message'] == 'Failed to create due to invalid months of experience'


def test_post_nullexperience(client, valid_auth):
    create_userskill_json = {"user_id": "U09", "Skill_id": 6, "months_of_exp": ""}
    response = client.post(f"{USERSKILLS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=create_userskill_json)
    assert response.status_code == 400
    assert response.json['message'] == 'Failed to create due to invalid data'


def test_post_existingid(client, valid_auth):
    create_userskill_json = {"user_id": USERID_POST_EXIST, "Skill_id": SKILL_ID_POST_EXIST, "months_of_exp": 18}
    response = client.post(f"{USERSKILLS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=create_userskill_json)
    assert response.status_code == 400
    assert response.json['message'] == 'Failed to create as UserSkillMap already exists'


""" ------------------Test cases for Put method ()---------------------------"""


def test_put_userskills(client, valid_auth):
    update_userskill_json = {"months_of_exp": MONTHS_OF_EXP_PUT}

    response = client.put(f"{USERSKILLS_ENDPOINT}/{USERSKILLID_PUT}", headers={"Authorization": "Basic " + valid_auth},
                          json=update_userskill_json)
    assert response.status_code == 201
    assert response.json['user_skill_id'] == USERSKILLID_PUT
    assert response.json['user_id'] == USER_ID_PUT
    assert response.json['Skill_id'] == SKILL_ID_PUT
    assert response.json['months_of_exp'] == MONTHS_OF_EXP_PUT
    assert response.json['message'] == 'Successfully Updated'


def test_put_invaliduserskills(client, valid_auth):
    update_userskill_json = {"months_of_exp": MONTHS_OF_EXP_PUT}

    response = client.put(f"{USERSKILLS_ENDPOINT}/{INVALID_USERSKILLID}", headers={"Authorization": "Basic " + valid_auth},
                          json=update_userskill_json)
    assert response.status_code == 404
    assert response.json['message'] == 'User Skill Mapping Not Found'


def test_put_userskills_invalidexp(client, valid_auth):
    update_userskill_json = {"months_of_exp": INVAD_MONTHS_OF_EXP_4}

    response = client.put(f"{USERSKILLS_ENDPOINT}/{USERSKILLID_PUT}", headers={"Authorization": "Basic " + valid_auth},
                          json=update_userskill_json)
    assert response.status_code == 400
    assert response.json['message'] == 'Failed to update due to invalid months of experience'


""" ------------------Test cases for Delete method ()--------------------------------------"""


def test_delete_one_userskills(client, valid_auth):
    response = client.delete(f"{USERSKILLS_ENDPOINT}/{USERSKILLID_DEL}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 200
    assert response.json['message'] == 'Successfully deleted'


def test_delete_invalid_userskillid(client, valid_auth):
    response = client.delete(f"{USERSKILLS_ENDPOINT}/{INVALID_USERSKILLID}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'User skill Map Not Found'


def test_delete_decimal_userskillid(client, valid_auth):
    response = client.delete(f"{USERSKILLS_ENDPOINT}/9.9", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'User skill Map Not Found'


def test_delete_alphanumeric_userskillid(client, valid_auth):
    response = client.delete(f"{USERSKILLS_ENDPOINT}/abc12", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'User skill Map Not Found'
