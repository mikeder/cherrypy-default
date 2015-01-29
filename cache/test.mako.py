# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422528773.449425
_enable_loop = True
_template_filename = '/home/meder/cherrypy-default/template/test.mako'
_template_uri = 'test.mako'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        body = context.get('body', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(unicode(body))
        __M_writer(u'\nOther stuff\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"28": 22, "21": 1, "22": 1, "15": 0}, "uri": "test.mako", "filename": "/home/meder/cherrypy-default/template/test.mako"}
__M_END_METADATA
"""
