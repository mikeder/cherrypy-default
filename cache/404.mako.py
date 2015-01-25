# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422180702.661684
_enable_loop = True
_template_filename = '/home/mike/Documents/cherrypy-default/template/404.mako'
_template_uri = '404.mako'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u"\n<title>Page Not Found</title>\nYou seem to have requested a page that doesn't exist.\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 1, "15": 0}, "uri": "404.mako", "filename": "/home/mike/Documents/cherrypy-default/template/404.mako"}
__M_END_METADATA
"""
