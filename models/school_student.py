from odoo import api, fields, models
import datetime

class Student(models.Model):
    _name = "school.student"
    _description = "datos del estudiante"

    name = fields.Char(string = "Nombre del estudiante") 
    birth_date = fields.Date(string = "Fecha de nacimiento")
    age = fields.Integer(string = "Edad",compute = "_computed_age")
    final_exam_grade = fields.Float(string = "Nota final del curso")
    subject_ids = fields.Many2Many("school.subject", "student_ids", string = "subjects")

    @api.depends("birth_date")
    def _computed_age(self):
        actual_date = datetime.date.today()

        for student in self:
            student_birth_date = fields.Datetime.to_datetime(student.student_birth_date).date()
            student_age = (actual_date - student_birth_date).days() / 365
            student_age = int(student_age)
            student.age = student_age
