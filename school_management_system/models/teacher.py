from odoo import api, fields, models, _


class TeacherTeacher(models.Model):
    _name = "teacher.teacher"
    _order = "name"
    _description = "Teacher"

    name = fields.Char(string="Name", required=True)
    department = fields.Char(string="Department", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection ([ 
        ('male', 'Male'),
        ('female', 'Female'),

    ])
    salary = fields.Float(string="Salary")
    is_active = fields.Boolean(string="Is active?")

    student_id = fields.One2many('student.student','teacher_id', string = "Student")
    management_id = fields.Many2one('management.management', string = "Management")

  
    

        

