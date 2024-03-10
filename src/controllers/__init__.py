from src.controllers.auth_controller import auth_bp
from src.controllers.course_controller import course_bp
from src.controllers.grade_controller import grade_bp
from src.controllers.program_controller import program_bp
from src.controllers.program_course_controller import program_course_bp
from src.controllers.semester_controller import semester_bp
from src.controllers.student_controller import student_bp


def register_routes(app, version):
    app.register_blueprint(auth_bp, url_prefix=f'/api/{version}/auth')
    app.register_blueprint(semester_bp, url_prefix=f'/api/{version}/semesters')
    app.register_blueprint(program_bp, url_prefix=f'/api/{version}/programs')
    app.register_blueprint(course_bp, url_prefix=f'/api/{version}/courses')
    app.register_blueprint(student_bp, url_prefix=f'/api/{version}/students')
    app.register_blueprint(program_course_bp, url_prefix=f'/api/{version}/program_courses')
    app.register_blueprint(grade_bp, url_prefix=f'/api/{version}/grades')
