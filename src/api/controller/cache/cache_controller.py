from fastapi import APIRouter, Depends
from src.api.docs.openapi import generate_validation_error_response, generate_unprocessable_entity_error_response
from src.api.handler.error_response import ErrorResponse
from src.infra.adapter.redis.redis_adapter import RedisAdapter
from src.api.controller.cache.dto.cache_output_dto import CacheOutputDto
from src.api.handler.exception_handler import http_exception_handler_manual
from fastapi import HTTPException


router = APIRouter()


@router.delete("/keys", response_model=CacheOutputDto, status_code=200, responses={
    400: {"model": ErrorResponse, "content": generate_validation_error_response()},
    422: {"model": ErrorResponse, "content": generate_unprocessable_entity_error_response()},
    200: {"model": CacheOutputDto}})
def delete_all_keys(
        *,
        service: RedisAdapter = Depends(RedisAdapter)):
    try:
        service.delete_all_key()
        return CacheOutputDto(status=True, message=["All cache was cleared"])
    except Exception as e:
        response_model = HTTPException(status_code=422, detail=e)
        return http_exception_handler_manual(exc=response_model)


@router.get("/keys", response_model=CacheOutputDto, status_code=200, responses={
    400: {"model": ErrorResponse, "content": generate_validation_error_response()},
    422: {"model": ErrorResponse, "content": generate_unprocessable_entity_error_response()},
    200: {"model": CacheOutputDto}})
def get_all_keys(
        *,
        service: RedisAdapter = Depends(RedisAdapter)):
    try:
        keys = service.get_all_key()
        keys = [key.decode('utf-8') for key in keys]
        return CacheOutputDto(status=True, message=keys)
    except Exception as e:
        response_model = HTTPException(status_code=422, detail=e)
        return http_exception_handler_manual(exc=response_model)
