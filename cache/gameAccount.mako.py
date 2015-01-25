# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422179497.307744
_enable_loop = True
_template_filename = '/home/mike/Documents/cherrypy-default/template/gameAccount.mako'
_template_uri = 'gameAccount.mako'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<html>\n<head>\n<title>Game Account Creation - NOC Tool</title>\n</head>\n<body>\n<h1>This is a test, it is only a test.</h1>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 1, "15": 0}, "uri": "gameAccount.mako", "filename": "/home/mike/Documents/cherrypy-default/template/gameAccount.mako"}
__M_END_METADATA
"""
