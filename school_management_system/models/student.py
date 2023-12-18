from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class StudentStudent(models.Model):
    _name = "student.student"
    _order = "name"
    _description = "Student"

    # = fields.Char(string="Serial Num", required = True, default = lambda self: self._next_serial_number())
    roll = fields.Char(string="Roll Number", default=lambda self: self._generate_sequece())
    name = fields.Char(string="Name", required=True)
    st_class = fields.Integer(string="Class")
    is_pass = fields.Boolean(string="passed", compute = "_compute_name", store = True)
    is_fail = fields.Boolean(string="failed", compute = "_compute_name", store = True)
    a = fields.Integer(string="a", required=True)
    b = fields.Integer(string="b", required=True)
    # roll = fields.Integer(string="Roll", required=True)
    age = fields.Integer(string="Age", required= True
    )
    gender = fields.Selection ([ 
        ('male', 'Male'),
        ('female', 'Female'),

    ])
    state = fields.Selection([('draft','Draft'), ('confirm', 'Confirmed'), ('cancel', 'Cancel')], default = 'draft', string = 'Status')

    @api.model
    def _generate_sequece(self):
        last_sequence = self.env['student.student'].search([],order='roll desc', limit=1)
        if last_sequence:
            last_value = int(last_sequence.roll[2:])
            next_value = last_value+1
        else:
            next_value=1
        formated_value = f"ID {next_value:02d}"
        return formated_value

    # @api.model
    # def create(self, vals):
    #     print("vals for create.....", vals)
    #     print("self for create .........", self)
        
    #     if vals.get('serial_num'):
    #         serial_num = self.env['student.student'].search([('serial_num','=', vals['serial_num'])])
    #         print("serial_num for create....", serial_num)
    #         if serial_num:
    #             raise ValidationError(_("serial number already exists"))
    #     return super(StudentStudent, self).create(vals)




    @api.depends('a','b')
    def _compute_name(self):
        self.is_pass = False
        self.is_fail = False
        if self.a + self.b > 40:
            self.is_pass = True
        else:
            self.is_fail = True

    @api.onchange('age')
    def _onchange_age(self):
        if self.age > 20:
            raise ValidationError(_("Age must be less than 20"))
    
    @api.onchange('roll')
    def _onchange_roll(self):
        roll= self.env['student.student'].search([('roll','=', self.roll)])
        if roll:
            raise ValidationError(_("Roll already exists"))
    
            
    @api.constrains('age')
    def _age_check(self):
        if self.age<0:
            raise ValidationError(_("Age can't be Negative"))

    teacher_id = fields.Many2one('teacher.teacher', string = "Teacher")
    management_id = fields.Many2one('management.management', string = "Management")


    # @api.model
    # def create(self, vals):
    #     print("vals for create.....", vals)
    #     print("self for create .........", self)
        
    #     if vals.get('roll'):
    #         roll= self.env['student.student'].search([('roll','=', vals['roll'])])
    #         print("roll for create....", roll)
    #         if roll:
    #             raise ValidationError(_("Roll already exists"))
    #     return super(StudentStudent, self).create(vals)
    
    # def write(self, vals):
    #     print("vals for create.....", vals)
    #     print("self for create .........", self)

    #     if vals.get('roll'):
    #         roll= self.env['student.student'].search([('roll','=', vals['roll'])])
    #         print("roll for create....", roll)
    #         if roll:
    #             raise ValidationError(_("Roll already exists"))
    #     return super(StudentStudent, self).write(vals)
   
 