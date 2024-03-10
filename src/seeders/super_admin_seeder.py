import uuid

from src.repositories.role_repository import RoleRepository
from src.repositories.user_repository import UserRepository
from passlib.hash import bcrypt


def seed_super_admin():
    role_repo = RoleRepository()
    super_admin_role = role_repo.find_by_name('Super Admin')
    admin = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'super@admin.com',
        'password': bcrypt.hash('password'),
        'phone_number': '0000000000',
        'role_id': super_admin_role.id,
    }
    repo = UserRepository()
    exists = repo.find_by_email(admin['email'])
    if exists is None:
        repo.store(admin)
