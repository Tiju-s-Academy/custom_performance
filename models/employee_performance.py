from odoo import models, fields, api,_


class EmployeePerformance(models.Model):
    _name = 'employee.performance'
    _description = 'Employee Performance'
    _rec_name = 'employee_id'


    employee_id = fields.Many2one('hr.employee', string="Employee",help="Employee name",
                                  default=lambda self: self.env.user.employee_id.id,required=True)

    job_position_id = fields.Many2one(
        related='employee_id.job_id',
        string="Job Position",
        help="Job position of the employee",
        readonly=True
    )
    department_id = fields.Many2one(
        related='employee_id.department_id',
        string="Department",
        help="Department of the employee",
        readonly=True
    )
    branch_id = fields.Many2one(related='employee_id.branch_id',string='Branch')

    badge_ids = fields.One2many(
        comodel_name='gamification.badge.user',
        inverse_name='user_id',
        string='Badges',
        compute='_compute_badges',
        store=False
    )

    @api.depends('employee_id.badge_ids')
    def _compute_badges(self):
        for record in self:
            record.badge_ids = record.employee_id.badge_ids

    @api.model
    def initialize_employee_performance_data(self):
        """Initialize employee performance records for all employees."""
        employees = self.env['hr.employee'].search([])
        for employee in employees:
            print("working")
            self.create({'employee_id': employee.id})

class Employee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def create(self, vals):
        employee = super(Employee, self).create(vals)
        # Automatically create employee performance record when a new employee is created
        self.env['employee.performance'].create({'employee_id': employee.id})
        return employee

