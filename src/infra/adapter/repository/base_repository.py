from src.infra.config.repository_config import SessionLocal
from sqlalchemy import text, and_
import logging


class MySuperContextManager:
    def __init__(self):
        # logging.basicConfig()
        # logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()

    def service_check(self) -> bool:
        try:
            client = self.db
            result = int(client.execute(text("select 1 as result")).first().result)
            if result == 1:
                return True
        except Exception as e:
            print(e)
            return False
        return False
