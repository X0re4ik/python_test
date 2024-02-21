import json
from typing import Any
from rest_framework.response import Response


class UnexpectedError:

    def __init__(self, get_response) -> None:
        self._get_response = get_response
    
    def __call__(self, request) -> Any:
        response = self._get_response(request)
        if 200 <= response.status_code < 300:  
            return response
        if isinstance(response, Response):
            response.content = str.encode(json.dumps({
                "error": response.data
            }))
        return response
    
    def process_exception(self, request, exception):
        return Response({
            "error": exception
        })
