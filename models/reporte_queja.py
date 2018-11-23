# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReporteQueja(models.Model):
	_name = "reporte.queja"

	id = fields.Char(string="Id")
	tipo = fields.Selection([('Queja','Queja'), ('Reclamo', 'Reclamo'),('Sugerencia', 'Sugerencia'), ('Legal','Legal')], string="Tipo")
	nombres = fields.Char(string="Nombres")
	direccion = fields.Char(string="Direccion")
	telefono = fields.Char(string="Telefono")
	email = fields.Char(string="Email")
	estado = fields.Selection([('Recibido','Recibido'), ('Procesando', 'Procesando'),('Aceptado', 'Aceptado'), ('Rechazado','Rechazado')], string="Estado")