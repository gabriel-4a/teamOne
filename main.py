# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# the handler section
class HomeHandler(webapp2.RequestHandler): #homepage "/"
    def get(self):
        home_template = the_jinja_env.get_template('templates/home.html') #pulls in "home.html" template
        self.response.write(home_template.render()) #serves home.html template back to front-end

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/about.html')
        self.response.write(about_template.render())

class PetsHandler(webapp2.RequestHandler):
    def get(self):
        # below are the form results from the form on home.html
        pets_template = the_jinja_env.get_template('templates/dogs.html')
        self.response.write(pets_template.render()) #passes in results_Dict that will fill the placeholders on results.html

class DogHandler(webapp2.RequestHandler):
	def get(self):

	        dogs_template = the_jinja_env.get_template('templates/dogs.html')
	        self.response.write(dogs_template.render())

class CatHandler(webapp2.RequestHandler):
	def get(self):
	        cats_template = the_jinja_env.get_template('templates/cats.html')
	        self.response.write(cats_template.render())

class GoldfishHandler(webapp2.RequestHandler):
    def get(self):
	        goldfish_template = the_jinja_env.get_template('templates/goldfish.html')
	        self.response.write(goldfish_template.render())

class SnakeHandler(webapp2.RequestHandler):
	def get(self):
	        snake_template = the_jinja_env.get_template('templates/snakes.html')
	        self.response.write(snake_template.render())

class MouseHandler(webapp2.RequestHandler):
    def get(self):
	        mouse_template = the_jinja_env.get_template('templates/mice.html')
	        self.response.write(mouse_template.render())

# the routes / app configuration section
app = webapp2.WSGIApplication([
  ('/', HomeHandler),
  ('/about', AboutHandler),
  ('/dogs', PetsHandler),
  ('/dogs', DogHandler),
  ('/cats', CatHandler),
  ('/snakes', SnakeHandler),
  ('/mice', MouseHandler),
  ('/goldfish',GoldfishHandler)
  ], debug=True)







# to spin your server, navigate to your parent folder and run in your terminal:
# dev_appserver.py app.yaml
# then go to http://localhost:8080 in your browser
# to stop your server, in your terminal press  control+C
