from odoo import models, fields, _
from odoo.exceptions import UserError


class AssignAttendeeSessions(models.TransientModel):
    _name = 'assign.attendee.sessions'
    _description = 'Assign Attendee Sessions'

    session_ids = fields.Many2many('session')
    attendee_ids = fields.Many2many('res.partner')

    def action_register_attendees(self):
        overloaded_sessions = self.session_ids.filtered(
            lambda session: session.number_of_seats < len(self.attendee_ids)
        )

        if overloaded_sessions:
            overloaded_sessions = ', '.join([session.name for session in overloaded_sessions])
            raise UserError(_('Aborted registration: attendee limit exceeded in %s.', overloaded_sessions))

        self.session_ids.write({'attendee_ids': self.attendee_ids})
