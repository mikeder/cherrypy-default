import sys
import logging
from logging import handlers
import os, os.path
import cherrypy
from cherrypy import _cplogging
from cherrypy.lib import httputil
import datetime

basdir = os.path.abspath(os.path.dirname(__file__))

class Server(object):
  def __init__(self, options):
    # Find directory where server is running
    self.base_dir = os.path.normpath(os.path.abspath(options.basedir))
    # Config directory
    self.conf_path = os.path.join(self.base_dir, 'conf')
    # Make sure log folder is in place
    log_dir = os.path.join(self.base_dir, 'logs')
    if not os.path.exists(log_dir):
      os.mkdir(log_dir)
    # Update settings for server and engine from config
    cherrypy.config.update(os.path.join(self.conf_path, 'server.cfg'))

    engine = cherrypy.engine
    
    # Append system path so Python can find app modules
    sys.path.insert(0, self.base_dir)
    
    # Template engine tool
    from lib.tools.template import MakoTool
    cherrypy.tools.render = MakoTool()

    # Mount app to be run - index() method from below for now
    from webapp.app import NocTool
    app = NocTool()
    conf = os.path.join(self.conf_path, 'app.cfg')
    webapp = cherrypy.tree.mount(app, '/', conf)
    self.make_rotate_logs(webapp)
    
    # Template engine plugin
    from lib.plugins.template import MakoTemplatePlugin
    templateDir = os.path.join(self.base_dir, 'template')
    cacheDir = os.path.join(self.base_dir, 'cache')  
    engine.mako = MakoTemplatePlugin(engine, templateDir, cacheDir)
    engine.mako.subscribe()

  def run(self):
    engine = cherrypy.engine
  
    if hasattr(engine, "signal_handler"):
      engine.signal_handler.subscribe()
      
    if hasattr(engine, "console_control_handler"):
      engine.console_control_handler.subscribe()

    # Start cherrypy engine
    engine.start()

    # Run the engine main loop
    engine.block()

  def on_error(self, status, message, traceback, version):
   code = '404' if status.startswith('404') else 'error'
   template = cherrypy.engine.publish('lookup-template', "%s.mako" % code).pop()
   return template.render()
   
  def make_rotate_logs(self, app):
   # see http://www.cherrypy.org/wiki/Logging#CustomHandlers
   log = app.log
   
   # Remove the default FileHandlers if present.
   log.error_file = ""
   log.access_file = ""
   
   maxBytes = getattr(log, "rot_maxBytes", 10485760)
   backupCount = getattr(log, "rot_backupCount", 5)
   
   # Make a new RotatingFileHandler for the error log.
   fname = getattr(log, "rot_error_file", "error.log")
   h = handlers.RotatingFileHandler(fname, 'a', maxBytes, backupCount)
   h.setLevel(logging.DEBUG)
   h.setFormatter(_cplogging.logfmt)
   log.error_log.addHandler(h)
   
   # Make a new RotatingFileHandler for the access log.
   fname = getattr(log, "rot_access_file", "access.log")
   h = handlers.RotatingFileHandler(fname, 'a', maxBytes, backupCount)
   h.setLevel(logging.DEBUG)
   h.setFormatter(_cplogging.logfmt)
   log.access_log.addHandler(h)

if __name__ == '__main__':
    from optparse import OptionParser
    
    def parse_commandline():
        curdir = os.path.normpath(os.path.abspath(os.path.curdir))
        
        parser = OptionParser()
        parser.add_option("-b", "--base-dir", dest="basedir",
                          help="Base directory in which the server "\
                          "is launched (default: %s)" % curdir)
        parser.set_defaults(basedir=curdir)
        (options, args) = parser.parse_args()

        return options

    Server(parse_commandline()).run()
