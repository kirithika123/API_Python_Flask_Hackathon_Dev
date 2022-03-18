"""
     test_skills_resource.py
     -----------------------
     TDD test cases built from gherkins for the Skills API.
     These functions test the get, post, put and delete methods
     of SkillsResource Class which are the units to be built to support url/Skills and ur/Skills/<id> endpoints
"""
from constants import SKILLS_ENDPOINT

from .constants_tdd import NUM_SKILLS_IN_DB, DECIMAL_SKILL_ID, SKILL_ID_TO_GET, INVALID_SKILLID, SKILL_ID_TO_PUT, \
    NON_EXISTING_SKILL_ID, SKILL_ID_TO_DELETE, ALPHA_SKILL_ID, SKILL_TO_POST,\
    SKILL_TO_POST_DUP, SKILL_TO_PUT, SKILL_TO_PUT_DUP, SKILL_ID_TO_TEST_INV, SKILL_ID_TO_PUT_DUP

"""
    test cases for get()
"""


def test_get_all_skills(client, valid_auth):
    response = client.get(f"{SKILLS_ENDPOINT}", headers={"authorization": "basic " + valid_auth})
    assert len(response.json)== NUM_SKILLS_IN_DB
    assert response.status_code == 200


def test_get_all_skills_unauth_pwd(client, invalid_password):
    response = client.get(f"{SKILLS_ENDPOINT}", headers={"Authorization": "Basic " + invalid_password})
    assert response.status_code == 401


def test_get_all_skills_unauth_user(client, invalid_user):
    response = client.get(f"{SKILLS_ENDPOINT}", headers={"Authorization": "Basic " + invalid_user})
    assert response.status_code == 401


def test_get_all_skills_noauth(client):
    response = client.get(f"{SKILLS_ENDPOINT}")
    assert response.status_code == 401


def test_get_skills_by_id(client, valid_auth):
    response = client.get(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_GET}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 200


def test_get_decimal_skill_id(client, valid_auth):
    response = client.get(f"{SKILLS_ENDPOINT}/{DECIMAL_SKILL_ID}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'Skill not found'


def test_get_alphanumeric_skill_id(client, valid_auth):
    response = client.get(f"{SKILLS_ENDPOINT}/{INVALID_SKILLID}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'Skill not found'


def test_get_null_skill_id(client, valid_auth):
    response = client.get(f"{SKILLS_ENDPOINT}/", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404


"""
    Test cases for post()
"""


def test_post_skill(client, valid_auth):
    new_skill_json = {"Skill_name": SKILL_TO_POST}
    response = client.post(f"{SKILLS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_skill_json)
    assert response.status_code == 201
    assert response.json['Skill_name'] == SKILL_TO_POST
    assert response.json['message'] == "Skill record successfully created"


def test_post_skill_unauth_pwd(client, invalid_password):
    new_skill_json = {"Skill_name": "AngularJS"}
    response = client.post(f"{SKILLS_ENDPOINT}", headers={"Authorization": "Basic " + invalid_password},
                           json=new_skill_json)
    assert response.status_code == 401


def test_post_skill_unauth_user(client, invalid_user):
    new_skill_json = {"Skill_name": "VisualStudio"}
    response = client.post(f"{SKILLS_ENDPOINT}", headers={"Authorization": "Basic " + invalid_user},
                           json=new_skill_json)
    assert response.status_code == 401


def test_post_skill_noauth(client):
    new_skill_json = {"Skill_name": "RestAssured"}
    response = client.post(f"{SKILLS_ENDPOINT}", json=new_skill_json)
    assert response.status_code == 401


def test_post_null_skill_name(client, valid_auth):
    new_skill_json = {"Skill_name": ""}
    response = client.post(f"{SKILLS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_skill_json)
    assert response.status_code == 400
    assert response.json['message'] == 'Failed to create.Missing fields or Invalid Skill name'


def test_post_integer_skill_name(client, valid_auth):
    new_skill_json = {"Skill_name": 1234}
    response = client.post(f"{SKILLS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_skill_json)
    assert response.status_code == 400
    assert response.json['message'] == 'Failed to create.Missing fields or Invalid Skill name'


def test_post_more_skill_names(client, valid_auth):
    new_skill_json = {"Skill_name": "Java,python"}
    response = client.post(f"{SKILLS_ENDPOINT}",
                          headers={"Authorization": "Basic " + valid_auth},
                          json=new_skill_json)

    assert response.status_code == 400
    assert response.json['message'] == "Failed to create.Missing fields or Invalid Skill name"


def test_post_multiple_skill_names(client, valid_auth):
    new_skill_json = {"Skill_name": SKILL_TO_POST_DUP}
    response = client.post(f"{SKILLS_ENDPOINT}",
                           headers={"Authorization": "Basic " + valid_auth},
                           json=new_skill_json)

    assert response.status_code == 400
    assert response.json['message'] == "Failed to create-Duplicate skill name"


def test_post_alphanumeric_skill_name(client, valid_auth):
    new_skill_json = {"Skill_name": "a1234"}
    response = client.post(f"{SKILLS_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth},
                           json=new_skill_json)
    assert response.status_code == 400
    assert response.json['message'] == 'Failed to create.Missing fields or Invalid Skill name'



"""
    Test cases for put()
"""


def test_put_skill(client, valid_auth):
    skill_json = {"Skill_name": SKILL_TO_PUT}
    response = client.put(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_PUT}",
                          headers={"Authorization": "Basic " + valid_auth},
                          json=skill_json)

    assert response.status_code == 201
    assert response.json['Skill_name'] == SKILL_TO_PUT
    assert response.json['message'] == "Skill record successfully updated"


def test_put_skill_unauth_pwd(client, invalid_password):
    skill_json = {"Skill_name": "PostgresSql"}
    response = client.put(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_PUT}",
                          headers={"Authorization": "Basic " + invalid_password},
                          json=skill_json)
    assert response.status_code == 401


def test_put_skill_unauth_user(client, invalid_user):
    skill_json = {"Skill_name": "PostgresSql"}
    response = client.put(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_PUT}",
                          headers={"Authorization": "Basic " + invalid_user})
    assert response.status_code == 401


def test_put_skill_noauth(client):
    skill_json = {"Skill_name": "PostgresSql"}
    response = client.put(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_PUT}",
                          json=skill_json)
    assert response.status_code == 401


def test_put_non_existing_skill_id(client, valid_auth):
    update_skill_json = {"Skill_name": "Data Science"}
    response = client.put(f"{SKILLS_ENDPOINT}/{NON_EXISTING_SKILL_ID}",
                          headers={"Authorization": "Basic " + valid_auth},
                          json=update_skill_json)
    assert response.status_code == 404
    assert response.json['message']== "Skill not found"

#
def test_put_null_skill_name(client, valid_auth):
    update_skill_json = {"Skill_name": ""}
    response = client.put(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_PUT}",
                          headers={"Authorization": "Basic " + valid_auth},
                          json=update_skill_json)
    assert response.status_code == 400
    assert response.json['message'] == "Failed to update.Missing fields or Invalid Skill name"


def test_put_more_skill_names(client, valid_auth):
    update_skill_json = {"Skill_name": "Java,python"}
    response = client.put(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_PUT}",
                          headers={"Authorization": "Basic " + valid_auth},
                          json=update_skill_json)
    assert response.status_code == 400
    assert response.json['message'] == "Failed to update.Missing fields or Invalid Skill name"


