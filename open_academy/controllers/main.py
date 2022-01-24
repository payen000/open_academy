from odoo import http


# This controller is added to bypass the error:
# "edit_custom() missing 1 required positional argument: 'custom_id'".
# when changing the layout of a dashboard.
class DashboardController(http.Controller):
    @http.route('/web/view/edit_custom', type='json', auth="user")
    def edit_custom(self, arch):
        return {'result': True}
