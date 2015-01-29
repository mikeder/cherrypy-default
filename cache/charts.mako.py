# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422536376.342308
_enable_loop = True
_template_filename = '/home/meder/cherrypy-default/template/charts.mako'
_template_uri = 'charts.mako'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n<head>\n<!-- Latest compiled and minified CSS -->\n<link rel="stylesheet" href="/static/css/bootstrap.min.css">\n<link rel="stylesheet" href="/static/css/jumbotron.css">\n\n<!-- Optional theme -->\n<link rel="stylesheet" href="/static/css/bootstrap-theme.min.css">\n\n<!-- Latest compiled and minified JavaScript -->\n<script src="/static/js/bootstrap.min.js"></script>\n<title>SqweebNet</title>\n</head>\n<body>\n<nav class="navbar navbar-inverse navbar-fixed-top">\n  <div class="container">\n    <div class="navbar-header">\n      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\n        <span class="sr-only">Toggle navigation</span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n      </button>\n      <a class="navbar-brand" href="/">SqweebNet</a>\n    </div>\n    <div id="navbar" class="navbar-collapse collapse">\n      <form class="navbar-form navbar-right">\n        <div class="form-group">\n          <input type="text" placeholder="Email" class="form-control">\n        </div>\n        <div class="form-group">\n          <input type="password" placeholder="Password" class="form-control">\n        </div>\n        <button type="submit" class="btn btn-success">Sign in</button>\n      </form>\n    </div><!--/.navbar-collapse -->\n  </div>\n</nav>\n\n<div class="container" align="center">\n  <h1>DHT22 Charts</h1>\n  <embed type="image/svg+xml" src="/static/charts/current.svg" /><br>\n  <embed type="image/svg+xml" src="/static/charts/last24.svg" /><br>\n</div> <!-- /container -->\n\n\n</div>\n</body></html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 1, "15": 0}, "uri": "charts.mako", "filename": "/home/meder/cherrypy-default/template/charts.mako"}
__M_END_METADATA
"""
