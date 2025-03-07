# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

from . import path

# query params
Model1Schema = schemas.StrSchema
ABSchema = schemas.StrSchema
AbSchema = schemas.StrSchema
ModelSelfSchema = schemas.StrSchema
ABSchema = schemas.StrSchema
RequestRequiredQueryParams = typing.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing.TypedDict(
    'RequestOptionalQueryParams',
    {
        '1': typing.Union[Model1Schema, str, ],
        'aB': typing.Union[ABSchema, str, ],
        'Ab': typing.Union[AbSchema, str, ],
        'self': typing.Union[ModelSelfSchema, str, ],
        'A-B': typing.Union[ABSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query__1 = api_client.QueryParameter(
    name="1",
    style=api_client.ParameterStyle.FORM,
    schema=Model1Schema,
    explode=True,
)
request_query_a_b = api_client.QueryParameter(
    name="aB",
    style=api_client.ParameterStyle.FORM,
    schema=ABSchema,
    explode=True,
)
request_query_ab = api_client.QueryParameter(
    name="Ab",
    style=api_client.ParameterStyle.FORM,
    schema=AbSchema,
    explode=True,
)
request_query__self = api_client.QueryParameter(
    name="self",
    style=api_client.ParameterStyle.FORM,
    schema=ModelSelfSchema,
    explode=True,
)
request_query_a_b2 = api_client.QueryParameter(
    name="A-B",
    style=api_client.ParameterStyle.FORM,
    schema=ABSchema,
    explode=True,
)
# header params
Model1Schema = schemas.StrSchema
ABSchema = schemas.StrSchema
ModelSelfSchema = schemas.StrSchema
ABSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing.TypedDict(
    'RequestOptionalHeaderParams',
    {
        '1': typing.Union[Model1Schema, str, ],
        'aB': typing.Union[ABSchema, str, ],
        'self': typing.Union[ModelSelfSchema, str, ],
        'A-B': typing.Union[ABSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header__2 = api_client.HeaderParameter(
    name="1",
    style=api_client.ParameterStyle.SIMPLE,
    schema=Model1Schema,
)
request_header_a_b3 = api_client.HeaderParameter(
    name="aB",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ABSchema,
)
request_header__self2 = api_client.HeaderParameter(
    name="self",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ModelSelfSchema,
)
request_header_a_b4 = api_client.HeaderParameter(
    name="A-B",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ABSchema,
)
# path params
Model1Schema = schemas.StrSchema
ABSchema = schemas.StrSchema
AbSchema = schemas.StrSchema
ModelSelfSchema = schemas.StrSchema
ABSchema = schemas.StrSchema
RequestRequiredPathParams = typing.TypedDict(
    'RequestRequiredPathParams',
    {
        '1': typing.Union[Model1Schema, str, ],
        'aB': typing.Union[ABSchema, str, ],
        'Ab': typing.Union[AbSchema, str, ],
        'self': typing.Union[ModelSelfSchema, str, ],
        'A-B': typing.Union[ABSchema, str, ],
    }
)
RequestOptionalPathParams = typing.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path__3 = api_client.PathParameter(
    name="1",
    style=api_client.ParameterStyle.SIMPLE,
    schema=Model1Schema,
    required=True,
)
request_path_a_b5 = api_client.PathParameter(
    name="aB",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ABSchema,
    required=True,
)
request_path_ab2 = api_client.PathParameter(
    name="Ab",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AbSchema,
    required=True,
)
request_path__self3 = api_client.PathParameter(
    name="self",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ModelSelfSchema,
    required=True,
)
request_path_a_b6 = api_client.PathParameter(
    name="A-B",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ABSchema,
    required=True,
)
# cookie params
Model1Schema = schemas.StrSchema
ABSchema = schemas.StrSchema
AbSchema = schemas.StrSchema
ModelSelfSchema = schemas.StrSchema
ABSchema = schemas.StrSchema
RequestRequiredCookieParams = typing.TypedDict(
    'RequestRequiredCookieParams',
    {
    }
)
RequestOptionalCookieParams = typing.TypedDict(
    'RequestOptionalCookieParams',
    {
        '1': typing.Union[Model1Schema, str, ],
        'aB': typing.Union[ABSchema, str, ],
        'Ab': typing.Union[AbSchema, str, ],
        'self': typing.Union[ModelSelfSchema, str, ],
        'A-B': typing.Union[ABSchema, str, ],
    },
    total=False
)


class RequestCookieParams(RequestRequiredCookieParams, RequestOptionalCookieParams):
    pass


request_cookie__4 = api_client.CookieParameter(
    name="1",
    style=api_client.ParameterStyle.FORM,
    schema=Model1Schema,
    explode=True,
)
request_cookie_a_b7 = api_client.CookieParameter(
    name="aB",
    style=api_client.ParameterStyle.FORM,
    schema=ABSchema,
    explode=True,
)
request_cookie_ab3 = api_client.CookieParameter(
    name="Ab",
    style=api_client.ParameterStyle.FORM,
    schema=AbSchema,
    explode=True,
)
request_cookie__self4 = api_client.CookieParameter(
    name="self",
    style=api_client.ParameterStyle.FORM,
    schema=ModelSelfSchema,
    explode=True,
)
request_cookie_a_b8 = api_client.CookieParameter(
    name="A-B",
    style=api_client.ParameterStyle.FORM,
    schema=ABSchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = schemas.AnyTypeSchema


request_body_body = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = schemas.AnyTypeSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _parameter_collisions(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        cookie_params: RequestCookieParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        parameter collision case
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs(RequestPathParams, path_params)
        self._verify_typed_dict_inputs(RequestCookieParams, cookie_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path__3,
            request_path_a_b5,
            request_path_ab2,
            request_path__self3,
            request_path_a_b6,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query__1,
            request_query_a_b,
            request_query_ab,
            request_query__self,
            request_query_a_b2,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        for parameter in (
            request_header__2,
            request_header_a_b3,
            request_header__self2,
            request_header_a_b4,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = request_body_body.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class ParameterCollisions(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def parameter_collisions(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        cookie_params: RequestCookieParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._parameter_collisions(
            body=body,
            query_params=query_params,
            header_params=header_params,
            path_params=path_params,
            cookie_params=cookie_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def post(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        cookie_params: RequestCookieParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._parameter_collisions(
            body=body,
            query_params=query_params,
            header_params=header_params,
            path_params=path_params,
            cookie_params=cookie_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


