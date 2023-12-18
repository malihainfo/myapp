# from odoo import api, models

# class TeacherSummary(models.AbstractModel):
#     _name = 'report.Bdtask_school_management_system.report_teacher_summary'
#     _description = 'Teacher Summary'

#     @api.model
#     def _get_report_values(self, docids, data=None):
#         print("abcddddddddddddddcccccccccccccccccccccc")
#         teachers = self.env['teacher.teacher'].search([])
        
#         teacher_list = []
#         for teacher in teachers:
#             val = {
#                 'name': teacher.name,
#                 'department': teacher.department,
#                 'gender': teacher.gender,
#             }
#             teacher_list.append(val)
#         print("teacher list", teacher_list)

#         return {
#             'doc_ids': docids,
#             'doc_model':'teacher.teacher',
#             'docs': teachers,
#             'data': data,
#             'teacher_list': teacher_list,
#         }