def test_put_invalid_skill_name3(client, valid_auth):
    update_skill_json = {"Skill_name": 1234}
    response = client.put(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_PUT}",
                          headers={"Authorization": "Basic " + valid_auth},
                          json=update_skill_json)

    assert response.status_code == 400
    assert response.json['message'] == "Failed to update.Missing fields or Invalid Skill name"


def test_put_multiple_skill_names(client, valid_auth):
    new_skill_json = {"Skill_name": SKILL_TO_PUT_DUP}
    response = client.put(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_PUT}",
                        headers={"Authorization": "Basic " + valid_auth},
                        json=new_skill_json)

    assert response.status_code == 400
    assert response.json['message'] == "Failed to update-Duplicate skill name"


def test_put_invalid_skill_name1(client, valid_auth):
    update_skill_json = {"Skill_name": "1a2b3c"}
    response = client.put(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_TEST_INV}",
                          headers={"Authorization": "Basic " + valid_auth},
                          json=update_skill_json)

    assert response.status_code == 400
    assert response.json['message'] == "Failed to update.Missing fields or Invalid Skill name"


"""
    Test cases for delete()
"""


def test_delete_skill(client, valid_auth):

    response = client.delete(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_DELETE}",
                          headers={"Authorization": "Basic " + valid_auth})

    assert response.status_code == 200
    assert response.json['message'] == "Successfully Deleted"


def test_delete_skill_unauth_pwd(client, invalid_password):
    response = client.delete(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_TEST_INV}",
                          headers={"Authorization": "Basic " + invalid_password})
    assert response.status_code == 401


def test_delete_skill_unauth_user(client, invalid_user):
    response = client.delete(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_TEST_INV}",
                          headers={"Authorization": "Basic " + invalid_user})
    assert response.status_code == 401


def test_delete_skill_noauth(client):
    response = client.delete(f"{SKILLS_ENDPOINT}/{SKILL_ID_TO_TEST_INV}")
    assert response.status_code == 401


def test_delete_skill_non_existing_id(client, valid_auth):
    response = client.delete(f"{SKILLS_ENDPOINT}/{NON_EXISTING_SKILL_ID}",
                             headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == "Failed to delete-Skill not found"


def test_delete_decimal_skill_id(client, valid_auth):
    response = client.delete(f"{SKILLS_ENDPOINT}/{DECIMAL_SKILL_ID}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == "Failed to delete-invalid skill id"


def test_delete_alphanumeric_skill_id(client, valid_auth):
    response = client.delete(f"{SKILLS_ENDPOINT}/{ALPHA_SKILL_ID}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == "Failed to delete-invalid skill id"
