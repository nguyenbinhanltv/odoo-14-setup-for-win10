from odoo import fields, models, api, _
from odoo.exceptions import UserError

class school_student(models.Model):
    _name = "school.student"
    _description = "school_student.school_student"

    name = fields.Char(string="Student name")
    school_id = fields.Many2one("school.profile", string="School")
    hobby_list = fields.Many2many("hobby", "school_hobby_rel", "student_id", "hobby_id", string="Hobbies")
    is_virtual_school = fields.Boolean(related="school_id.is_virtual_class", string="Is virtual class")
    school_address = fields.Text(related="school_id.address", string="School address")

    def write(self, vals):
        rtn = super(school_student, self).create(vals)
        if not rtn.hobby_list:
            raise UserError(_("Plese chose least one hobby!"))
        return rtn

class SchoolProfile(models.Model):
    _inherit = "school.profile"

    school_list = fields.One2many("school.student", "school_id", string="Students")

    @api.model
    def create(self, vals):
        rtn = super(SchoolProfile, self).create(vals)
        if not rtn.school_list:
            raise UserError(_("Student list is empty!"))
        return rtn

class Hobbies(models.Model):
    _name = "hobby"

    name = fields.Char(string="Hobby")