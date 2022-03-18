"""
    userskillsmap_resource.py
    ----------------------
    Contains the functionality to-
    read list of all users in LMS DB and their mapped skills - url/UserSkillsMap
    read one user and mapped skills - url/UserSkillsMap?user_id=<id>
    read all users mapped to a particular skill - url/UserSkillsMap?skill_id=<id>
"""

from models import User, SkillMap, SkillMaster
from flask_restful import Resource
from flask import request
from authentication import auth
from database import db
from sqlalchemy.exc import SQLAlchemyError


def skill_search(id):
    try:
        skills = db.session.query(SkillMaster, SkillMap). \
            select_from(SkillMap).join(SkillMaster).filter(SkillMap.user_id == id).all()
    except SQLAlchemyError:
        return {'message': "Internal server error"}, 500
    skills_list = []
    for skillmaster, skillmap in skills:
        skill_data = {'id': skillmaster.skill_id, 'Skill': skillmaster.skill_name}
        skills_list.append(skill_data)
    return skills_list

def user_search(id):
    try:
        users = db.session.query(SkillMap, User). \
            select_from(SkillMap).join(User).filter(SkillMap.skill_id == id).all()
    except SQLAlchemyError:
        return {'message': "Internal server error"}, 500
    users_list = []
    skill = SkillMaster.query.get(id)
    skill_list = [{'id': skill.skill_id, 'skill': skill.skill_name}]
    for skillmap, user in users:
        user_data = {'id': user.user_id, 'firstName': user.user_first_name, 'lastName': user.user_last_name,
                     'skillmap': skill_list}
        users_list.append(user_data)
    return users_list


class UserSkillsMappingResource(Resource):
    @auth.login_required
    def get(self):
        # pdb.set_trace()
        if request.args.get('user_id'):
            # pdb.set_trace()
            id = request.args['user_id']
            if '\"' in id:
                id = id.strip('\"')
            elif '\'' in id:
                id = id.strip('\'')

            user = User.query.get(id)
            if user is None:
                return {'message': 'User not found'}, 404
            skills_list = skill_search(id)
            user_data = [{'id': user.user_id, 'firstName': user.user_first_name,'lastName': user.user_last_name,
                          'skillmap': skills_list}]
            return {'users': user_data}, 200
        elif request.args.get('skill_id'):
            id = request.args['skill_id']
            if '\"' in id:
                id = id.strip('\"')
            elif '\'' in id:
                id = id.strip('\'')

            try:
                skill = SkillMaster.query.get(id)
            except SQLAlchemyError:
                return {'message': 'Skill not found'}, 404
            if skill is None:
                return {'message': 'Skill not found'}, 404
            users_list = user_search(id)
            return {'users': users_list}, 200
        else:
            users = User.query.all()
            user_list = []
            for user in users:
                skills_list = skill_search(user.user_id)
                user_data = {'id':user.user_id, 'firstName': user.user_first_name, 'lastName': user.user_last_name,
                             'skillmap': skills_list}
                user_list.append(user_data)
            return {'users': user_list}, 200

