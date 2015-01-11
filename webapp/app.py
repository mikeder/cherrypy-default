import cherrypy

__all__ = ['NocTool']

class NocTool(object):
  def __init__(self):
    pass

  @cherrypy.expose
  @cherrypy.tools.render(template='index.mako')
  def index(self):
    pass 
