from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # db.init_app(app)
    jwt.init_app(app)

    from src.controllers import auth_router, role_router, user_router, student_router, account_router, payment_request_router, program_router, fee_router, department_router
    app.register_blueprint(auth_router.bp)
    app.register_blueprint(role_router.bp)
    app.register_blueprint(user_router.bp)
    app.register_blueprint(student_router.bp)
    app.register_blueprint(account_router.bp)
    app.register_blueprint(payment_request_router.bp)
    app.register_blueprint(program_router.bp)
    app.register_blueprint(fee_router.bp)
    app.register_blueprint(department_router.bp)

    return app
