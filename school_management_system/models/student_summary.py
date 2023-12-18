from odoo import api, models

class StudentSummary(models.AbstractModel):
    _name = 'report.school_management_system.report_student_summary'
    _description = 'Student Summary'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("abcddddddddddddddcccccccccccccccccccccc")
        students = self.env['student.student'].search([])
        print("students:", students)
        student_list = []
        for student in students:
            val = {
                'name': student.name,
                'roll': student.roll,
                'gender': student.gender,
            }
            student_list.append(val)
        print("student list", student_list)

        return {
            'doc_ids': docids,
            'doc_model':'student.student',
            'docs': students,
            'data': data,
            'student_list': student_list,
        }
