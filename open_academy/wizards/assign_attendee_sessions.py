from odoo import models, fields, _
from odoo.exceptions import ValidationError


class AssignAttendeeSessions(models.TransientModel):
    _name = 'assign.attendee.sessions'
    _description = 'Assign Attendee Sessions'

    session_id = fields.Many2one('session')
    attendee_ids = fields.Many2many('res.partner')

    def action_register_attendees(self):
        if self.session_id.number_of_seats < len(self.attendee_ids):
            raise ValidationError(_('Aborted registration: attendee limit exceeded'))

        self.session_id.attendee_ids = self.attendee_ids
