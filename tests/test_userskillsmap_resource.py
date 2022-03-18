"""
    test_usersskillsmap_resource.py
    ----------------------
    TDD test cases built from gherkins for the UsersSkillsMap API.
    These functions test the get method provided for incoming query parameters.
    url/UserSkillsMap - get all users with skills in JSON response
    url/UserSkillsMap?user_id=<user_id> - get single user 'user_id' with his mapped skills in JSON response
    url/UserSkillsMap?skill_id=1=<skill_id> - get all users with skill mapped to 'skill_id'
    of UsersResource Class which are the units to be built to support url/Users and ur/Users/<id> endpoints
"""

from constants import USERSKILLS_MAPPING_ENDPOINT
from .constants_tdd import NUM_USERS_IN_DB, QUERY_USER_ID, QUERY_SKILL_ID, QUERY_SKILL_ID_NOT_EXIST,\
                        QUERY_USER_ID_NOT_EXIST, QUERY_USER_ID_STR, QUERY_SKILL_ID_STR


def test_get_all_users_skills(client, valid_auth):
    user_key = 'users'
    id_key = 'id'
    firstname_key = 'firstName'
    lastname_key = 'lastName'
    skillmap_key = 'skillmap'
    response = client.get(f"{USERSKILLS_MAPPING_ENDPOINT}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 200
    assert user_key in response.json
    json_list = response.json['users']
    assert len(json_list) == NUM_USERS_IN_DB
    for i in range(len(json_list)):
        assert id_key in response.json['users'][i]
        assert firstname_key in response.json['users'][i]
        assert lastname_key in response.json['users'][i]
        assert skillmap_key in response.json['users'][i]


def test_get_all_users_skills_inv_pwd(client, invalid_password):
    response = client.get(f"{USERSKILLS_MAPPING_ENDPOINT}", headers={"Authorization": "Basic " + invalid_password})
    assert response.status_code == 401


def test_get_all_users_skills_inv_user(client, invalid_user):
    response = client.get(f"{USERSKILLS_MAPPING_ENDPOINT}", headers={"Authorization": "Basic " + invalid_user})
    assert response.status_code == 401


def test_get_all_users_skills_noauth(client):
    response = client.get(f"{USERSKILLS_MAPPING_ENDPOINT}", headers={"Authorization": "Basic "})
    assert response.status_code == 401


def test_get_existing_user_skills(client, valid_auth):
    user_key = 'users'
    id_key = 'id'
    firstname_key = 'firstName'
    lastname_key = 'lastName'
    skillmap_key = 'skillmap'
    response = client.get(f"{USERSKILLS_MAPPING_ENDPOINT}{QUERY_USER_ID}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 200
    assert user_key in response.json
    json_list = response.json['users']
    assert len(json_list) == 1
    assert id_key in response.json['users'][0]
    assert firstname_key in response.json['users'][0]
    assert lastname_key in response.json['users'][0]
    assert skillmap_key in response.json['users'][0]


def test_get_existing_user_str_skills(client, valid_auth):
    user_key = 'users'
    id_key = 'id'
    firstname_key = 'firstName'
    lastname_key = 'lastName'
    skillmap_key = 'skillmap'
    response = client.get(f"{USERSKILLS_MAPPING_ENDPOINT}{QUERY_USER_ID_STR}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 200
    assert user_key in response.json
    json_list = response.json['users']
    assert len(json_list) == 1
    assert id_key in response.json['users'][0]
    assert firstname_key in response.json['users'][0]
    assert lastname_key in response.json['users'][0]
    assert skillmap_key in response.json['users'][0]


def test_get_non_existing_user_skills(client, valid_auth):
    response = client.get(f"{USERSKILLS_MAPPING_ENDPOINT}{QUERY_USER_ID_NOT_EXIST}", headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'User not found'


def test_get_existing_user_skills_noauth(client):
    response = client.get(f"{USERSKILLS_MAPPING_ENDPOINT}{QUERY_USER_ID}", headers={"Authorization": "Basic "})
    assert response.status_code == 401


def test_get_existing_skill_users(client, valid_auth):
    user_key = 'users'
    id_key = 'id'
    firstname_key = 'firstName'
    lastname_key = 'lastName'
    skillmap_key = 'skillmap'
    response = client.get(f"{USERSKILLS_MAPPING_ENDPOINT}{QUERY_SKILL_ID}",
                          headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 200
    assert user_key in response.json
    json_list = response.json['users']
    for i in range(len(json_list)):
        assert id_key in response.json['users'][i]
        assert firstname_key in response.json['users'][i]
        assert lastname_key in response.json['users'][i]
        assert skillmap_key in response.json['users'][i]


def test_get_existing_skill_str_users(client, valid_auth):
    user_key = 'users'
    id_key = 'id'
    firstname_key = 'firstName'
    lastname_key = 'lastName'
    skillmap_key = 'skillmap'
    response = client.get(f"{USERSKILLS_MAPPING_ENDPOINT}{QUERY_SKILL_ID_STR}",
                          headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 200
    assert user_key in response.json
    json_list = response.json['users']
    for i in range(len(json_list)):
        assert id_key in response.json['users'][i]
        assert firstname_key in response.json['users'][i]
        assert lastname_key in response.json['users'][i]
        assert skillmap_key in response.json['users'][i]


def test_get_non_existing_skill_users(client, valid_auth):
    response = client.get(f"{USERSKILLS_MAPPING_ENDPOINT}{QUERY_SKILL_ID_NOT_EXIST}",
                          headers={"Authorization": "Basic " + valid_auth})
    assert response.status_code == 404
    assert response.json['message'] == 'Skill not found'




