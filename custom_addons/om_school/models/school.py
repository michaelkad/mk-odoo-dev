import math

from num2words import num2words

from odoo import models, fields, api, _


# class AccountPayment(models.Model):
#     _inherit = 'account.payment'
#
#     school_account = fields.Char(string='School Account', required=True)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    date_test = fields.Date('Date by mk', required=False, readonly=False, select=True
                            , default=lambda s: fields.Date.context_today(s))


class SchoolBuilding(models.Model):
    _name = 'school.building'
    _inherit = ['mail.thread', 'mail.activity.mixin', ]
    _description = 'School Record'
    _rec_name = 'school_name'
    _order = 'id desc'

    @api.depends('amount')
    def moneytostring(self):
        currency = 'Dollars'
        change = 'Cents'
        precision = 2

        for rec in self:
            change_amt = math.floor((rec.amount - int(rec.amount)) * pow(10, precision))
            print(change_amt)
            rec.amount_in_word = '{main_amt} {main_word}'.format(
                main_amt=num2words(int(rec.amount)).title(),
                main_word=currency,
            )
            if change_amt > 0:
                rec.amount_in_word += ' and {change_amt} {change_word}'.format(
                    change_amt=num2words(change_amt).title(),
                    change_word=change,
                )

    school_name = fields.Char(string='School Name', required=True)
    email = fields.Char(string='Email')
    notes = fields.Char(string='Notes')
    description = fields.Char(string='Description')
    school_building = fields.Integer(string='Building Number')
    school_rooms = fields.Integer(string='Rooms number')
    image = fields.Binary(string='Image')
    name_seq = fields.Char(string='Building Id', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))
    amount = fields.Float(string='Money Amount', default=0)
    amount_in_word = fields.Char(string="Amount in words", compute=moneytostring)
    street_address = fields.Char(string='Stress Address')
    street_address2 = fields.Char(string='Stress Address2')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    zip = fields.Char(string='Zip Code')
    date_action = fields.Date('Date current action', required=False, readonly=False, select=True
                              , default=lambda s: fields.Date.context_today(s))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('school.building.sequence') or _('New')
        result = super(SchoolBuilding, self).create(vals)
        return result
