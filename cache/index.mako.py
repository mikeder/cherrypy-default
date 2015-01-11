# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1420978818.877634
_enable_loop = True
_template_filename = '/home/mike/Documents/noc-tools/template/index.mako'
_template_uri = 'index.mako'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n<head>\n<link href="/static/css/style.css" rel="stylesheet">\n<title>NOC Tool v0.01</title>\n<script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>\n     <script type="text/javascript">\n       $(document).ready(function() {\n\n         $("#generate").click(function(e) {\n           $.post("/generator", {"length": $("select[name=\'length\']").val()})\n            .done(function(string) {\n               $("#string").show();\n               $("#string input").val(string);\n            });\n           e.preventDefault();\n         });\n       });\n     </script>\n</head>\n<body>\n<h2>NOC Tool aka Derpstation 9000</h2>\n<hr>\nRandom sequence generator:\n<form name="generator">\n  <select name="length">\n    <option value="5">5</option>\n    <option value="6">6</option>\n    <option value="7">7</option>\n    <option value="8">8</option>\n    <option value="9">9</option>\n    <option value="10">10</option>\n    <option value="11">11</option>\n    <option value="12">12</option>\n    <option value="13">13</option>\n    <option value="14">14</option>\n    <option value="15">15</option>\n    <option value="16">16</option>\n    <option value="17">17</option>\n    <option value="18">18</option>\n    <option value="19">19</option>\n    <option value="20">20</option>\n  </select>\n  <button id="generate">Generate</button>\n</form>\n<div id="string">\n  <input type="text" width="25" />\n</div>\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 1, "15": 0}, "uri": "index.mako", "filename": "/home/mike/Documents/noc-tools/template/index.mako"}
__M_END_METADATA
"""
