from flask import request
from flask_restful import Resource, Api
from app.entity import ProjectEntity, UsersEntity, CostCenterEntity

def setup_route(app):

	# Este rota é para designar o menu inicial. Feito no Angular?
	class IndexEntity(Resource):
		def get(self):
			return 'oi'

	class Projects(Resource):

		def get(self):
			return {'projects': [project.json() for project in ProjectEntity.query.all()]}

		def post(self):
			data = request.get_json()
			project = ProjectEntity(**data)
			try:
				project.save_project()
			except:
				# Internal Server Error
				return {'message': 'An internal error occurred trying to save project.'}, 500
			return project.json()


	class Project(Resource):
		def get(self, id):
			project = ProjectEntity.find_project(id)
			if project:
				return project.json()
			return {'message': 'Project not found.'}, 404

		def post(self, id):
			if ProjectEntity.find_project(id):
				# Bad request
				return {'message': 'Project id {} already exists.'.format(id)}, 400

			data = request.get_json()
			project = ProjectEntity(**data)
			project.id = id
			try:
				project.save_project()
			except:
				# Internal Server Error
				return {'message': 'An internal error occurred trying to save project.'}, 500
			return project.json()

		def put(self, id):
			data = request.get_json()
			project = ProjectEntity.find_project(id)
			if project:
				project.update_project(**data)
				try:
					project.save_project()
				except:
					# Internal Server Error
					return {'message': 'An internal error occurred trying to save project.'}, 500
				return project.json(), 200
			return {'message': 'Project not found.'}, 404

		def delete(self, id):
			project = ProjectEntity.find_project(id)
			if project:
				try:
					project.delete_project()
				except:
					# Internal Server Error
					return {'message': 'An internal error occurred trying to delete project.'}, 500
				return{'message': 'Project deleted.'}
			return {'message': 'Project not found.'}, 404

	class Users(Resource):

		def get(self):
			return {'users': [project.json() for project in UsersEntity.query.all()]}

		def post(self):
			data = request.get_json()
			user = UsersEntity(**data)
			try:
				user.save_user()
			except:
				# Internal Server Error
				return {'message': 'An internal error occurred trying to save User.'}, 500
			return user.json()

	class User(Resource):

		def get(self, id):
			user = UsersEntity.find_user(id)
			if user:
				return user.json()
			return {'message': 'User not found.'}, 404

		def post(self, id):
			if UsersEntity.find_user(id):
				# Bad request
				return {'message': 'User id {} already exists.'.format(id)}, 400

			data = request.get_json()
			user = UsersEntity(**data)
			user.id = id
			try:
				user.save_user()
			except:
				# Internal Server Error
				return {'message': 'An internal error occurred trying to delete User.'}, 500
			return{'message': 'User deleted.'}


	class Centers(Resource):

		def get(self):
			return {'Cost Centers': [center.json() for center in CostCenterEntity.query.all()]}

		def post(self):
			data = request.get_json()
			center = CostCenterEntity(**data)
			try:
				center.save_center()
			except:
				# Internal Server Error
				return {'message': 'An internal error occurred trying to save cost center.'}, 500
			return center.json()

	class Center(Resource):

		def get(self, id):
			center = CostCenterEntity.find_center(id)
			if center:
				return center.json()
			return {'message': 'Cost Center not found.'}, 404

		def post(self, id):
			if CostCenterEntity.find_center(id):
				# Bad request
				return {'message': 'Cost center sector {} already exists.'.format(id)}, 400

			data = request.get_json()
			center = CostCenterEntity(**data)
			center.id = id
			try:
				center.save_center()
			except:
				# Internal Server Error
				return {'message': 'An internal error occurred trying to save Cost Center.'}, 500
			return center.json()

		def put(self, id):
			data = request.get_json()
			center = CostCenterEntity.find_center(id)
			if center:
				center.update_center(**data)
				try:
					center.save_center()
				except:
					# Internal Server Error
					return {'message': 'An internal error occurred trying to save Cost Center.'}, 500
				return center.json(), 200
			return {'message': 'Cost Center not found.'}, 404

	def delete(self, id):
			center = CostCenterEntity.find_center(id)
			if center:
				try:
					center.delete_center()
				except:
					# Internal Server Error
					return {'message': 'An internal error occurred trying to delete Cost Center.'}, 500
				return{'message': 'Cost Center deleted.'}
			return {'message': 'Cost Center not found.'}, 404

	api = Api(app)

	api.add_resource(IndexEntity, '/index' )
	api.add_resource(Projects, '/projects')
	api.add_resource(Project, '/projects/<int:id>')
	api.add_resource(Users, '/users')
	api.add_resource(User, '/users/<int:id>')
	api.add_resource(Centers, '/costcenters')
	api.add_resource(Center, '/costcenters/<int:id>')