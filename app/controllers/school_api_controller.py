from typing import List
from sqlalchemy.orm import Session
from ..models.school import School as SchoolInfo
from ..schemas import School as SchoolSchema


def getAll(session: Session):
    return session.query(SchoolInfo).all()

