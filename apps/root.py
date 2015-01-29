import random
import string
import cherrypy

__all__ = ['Root']

class Index(object):
  
  @cherrypy.expose
  @cherrypy.tools.render(template='index.mako')
  def index(test=None):
    test = 'words'
    return {'test': test} 

  @cherrypy.expose
  @cherrypy.tools.render(template='charts.mako')
  def charts(self):
    pass

  @cherrypy.expose
  @cherrypy.tools.render(template='test.mako')
  def test(body=None):
    derp = 'Mike'
    body = '''
            <h1> SqweebNet Testing Grounds </h1>
            Here derps derpington %s''' % derp
    return {'body':body}

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

