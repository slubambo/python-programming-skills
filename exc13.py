class HttpException(Exception):
    statusCode = None
    message = None

    def __init__(self):
        super().__init__(
            f'Status Code: {self.statusCode}! Message: {self.message}')


class NotFoundException(HttpException):
    statusCode = 404
    message = 'Server not Found'


class ServerError(HttpException):
    statusCode = 500
    message = 'Server is Down! We shall soon be available'


def raiseNotFoundError():
    raise NotFoundException()


raiseNotFoundError()
