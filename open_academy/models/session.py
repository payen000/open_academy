from odoo import models, fields, api


class Session(models.Model):
    _name = 'session'
    _description = 'Session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    active = fields.Boolean(default=True)
    duration = fields.Float()
    number_of_seats = fields.Integer()
    instructor_id = fields.Many2one('res.partner', domain="['|',('is_instructor', '=', True),('category_id.name', 'like', 'Teacher')]")
    course_id = fields.Many2one('course', required=True)
    attendee_ids = fields.Many2many('res.partner')
    taken_seats_percentage = fields.Char('Taken Seats %', compute='_compute_taken_seats_percentage')

    @api.depends('attendee_ids', 'number_of_seats')
    def _compute_taken_seats_percentage(self):
        for record in self:
            taken_seats_percentage = int(100*len(record.attendee_ids)/record.number_of_seats) if record.number_of_seats > 0 else 0
            record.taken_seats_percentage = taken_seats_percentage

    @api.onchange('attendee_ids', 'number_of_seats')
    def _onchange_seats(self):
        warning_message = [] 

        if self.number_of_seats < len(self.attendee_ids):
            if self.number_of_seats < 0:
                warning_message.append('There cannot be less than 0 seats available.')

            self.number_of_seats = self._origin.number_of_seats
            self.attendee_ids = self._origin.attendee_ids
            warning_message.append('Maximum seat capacity exceeded; discarded operation.')

        if warning_message:
            return {
                'warning': {
                    'title': 'Error in number of seats or attendees',
                    'message': ' '.join(warning_message),
                }
            }
