import werkzeug.exceptions


class ServerErrorException(werkzeug.exceptions.HTTPException):
    code = 500
