# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422536284.546185
_enable_loop = True
_template_filename = '/home/meder/cherrypy-default/template/index.mako'
_template_uri = 'index.mako'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n<head>\n<!-- Latest compiled and minified CSS -->\n<link rel="stylesheet" href="/static/css/bootstrap.min.css">\n\n<!-- Optional theme -->\n<link rel="stylesheet" href="/static/css/bootstrap-theme.min.css">\n\n<!-- Latest compiled and minified JavaScript -->\n<script src="/static/js/bootstrap.js"></script>\n<title>SqweebNet</title>\n</head>\n<body>\n<nav class="navbar navbar-inverse">\n  <div class="container-fluid">\n    <!-- Brand and toggle get grouped for better mobile display -->\n    <div class="navbar-header">\n      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n        <span class="sr-only">Toggle navigation</span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n      </button>\n      <a class="navbar-brand" href="/">SqweebNet</a>\n    </div>\n\n    <!-- Collect the nav links, forms, and other content for toggling -->\n    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n      <ul class="nav navbar-nav">\n        <li><a href="/charts">Charts</a></li>\n        <li class="dropdown">\n          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Menu<span class="caret"></span></a>\n          <ul class="dropdown-menu" role="menu">\n            <li><a href="http://github.com/mikeder">GitHub</a></li>\n            <li><a href="http://mikeder.net">mikeder.net</a></li>\n            <li><a href="http://sqweeb.net:8080">CherryMusic</a></li>\n            <li class="divider"></li>\n            <li><a href="#">Separated link</a></li>\n            <li class="divider"></li>\n            <li><a href="#">One more separated link</a></li>\n          </ul>\n        </li>\n      </ul>\n      <form class="navbar-form navbar-left" role="search">\n        <div class="form-group">\n          <input type="text" class="form-control" placeholder="Search">\n        </div>\n        <button type="submit" class="btn btn-default">Submit</button>\n      </form>\n      <ul class="nav navbar-nav navbar-right">\n        <li><a href="#">Link</a></li>\n        <li class="dropdown">\n          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Dropdown <span class="caret"></span></a>\n          <ul class="dropdown-menu" role="menu">\n            <li><a href="#">Action</a></li>\n            <li><a href="#">Another action</a></li>\n            <li><a href="#">Something else here</a></li>\n            <li class="divider"></li>\n            <li><a href="#">Separated link</a></li>\n          </ul>\n        </li>\n      </ul>\n    </div><!-- /.navbar-collapse -->\n  </div><!-- /.container-fluid -->\n</nav>\n<div class="container">\n  <!-- Example row of columns -->\n  <div class="row">\n    <div class="col-md-6">\n      <h2>CherryMusic</h2>\n    </div>\n    <div class="col-md-6">\n      <h2>RSDC</h2>\n    </div>\n   </div>\n  </div>\n\n  <hr>\n\n  <footer>\n    <p>&copy; Company 2014</p>\n  </footer>\n</div> <!-- /container -->\n\n\n</div>\n</body></html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 1, "15": 0}, "uri": "index.mako", "filename": "/home/meder/cherrypy-default/template/index.mako"}
__M_END_METADATA
"""
