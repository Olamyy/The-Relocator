class BaseRelocError(Exception):
    def __init__(self, message=None, http_status=None):
        super(BaseRelocError, self).__init__(message)

        self.message = message
        self.http_status = http_status


class InvalidPathError(BaseRelocError):
    """
    Auth Key Not Provided
    """
    pass


class RequiresFileError(BaseRelocError):
    """
    Auth Key Not Provided
    """
    pass
