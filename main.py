import os, urllib, jinja2, webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({}))

class ComputingEverywherePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('computing_everywhere.html')
        self.response.write(template.render({}))

        
application = webapp2.WSGIApplication([
    ('/computing_everywhere', ComputingEverywherePage),
    ('/*', MainPage),
], debug=True)
