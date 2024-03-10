import uuid


def generate_password():
    return 'password'


def generate_student_code():
    return str(uuid.uuid4())


def get_offset(page=None, limit=20):
    p = int('0' if page == '' else str(page))
    if p <= 1:
        return 0
    return (p - 1) * limit
