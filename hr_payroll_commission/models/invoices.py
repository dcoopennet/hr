# -*- coding: utf-8 -*-
# © 2016 Coninckx David (Open Net Sarl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    # ---------- Fields management

    slip_id = fields.Many2one('hr.payslip', string='Pay slip')
