import os

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from src.api.controller.common.dto.heartbeat_output_dto import HeartbeatOutputDto
from src.api.controller.common.dto.service_check_output_dto import ServiceCheckOutputDto
from src.api.controller.common.dto.token_output_dto import TokenOutputModel
from src.infra.adapter.redis.redis_adapter import RedisAdapter
from src.infra.adapter.repository.base_repository import MySuperContextManager

router = APIRouter()


@router.get("/heartbeat", response_model=HeartbeatOutputDto, status_code=200)
def heartbeat():
    return HeartbeatOutputDto.to_model(os.environ['HOSTNAME'])


@router.get("/service-check", response_model=ServiceCheckOutputDto, status_code=200)
def service_check():
    return ServiceCheckOutputDto.to_model(
        db_connection_check=MySuperContextManager().service_check(),
        redis_cache_check=RedisAdapter.service_check()
    )


@router.post("/token", response_model=TokenOutputModel, status_code=200)
def token(form_data: OAuth2PasswordRequestForm = Depends()):

    if form_data.client_id is None or form_data.client_secret is None:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="client_id or client_secret is missing",
            headers={"WWW-Authenticate": "Bearer"},
        )

    data = {}
    # TODO: connect to auth service, now only test
    data["access_token"] = "test"

    if 'access_token' in data.keys():
        token = data['access_token']
    else:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="access_token is not available",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return TokenOutputModel.to_model(access_token=token, token_type="bearer")
