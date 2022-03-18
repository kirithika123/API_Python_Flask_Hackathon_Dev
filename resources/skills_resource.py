"""
    skills_resource.py
    -----------------
    Contains the CRUD functionalities for the endpoints /Skills and /Skills/<id>
"""

from datetime import datetime
from flask import request
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from authentication import auth
from database import db
from models import SkillMaster


class SkillsResource(Resource):
    @auth.login_required
    def get(self, id=None):
        if not id:
            skills = SkillMaster.query.all()
            skill_list = []
            for skill in skills:
                skill_data = {'Skill_Id': skill.skill_id, 'Skill_name': skill.skill_name}
                skill_list.append(skill_data)
            return skill_list, 200
        try:
            skill = SkillMaster.query.get(id)
        except SQLAlchemyError:
            return {'message': 'Skill not found'}, 404
        if skill is None:
            return {'message': 'Skill not found'}, 404
        skill_data = {'Skill_Id': skill.skill_id, 'Skill_name': skill.skill_name}
        return skill_data, 200

    @auth.login_required
    def post(self):
        # Checking for valid JSON
        if request.is_json:
            try:
                name = request.json['Skill_name']
            except KeyError:
                return {'message': 'Failed to create-missing mandatory fields'}
            # Checking for blank or multiple skill names
            if not name or ',' in str(name) or type(name) is int or type(name) is bool:
                return {'message': 'Failed to create.Missing fields or Invalid Skill name'}, 400

            # Checking for duplicate skill name
            skills = SkillMaster.query.all()
            skill_check = False

            for skill in skills:
                skill_name = skill.skill_name
                if str(skill_name).lower() == str(name).lower():
                    skill_check = True
                    break
            if not skill_check:
                skill = SkillMaster(skill_name=name, creation_time=datetime.now(), last_mod_time=datetime.now())
                try:
                    db.session.add(skill)
                    db.session.commit()
                except SQLAlchemyError:
                    return {'message': 'Failed to create- Internal server error'}, 500
                return {'Skill_Id': skill.skill_id, 'Skill_name': skill.skill_name,
                        'message': 'Skill record successfully created'}, 201
            else:
                return {'message': 'Failed to create-Duplicate skill name'}, 400
        else:
            return {'message': 'Improper JSON format'}, 400


    @auth.login_required
    def put(self, id):
        try:
            skill = SkillMaster.query.get(id)
        except SQLAlchemyError:
            return {'message': 'Skill not found'}, 404
        if skill is None:
            return {'message': 'Skill not found'}, 404
        if request.is_json:
            try:
                name = request.json['Skill_name']
            except KeyError:
                return {'message': 'Failed to update-missing mandatory fields'}
                # Checking for blank or multiple skill names
            if not name or ',' in str(name) or type(name) is int or type(name) is bool:
                return {'message': 'Failed to update.Missing fields or Invalid Skill name'}, 400

            # Checking for duplicate skill name
            skills = SkillMaster.query.all()
            skill_exist = False
            id_exist=0

            for item in skills:
                skill_name = item.skill_name
                if str(skill_name).lower() == str(name).lower():
                    id_exist = item.skill_id
                    skill_exist = True
                    break

            if not skill_exist or id_exist == int(id):
                skill.skill_name = name
                skill.last_mod_time = datetime.now()
                try:
                    db.session.commit()
                except SQLAlchemyError:
                    return {'message': 'Failed to update-internal server error'}, 500
                return {'Skill_Id': skill.skill_id, 'Skill_name': skill.skill_name,
                        'message': 'Skill record successfully updated'}, 201
            else:
                return {'message': 'Failed to update-Duplicate skill name'}, 400
        else:
            return {'message': 'Improper JSON format'}, 400

    @auth.login_required
    def delete(self, id):
        try:
            skill = SkillMaster.query.get(id)
        except SQLAlchemyError:
            return {'message': 'Failed to delete-invalid skill id'}, 404
        if skill is None:
            return {'message': 'Failed to delete-Skill not found'}, 404
        try:
            db.session.delete(skill)
            db.session.commit()
        except SQLAlchemyError:
            return {'message': "Failed to delete-Internal server error"}, 500
        return {'message': 'Successfully Deleted'}, 200
