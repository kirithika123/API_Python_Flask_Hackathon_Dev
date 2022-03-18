"""
conftest.py
-----------
The start point of pytest where we can create fixtures. Currently we have -
1. client -to create the mock client 'app.test_client' object that is used to send the CRUD requests
    and create a mock DB
2. valid_auth -to create valid basic auth token using valid username and password
3. invalid_password - to create invalid basic auth token using valid username but invalid password
4. invalid_user - to create invalid basic auth token using invalid password but valid username

"""

import pytest
import datetime
from flask import Flask
from flask_restful import Api
from database import db
from resources.users_resource import UsersResource
from resources.skills_resource import SkillsResource
from resources.userskills_resource import UserSkillsResource
from resources.userskillsmap_resource import UserSkillsMappingResource
from models import User, SkillMap, SkillMaster
from base64 import b64encode
from configuration import USER_NAME, PASSWORD
# from app import create_app
from .constants_tdd import DATABASE_URL_TEST, INVALID_USER_FIXTURE, INVALID_PWD_FIXTURE


@pytest.fixture(scope="module")
def client():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL_TEST
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    api = Api(app)
    api.add_resource(UsersResource, '/Users', '/Users/<id>')
    api.add_resource(SkillsResource, '/Skills', '/Skills/<id>')
    api.add_resource(UserSkillsMappingResource, '/UserSkillsMap')
    api.add_resource(UserSkillsResource, '/UserSkills', '/UserSkills/<id>')
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            create_test_db()
        yield client
    with app.app_context():
        teardown()


@pytest.fixture
def valid_auth():
    cred_string = USER_NAME + ':' + PASSWORD
    cred_bytes = cred_string.encode("utf-8")
    return b64encode(cred_bytes).decode("utf-8")


@pytest.fixture
def invalid_password():
    cred_string = USER_NAME + ':' + INVALID_PWD_FIXTURE
    cred_bytes = cred_string.encode("utf-8")
    return b64encode(cred_bytes).decode("utf-8")


@pytest.fixture
def invalid_user():
    cred_string = INVALID_USER_FIXTURE + ':' + PASSWORD
    cred_bytes = cred_string.encode("utf-8")
    return b64encode(cred_bytes).decode("utf-8")


# Function to create a mock DB with 3 tables - tbl_lms_user, tbl_lms_skill_master and tbl_lms_userskills_map
def create_test_db():
    db.create_all()
    user = User(user_id='U01', user_first_name='Harry',
                            user_last_name='Potter', user_phone_number=1112223333,
                            user_location='New Jersey', user_time_zone='EST',
                            user_linkedin_url='https://www.linkedin.com/HarryPotter',
                            user_edu_ug='BTech', user_edu_pg='MTech',
                            user_comments='Looking for a job', user_visa_status='H1B',
                            creation_time=datetime.datetime.now(), last_mod_time=datetime.datetime.now())
    db.session.add(user)
    db.session.commit()
    user = User(user_id='U02', user_first_name='Mary',
                user_last_name='Poppins', user_phone_number=2221113333,
                user_location='USA', user_time_zone='EST',
                user_linkedin_url='https://www.linkedin.com/MaryPoppins',
                user_edu_ug='BTech', user_edu_pg='MTech',
                user_comments='Looking for a job', user_visa_status='H4-EAD',
                creation_time=datetime.datetime.now(), last_mod_time=datetime.datetime.now())
    db.session.add(user)
    db.session.commit()
    user = User(user_id='U03', user_first_name='Sherlock',
                user_last_name='Holmes', user_phone_number=4445556666,
                user_location='USA', user_time_zone='PST',
                user_linkedin_url='https://www.linkedin.com/SherlockHolmes',
                user_edu_ug='BSc', user_edu_pg='MSc',
                user_comments='Looking for a job', user_visa_status='H4-EAD',
                creation_time=datetime.datetime.now(), last_mod_time=datetime.datetime.now())
    db.session.add(user)
    db.session.commit()
    user = User(user_id='U04', user_first_name='James',
                user_last_name='Bond', user_phone_number=1111111111,
                user_location='USA', user_time_zone='PST',
                user_linkedin_url='https://www.linkedin.com/JamesBond',
                user_edu_ug='BSc', user_edu_pg='MSc',
                user_comments='Working parttime', user_visa_status='US-Citizen',
                creation_time=datetime.datetime.now(), last_mod_time=datetime.datetime.now())
    db.session.add(user)
    db.session.commit()
    user = User(user_id='U05', user_first_name='Ahaana',
                user_last_name='Krishna', user_phone_number=3336665555,
                user_location='USA', user_time_zone='CST',
                user_linkedin_url='https://www.linkedin.com/Ahaana',
                user_edu_ug='BSc', user_edu_pg='MSc',
                user_comments='Database Engineer', user_visa_status='H1B',
                creation_time=datetime.datetime.now(), last_mod_time=datetime.datetime.now())
    db.session.add(user)
    db.session.commit()

    skill = SkillMaster(skill_name='Java', creation_time=datetime.datetime.now(),
                        last_mod_time=datetime.datetime.now())
    db.session.add(skill)
    db.session.commit()
    skill = SkillMaster(skill_name='Python', creation_time=datetime.datetime.now(),
                        last_mod_time=datetime.datetime.now())
    db.session.add(skill)
    db.session.commit()
    skill = SkillMaster(skill_name='Databases', creation_time=datetime.datetime.now(),
                        last_mod_time=datetime.datetime.now())
    db.session.add(skill)
    db.session.commit()
    skill = SkillMaster(skill_name='Testing', creation_time=datetime.datetime.now(),
                        last_mod_time=datetime.datetime.now())
    db.session.add(skill)
    db.session.commit()
    skill = SkillMaster(skill_name='Javascript', creation_time=datetime.datetime.now(),
                        last_mod_time=datetime.datetime.now())
    db.session.add(skill)
    db.session.commit()

    userskill = SkillMap(user_skill_id='US01', user_id='U01', skill_id=1,
                         months_of_exp=12, creation_time=datetime.datetime.now(),
                         last_mod_time=datetime.datetime.now())
    db.session.add(userskill)
    db.session.commit()
    userskill = SkillMap(user_skill_id='US02', user_id='U01', skill_id=4,
                         months_of_exp=24, creation_time=datetime.datetime.now(),
                         last_mod_time=datetime.datetime.now())
    db.session.add(userskill)
    db.session.commit()
    userskill = SkillMap(user_skill_id='US03', user_id='U02', skill_id=2,
                         months_of_exp=16, creation_time=datetime.datetime.now(),
                         last_mod_time=datetime.datetime.now())
    db.session.add(userskill)
    db.session.commit()
    userskill = SkillMap(user_skill_id='US04', user_id='U03', skill_id=3,
                         months_of_exp=24, creation_time=datetime.datetime.now(),
                         last_mod_time=datetime.datetime.now())
    db.session.add(userskill)
    db.session.commit()
    userskill = SkillMap(user_skill_id='US05', user_id='U04', skill_id=1,
                         months_of_exp=24, creation_time=datetime.datetime.now(),
                         last_mod_time=datetime.datetime.now())
    db.session.add(userskill)
    db.session.commit()


# Function to drop tables at the end of fixture
def teardown():
    db.session.remove()
    db.drop_all()
