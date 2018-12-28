# -*- coding: utf-8 -*-
from odoo import http

# class Artige-social(http.Controller):
#     @http.route('/artige-social/artige-social/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/artige-social/artige-social/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('artige-social.listing', {
#             'root': '/artige-social/artige-social',
#             'objects': http.request.env['artige-social.artige-social'].search([]),
#         })

#     @http.route('/artige-social/artige-social/objects/<model("artige-social.artige-social"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('artige-social.object', {
#             'object': obj
#         })