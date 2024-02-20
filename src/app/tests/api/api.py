from typing import Literal

import pytest
from django.utils.functional import cached_property
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class APIMixin:
    def post(self, *args, expected_status=status.HTTP_201_CREATED, **kwargs):
        return self._run_http_method(
            *args,
            expected_status=expected_status,
            method="post", 
            **kwargs)
    
    def patch(self, *args, expected_status=status.HTTP_200_OK, **kwargs):
        return self._run_http_method(
            *args, 
            expected_status=expected_status, 
            method="patch", 
            **kwargs)
    
    def put(self, *args, expected_status=status.HTTP_200_OK, **kwargs):
        return self._run_http_method(
            *args, 
            expected_status=expected_status, 
            method="put", 
            **kwargs)

    def get(self, *args, expected_status=status.HTTP_200_OK, **kwargs):
        return self._run_http_method(
            *args, 
            expected_status=expected_status, 
            method="get", 
            **kwargs)
    
    def delete(self, *args, expected_status=status.HTTP_200_OK, **kwargs):
        return self._run_http_method(
            *args, 
            expected_status=expected_status, 
            method="delete",
            **kwargs)

    def _run_http_method(self, *args, expected_status: int, 
                         method: Literal["post", "get", "patch", "put", "delete"], **kwargs):
        _http_method = getattr(self.client, method)
        response = _http_method(*args, follow=True, format='json', **kwargs)
        assert response.status_code, expected_status
        return response.json() if method != "delete" else {}

class TestAPIClient(APIMixin):
    
    @cached_property
    def client(self):
        return APIClient()
    

class BaseAPITestCase(APITestCase, APIMixin):
    pass