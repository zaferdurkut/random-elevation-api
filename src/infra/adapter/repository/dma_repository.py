from src.infra.adapter.repository.entity.dma_entity import DMAEntity
from src.infra.adapter.repository.base_repository import MySuperContextManager


class DmaRepository:
    def get_all(self):
        with MySuperContextManager() as db:
            dma_list = db.query(DMAEntity).filter(DMAEntity.status == True).all()

            return [dma for dma in dma_list]
