# -*- coding: utf-8 -*-
# from odoo import http


# class TechscopeFilterEmployee(http.Controller):
#     @http.route('/techscope_filter_employee/techscope_filter_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/techscope_filter_employee/techscope_filter_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('techscope_filter_employee.listing', {
#             'root': '/techscope_filter_employee/techscope_filter_employee',
#             'objects': http.request.env['techscope_filter_employee.techscope_filter_employee'].search([]),
#         })

#     @http.route('/techscope_filter_employee/techscope_filter_employee/objects/<model("techscope_filter_employee.techscope_filter_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('techscope_filter_employee.object', {
#             'object': obj
#         })
