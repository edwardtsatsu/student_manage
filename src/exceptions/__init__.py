from pydantic import ValidationError

from src.exceptions.access_denied_exception import AccessDeniedException
from src.exceptions.exception_handler import resource_not_found_handler, bad_request_handler, email_exists_handler, \
    access_denied_handler, order_update_handler
from src.exceptions.not_found_exception import ResourceNotFoundException
from src.exceptions.server_error_exception import ServerErrorException


def register_handlers(app):
    app.register_error_handler(ResourceNotFoundException, resource_not_found_handler)
    app.register_error_handler(ValidationError, bad_request_handler)
    app.register_error_handler(AccessDeniedException, access_denied_handler)
    app.register_error_handler(ServerErrorException, server_error_exception)
