# -*- coding: utf-8 -*-
# from odoo import http


# class PluginsTest(http.Controller):
#     @http.route('/plugins_test/plugins_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/plugins_test/plugins_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('plugins_test.listing', {
#             'root': '/plugins_test/plugins_test',
#             'objects': http.request.env['plugins_test.plugins_test'].search([]),
#         })

#     @http.route('/plugins_test/plugins_test/objects/<model("plugins_test.plugins_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('plugins_test.object', {
#             'object': obj
#         })
