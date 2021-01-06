from odoo import models, fields, api, _

class CreateCheck(models.TransientModel):
    _name = 'create.check'

    date_action = fields.Date('Date current action', required=False, readonly=False, select=True
                              , default=lambda s: fields.Date.context_today(s))