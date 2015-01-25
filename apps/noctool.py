import random
import string
import cherrypy

__all__ = ['NocTool']

class Root(object):
  
  @cherrypy.expose
  @cherrypy.tools.render(template='index.mako')
  def index(self):
    pass

  @cherrypy.expose
  @cherrypy.tools.render(template='gameAccount.mako')
  def gameAccount(self):
    pass

class Generator(object):
  exposed = True

  @cherrypy.tools.accept(media='text/plain')
  def GET(self):
    return cherrypy.session['mystring']

  def POST(self, length=8):
    some_string = ''.join(random.sample(string.hexdigits, int(length)))
    cherrypy.session['mystring'] = some_string
    return some_string

  def PUT(self, another_string):
    cherrypy.session['mystring'] = another_string

  def DELETE(self):
    cherrypy.session.pop('mystring', None)

