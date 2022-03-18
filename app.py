"""

app.py
------
THIS is where our Flask server starts. We create an instance of Flask, set the database path,
initialize db, create an instance of the Api class from flask_restful that will help us create
helper classes for each resource which is to be mapped to an endpoint.
Currently, this Flask app runs with the default WerkZeug development server. For deployment, we will need to configure
it with a production grade HTTP server

"""

from flask import Flask, render_template
from flask_restful import Api
from resources.users_resource import UsersResource
from resources.skills_resource import SkillsResource
from resources.userskills_resource import UserSkillsResource
from resources.userskillsmap_resource import UserSkillsMappingResource
from database import db
from authentication import auth
from configuration import DATABASE_URL_DEV

# Configuring Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL_DEV
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)
api.add_resource(UsersResource, '/Users', '/Users/<id>')
api.add_resource(SkillsResource, '/Skills', '/Skills/<id>')
api.add_resource(UserSkillsMappingResource, '/UserSkillsMap')
api.add_resource(UserSkillsResource, '/UserSkills', '/UserSkills/<id>')

# Configuring swagger start to the path url/
@app.route('/')
@auth.login_required
def get_docs():
     print('sending docs')
     return render_template('swaggerui.html')


# App start point
if __name__ == '__main__':
     app.run(debug=True)
