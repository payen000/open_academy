from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime


class Session(models.Model):
    _name = 'session'
    _description = 'Session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    stop_date = fields.Date()
    lasting_days = fields.Integer(compute='_compute_lasting_days')
    active = fields.Boolean(default=True)
    duration = fields.Float()
    number_of_seats = fields.Integer()
    instructor_id = fields.Many2one(
        "res.partner", domain="['|', ('is_instructor', '=', True), ('category_id.name', 'like', 'Teacher')]"
    )
    course_id = fields.Many2one('course', required=True)
    attendee_ids = fields.Many2many('res.partner')
    taken_seats_percentage = fields.Char('Taken Seats %', compute='_compute_taken_seats_percentage')
    attendee_count = fields.Integer(compute='_compute_attendee_count', store=True)

    @api.depends('attendee_ids', 'number_of_seats')
    def _compute_taken_seats_percentage(self):
        for record in self:
            n_seats = record.number_of_seats
            n_attendees = 100*len(record.attendee_ids)
            taken_seats_percentage = int(n_attendees/n_seats) if n_seats > 0 else 0
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

    @api.constrains('attendee_ids', 'instructor_id')
    def _check_instructor_id_in_attendee_ids(self):
        for record in self:
            if record.instructor_id in record.attendee_ids:
                error_message = _('Instructor cannot be an attendee for their own session!')
                raise ValidationError(error_message)

    @api.depends('start_date', 'stop_date')
    def _compute_lasting_days(self):
        for record in self:
            fmt = '%Y-%m-%d'
            start_date = str(record.start_date)
            stop_date = str(record.stop_date)
            d1 = datetime.strptime(start_date, fmt)
            d2 = datetime.strptime(stop_date, fmt)
            record.lasting_days = (d2 - d1).days

    @api.depends('attendee_ids')
    def _compute_attendee_count(self):
        for record in self:
            record.attendee_count = len(record.attendee_ids)
