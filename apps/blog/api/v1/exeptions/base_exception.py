from rest_framework.exceptions import APIException


class AlreadyRatedException(APIException):
    status_code = 400
    default_detail = "Have already rated this post."
    default_code = "bad_request"

class AlreadyBookMarkedException(APIException):
    status_code = 400
    default_detail = "Have already BookMarked this post."
    default_code = "bad_request"

class AlreadyClappedException(APIException):
    status_code = 400
    default_detail = "Have already Clapped this post."
    default_code = "bad_request"
