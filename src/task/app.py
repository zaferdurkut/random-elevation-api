from celery import Celery

from src.core.exception.application_exception import ApplicationException
from src.task.config.celery_config import *

celery_app = Celery("worker",
                    backend="redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_BACKEND_DB}".format(
                        REDIS_HOST=str(REDIS_HOST),
                        REDIS_PORT=str(REDIS_PORT),
                        REDIS_CELERY_BACKEND_DB=str(REDIS_CELERY_BACKEND_DB)),

                    broker="redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_BROKER_DB}".format(
                        REDIS_HOST=str(REDIS_HOST),
                        REDIS_PORT=str(REDIS_PORT),
                        REDIS_CELERY_BROKER_DB=str(REDIS_CELERY_BROKER_DB)),

                    )


@celery_app.task(
    bind=True,
    autoretry_for=(ApplicationException,),
    retry_kwargs={"max_retries": 1000000000000},
    retry_backoff=True,
    retry_backoff_max=10,
    timelimit=600
)
def chordfinisher(self):
    return "OK"
