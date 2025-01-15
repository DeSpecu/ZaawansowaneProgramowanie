from flask import Flask
from flask_restful import Resource, Api

class Movie(Resource):

   def get(self):
       y = []
       r = open("movies.txt")
       for x in r:
           splitted = x.split(',')
           self.id = splitted[0].replace('\n','')
           self.title = splitted[1].replace('\n','')
           self.genres = splitted[2].replace('\n','')
           y.append({'id': self.id, 'title': self.title, 'genres': self.genres})

       return y


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
   def get(self):
       return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(Movie, '/movies')

if __name__ == '__main__':
   app.run(debug=True)