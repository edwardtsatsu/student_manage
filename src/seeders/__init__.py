from src.seeders.role_seeder import seed_roles
from src.seeders.super_admin_seeder import seed_super_admin


def run_seed():
    seed_roles()
    seed_super_admin()
