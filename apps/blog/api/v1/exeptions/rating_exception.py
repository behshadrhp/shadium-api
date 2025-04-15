from rest_framework.exceptions import APIException


class AlreadyRatedException(APIException):
    status_code = 400
    default_detail = "Have already rated this post."
    default_code = "bad_request"
