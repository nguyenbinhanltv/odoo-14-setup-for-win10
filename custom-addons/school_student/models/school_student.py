from odoo import fields, models

class school_student(models.Model):
    _name = "school.student"
    _description = "school_student.school_student"

    name = fields.Char(string="Student name")
    school_id = fields.Many2one("school.profile", string="School")

class SchoolProfile(models.Model):
    _inherit = "school.profile"

    school_list = fields.One2many("school.student", "school_id", string="School List")