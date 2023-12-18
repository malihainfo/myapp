from odoo import api, fields, models, _


class SaleOrder(models.Model):
    '''we inherited this model for adding test field'''
    _inherit = "sale.order"

    test = fields.Char(string = "Test")
    teacher_id = fields.Many2one('res.partner',string = "Teacher id", change_default = True)
    @api.onchange('teacher_id')
    def onchange_teacher_id(self):
        for rec in self.order_line:
            rec.teacher_id = self.teacher_id.id

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    teacher_id = fields.Many2one('res.partner',string = "Teacher id", change_default = True)

    @api.model
    def create(self,vals):
        res= super(SaleOrderLine, self).create(vals)
        for rec in res:
            rec.teacher_id = rec.order_id.teacher_id.id
        return res


