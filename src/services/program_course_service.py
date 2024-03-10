from abc import ABC
from datetime import datetime

from injector import inject
from sqlalchemy import update, insert

from configs.database import db_session
from src.dtos.program_course_dto import ProgramCourseDto
from src.dtos.program_dto import ProgramDto
from src.exceptions import ServerErrorException
from src.models import ProgramCourse
from src.repositories.program_course_repository import ProgramCourseRepository
from src.services.base_service import BaseService


class ProgramCourseService(BaseService, ABC):
    @inject
    def __init__(self, repository: ProgramCourseRepository):
        super().__init__(repository)

    def assign_courses(self, data):
        program_id = data['program_id']
        semester_id = data['semester_id']
        courses = data['courses']
        courses_map = {item: item for item in courses}

        current_program_courses = self.repository.find_by_program_id_and_semester_id(program_id, semester_id)
        current_program_courses_map = {item.course_id: item for item in current_program_courses}

        courses_to_remove = [item.course_id for item in current_program_courses if item not in courses_map]
        courses_to_add = [item for item in courses if item not in current_program_courses_map]

        try:
            # remove courses
            if len(courses_to_remove) > 0:
                db_session.execute(update(ProgramCourse)
                                   .where(ProgramCourse.deleted_at.is_(None))
                                   .where(ProgramCourse.program_id == program_id)
                                   .where(ProgramCourse.semester_id == semester_id)
                                   .where(ProgramCourse.course_id.in_(courses_to_remove))
                                   .values(deleted_at=datetime.now()))

            # add course
            if len(courses_to_add) > 0:
                new_courses = [{
                    'program_id': program_id,
                    'semester_id': semester_id,
                    'course_id': course,
                } for course in courses_to_add]

                db_session.execute(insert(ProgramCourse), new_courses)

                db_session.commit()

            program_courses = self.repository.find_by_program_id_and_semester_id(program_id, semester_id)

            return list(map(lambda x: ProgramCourseDto.from_orm(x).dict(), program_courses))

        except Exception as e:
            print(f'error assigning courses {e}')
            db_session.rollback()
            raise ServerErrorException(description='error assigning courses')

    def get_dto(self):
        return ProgramCourseDto
