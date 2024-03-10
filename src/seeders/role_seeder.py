from src.repositories.role_repository import RoleRepository


def seed_roles():
    roles = [
        {
            'name': 'Super Admin'
        },
        {
            'name': 'Student'
        },
    ]
    repo = RoleRepository()
    for role in roles:
        exists = repo.find_by_name(role['name'])
        if exists is None:
            repo.store(role)


