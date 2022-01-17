from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(help='Is this partner a session instructor?')
    session_ids = fields.Many2many('session')
