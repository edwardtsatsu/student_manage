from abc import ABC

from injector import inject

from passlib.hash import bcrypt
from configs.database import db_session
from src.dtos.program_dto import ProgramDto
from src.dtos.student_dto import StudentDto
from src.exceptions import ServerErrorException
from src.models import User, Student
from src.repositories.role_repository import RoleRepository
from src.repositories.student_repository import StudentRepository
from src.services.base_service import BaseService
from utils import generate_password, generate_student_code


class StudentService(BaseService, ABC):
    @inject
    def __init__(self, repository: StudentRepository, role_repo: RoleRepository):
        super().__init__(repository)
        self.role_repo = role_repo

    def find_all(self, query=None):
        resources = self.repository.find_all(query)
        return list(map(lambda x: self.__build_dto(x, x.user), resources))

    def store(self, data):
        student_role = self.role_repo.find_by_name('Student')
        try:
            user_data = {
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'middle_name': data['middle_name'],
                'role_id': student_role.id,
                'email': data['email'],
                'phone_number': data['phone_number'],
                'password': bcrypt.hash(generate_password()),
            }
            user = User(**user_data)

            db_session.add(user)

            db_session.flush()

            student_data = {
                'user_id': user.id,
                'student_code': generate_student_code(),
                'program_id': data['program_id'],
                'gender': data['gender'],
                'date_of_birth': data['date_of_birth'],
                'current_year': 1,
            }
            student = Student(**student_data)

            db_session.add(student)
            db_session.commit()

            student_dto = self.__build_dto(student, user)

            return student_dto

        except Exception as e:
            print(f'error saving student {e}')
            db_session.rollack()
            raise ServerErrorException(description='Error registering student')

    def get_dto(self):
        return StudentDto

    def __build_dto(self, student, user):
        return StudentDto(
            id=student.id,
            first_name=user.first_name,
            last_name=user.last_name,
            middle_name=user.middle_name,
            email=user.email,
            phone_number=user.phone_number,
            gender=student.gender,
            date_of_birth=student.date_of_birth,
            student_code=student.student_code,
            is_active=student.is_active,
            created_at=student.created_at,
            current_year=student.current_year,
            program=ProgramDto(
                id=student.program.id,
                name=student.program.name,
                code=student.program.code,
                duration_in_years=student.program.duration_in_years,
                created_at=student.program.created_at,
            ).dict()
        ).dict()
