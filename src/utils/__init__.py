from django.core.exceptions import ValidationError
from rest_framework.serializers import ValidationError as DRFValidationError
from rest_framework.views import exception_handler as drf_exception_handler


def exception_handler(exc: Exception, context):
    if isinstance(exc, ValidationError):
        if hasattr(exc, "error_dict"):
            exc = DRFValidationError(exc.error_dict)
        elif not hasattr(exc, "message"):
            exc = DRFValidationError(exc.error_list)
        else:
            exc = DRFValidationError(exc.message, exc.code)

    return drf_exception_handler(exc, context)
