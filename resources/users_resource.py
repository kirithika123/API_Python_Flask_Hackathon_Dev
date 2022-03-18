"""
    users_resource.py
    -----------------
    Contains the CRUD functionalities for the endpoints /Users and /Users/<id>
"""

import datetime
import sqlalchemy
from flask import request
from flask_restful import Resource
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.expression import cast
from models import User
from authentication import auth
from database import db
from utils import invalid_user_fields
from constants import MISSING_MAND_FIELDS, FAILED_TO_CREATE, FAILED_TO_UPDATE


class UsersResource(Resource):
    @auth.login_required
    def get(self, id=None):
        # Get all users
        if not id:
            users = User.query.all()
            user_list = []
            for user in users:
                name = f"{user.user_first_name},{user.user_last_name}"
                user_data = {'user_id': user.user_id, 'name': name, 'phone_number': int(user.user_phone_number),
                            'location': user.user_location, 'time_zone': user.user_time_zone,
                            'linkedin_url': user.user_linkedin_url}
                user_list.append(user_data)
            return user_list, 200

        # Get single user
        user = User.query.get(id)
        if user is None:
            return {'message': 'User Not Found'}, 404
        name = f"{user.user_first_name},{user.user_last_name}"
        return {'user_id': user.user_id, 'name': name, 'phone_number': int(user.user_phone_number),
                'location': user.user_location, 'time_zone': user.user_time_zone,
                'linkedin_url': user.user_linkedin_url}, 200

    @auth.login_required
    def post(self):
        # Checking for valid JSON
        if request.is_json:
            # Checking for invalid user field values
            invalid_status = invalid_user_fields(request.json)
            if invalid_status['invalid']:
                return {'message': f"{FAILED_TO_CREATE}-{invalid_status['message']}"}, 400
            # Getting first and last names
            full_name = (str(request.json['name'])).split(',')
            first_name = full_name[0]
            last_name = full_name[1]
            # Retrieving max ID in DB
            try:
                max_id = db.session.query(func.max(cast(func.replace(User.user_id, "U", ""), sqlalchemy.Integer))).scalar()
                if max_id is not None:
                    max_id+= 1
                else:
                    max_id = 1
            except SQLAlchemyError:
                return {'message': f"{FAILED_TO_CREATE}-Internal server error"}, 500
            str_max_id = str(max_id)
            if len(str_max_id) > 1:
                new_user_id = 'U' + str_max_id
            else:
                new_user_id = 'U0' + str_max_id
            # Adding new user into Users table
            try:
                user = User(user_id=new_user_id, user_first_name=first_name,
                            user_last_name=last_name, user_phone_number=int(request.json['phone_number']),
                            user_location=request.json['location'], user_time_zone=request.json['time_zone'],
                            user_linkedin_url=request.json['linkedin_url'],
                            user_edu_ug=request.json['education_ug'], user_edu_pg=request.json['education_pg'],
                            user_comments=request.json['comments'], user_visa_status=request.json['visa_status'],
                            creation_time=datetime.datetime.now(), last_mod_time=datetime.datetime.now())
            except KeyError:
                return {'message': f"{FAILED_TO_CREATE}-{MISSING_MAND_FIELDS}"}, 400
            try:
                db.session.add(user)
                db.session.commit()
            except SQLAlchemyError:
                return {'message': f"{FAILED_TO_CREATE}-Internal server error"}, 500

            name = f"{user.user_first_name},{user.user_last_name}"
            return {'user_id': user.user_id, 'name': name, 'phone_number': int(user.user_phone_number),
                    'location': user.user_location, 'time_zone': user.user_time_zone, 'linkedin_url': user.user_linkedin_url,
                    'education_ug': user.user_edu_ug, 'education_pg': user.user_edu_pg,
                    'visa_status': user.user_visa_status,
                    'comments': user.user_comments, 'message': 'User record successfully created'}, 201
        else:
            return {'message': 'Improper JSON format'}, 400

    @auth.login_required
    def put(self, id):
        if request.is_json:
            user = User.query.get(id)
            if user is None:
                return {'message': 'User Not Found'}, 404
            invalid_status = invalid_user_fields(request.json)
            if invalid_status['invalid']:
                return {'message': f"{FAILED_TO_UPDATE}-{invalid_status['message']}"}, 400
            try:
                full_name = (str(request.json['name'])).split(',')
                first_name = full_name[0]
                last_name = full_name[1]
                user.user_first_name = first_name
                user.user_last_name = last_name
                user.user_phone_number = int(request.json['phone_number'])
                user.user_location = request.json['location']
                user.user_time_zone = request.json['time_zone']
                user.user_linkedin_url = request.json['linkedin_url']
                user.user_edu_ug = request.json['education_ug']
                user.user_edu_pg = request.json['education_pg']
                user.user_visa_status = request.json['visa_status']
                user.user_comments= request.json['comments']
                user.last_mod_time = datetime.datetime.now()
            except KeyError:
                return {'message': f"{FAILED_TO_UPDATE}-{MISSING_MAND_FIELDS}"}, 400
            try:
                db.session.commit()
            except SQLAlchemyError:
                return {'message': f"{FAILED_TO_UPDATE}-Internal server error"}, 500

            name = f"{user.user_first_name},{user.user_last_name}"
            return {'user_id': user.user_id, 'name': name, 'phone_number': int(user.user_phone_number),
                    'location': user.user_location, 'time_zone': user.user_time_zone,
                    'linkedin_url': user.user_linkedin_url,
                    'education_ug': user.user_edu_ug, 'education_pg': user.user_edu_pg,
                    'visa_status': user.user_visa_status,
                    'comments': user.user_comments, 'message': 'User record successfully updated'}, 201
        else:
            return {'message': 'Improper JSON format'}, 400

    @auth.login_required
    def delete(self, id):
        user = User.query.get(id)

        if user is None:
            return {'message': 'Failed to delete-user not found'}, 404
        try:
            db.session.delete(user)
            db.session.commit()
        # if any database exception occurs
        except SQLAlchemyError:
            return {'message': "Failed to delete-Internal server error"}, 500

        return {'message': 'User record successfully deleted'}, 200


















