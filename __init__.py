from . import models

def post_init_hook(env):
    """Initialize employee performance data after module installation."""
    env['employee.performance'].initialize_employee_performance_data()
