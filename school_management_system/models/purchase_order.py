from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    test = fields.Char(string = "Test")
    is_ok = fields.Boolean(string="is_ok", store = True, default = False)
    teacher_id = fields.Many2one('res.partner',string = "Teacher id", change_default = True)

    def action_ok(self):
        self.is_ok = True
    def action_not_ok(self):
        self.is_ok = False
    @api.onchange('teacher_id')
    def onchange_teacher_id(self):
        for rec in self.order_line:
            rec.teacher_id = self.teacher_id.id

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    test2 = fields.Char(string = "Test 2")
    test3 = fields.Char(string = "Test 3")
    teacher_id = fields.Many2one('res.partner',string = "Teacher id", change_default = True)

    @api.model
    def create(self,vals):
        res= super(PurchaseOrderLine, self).create(vals)
        for rec in res:
            rec.teacher_id = rec.order_id.teacher_id.id
        return res
        
