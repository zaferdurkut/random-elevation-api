import datetime
import uuid

from geoalchemy2 import Geometry
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID

from src.infra.config.repository_config import Base


class DMAEntity(Base):
    __tablename__ = 'dma'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    short_name = Column(String)
    time_zone = Column(String)
    geom = Column(Geometry(geometry_type='POLYGON', srid=4326))
    status = Column(Boolean, unique=False, default=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    created_at = Column(DateTime)
