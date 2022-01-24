from odoo import api, fields, models


class ReportSession(models.AbstractModel):
    _name = 'report.sesion'
    _description = 'Get printed sessions report.'

    session_ids = fields.Many2many('session')
