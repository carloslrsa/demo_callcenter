# -*- coding: utf-8 -*-
{
    'name': "Modulo Call Center",

    'summary': """
        Modulo para operadores de Call Center
        """,

    'description': """
        El módulo se encarga de presentar un portal de acceso
        a los operadores del Área de Call Center de la empresa
        Taxi Monterrico, en el cual pueda permitirle atender las
        comunicaciones vía telefónica como son la atención de incidentes,
        quejas y demás; de manera integrada con las demás áreas de la empresa.
    """,

    'author': "Equipo de Call Center",
    'website': "http://es.dota2.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    'application' : True,
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}