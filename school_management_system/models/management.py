from odoo import api, fields, models, _

class ManagementManagement(models.Model):
    _name = "management.management"
    _order = "name"
    _description = "Management"
    
    name = fields.Char(string="Name")

    student_id = fields.One2many('student.student','management_id', string = "Student" )
    teacher_id = fields.One2many('teacher.teacher','management_id', string = "Teacher")
    
