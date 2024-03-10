from flask_injector import FlaskInjector

from src.di.modules.course_module import CourseModule
from src.di.modules.program_course_module import ProgramCourseModule
from src.di.modules.program_module import ProgramModule
from src.di.modules.semester_module import SemesterModule
from src.di.modules.student_module import StudentModule
from src.di.modules.user_module import UserModule


def init_container(app):
    FlaskInjector(app=app, modules=[
        UserModule,
        ProgramModule,
        SemesterModule,
        CourseModule,
        ProgramCourseModule,
        StudentModule,
    ])
