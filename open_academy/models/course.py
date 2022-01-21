from odoo import models, fields, _


class Course(models.Model):
    _name = 'course'
    _description = 'Course'

    name = fields.Char(required=True)
    title = fields.Char(required=True, copy=False)
    description = fields.Text()
    responsible_user_id = fields.Many2one('res.users')
    session_ids = fields.One2many('session', 'course_id')
    _sql_constraints = [
        (
            'description',
            'CHECK(title != description)',
            _('The course title and the course description must be different!')
        ),
        (
            'title',
            'UNIQUE(title)',
            _('The course name must be unique!')
        ),
    ]

    def copy(self):
        new_title = f'copy of [{self.title}]'
        count = self.search_count([('title', 'like', new_title), ])
        new_title += f' ({count})' if count > 0 else ''
        default = {'title': new_title, }

        return super().copy(default=default)
