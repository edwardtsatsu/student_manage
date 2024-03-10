from abc import ABC

from injector import inject
from sqlalchemy import insert

from configs.database import db_session
from src.dtos.student_course_dto import StudentCourseDto
from src.models import StudentCourse
from src.repositories.program_course_repository import ProgramCourseRepository
from src.repositories.student_course_repository import StudentCourseRepository
from src.repositories.user_repository import UserRepository
from src.services.base_service import BaseService


class StudentCourseService(BaseService, ABC):
    @inject
    def __init__(self, repository: StudentCourseRepository, user_repo: UserRepository,
                 program_course_repo: ProgramCourseRepository):
        super().__init__(repository)
        self.user_repo = user_repo
        self.program_course_repo = program_course_repo

    def store(self, data):
        semester_id = data['semester_id']
        courses = data['courses']
        user_id = data['user_id']

        user = self.user_repo.find_student_by_id(user_id)
        student = user.student
        program_id = user.student.program_id

        program_courses = self.program_course_repo.find_by_program_id_and_semester_id_and_course_id_in(
            program_id=program_id,
            semester_id=semester_id,
            course_ids=courses
        )

        student_courses = [{
            'student_id': student.id,
            'program_course_id': item.id
        } for item in program_courses]

        db_session.execute(insert(StudentCourse), student_courses)

        db_session.commit()

        return None

    def get_dto(self):
        return StudentCourseDto
