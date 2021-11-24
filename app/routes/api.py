from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from ..schemas import BaseSchool, School
from ..database import get_db
from ..controllers import school_api_controller

router = APIRouter()


@cbv(router)
class SchoolRoute:
    session: Session = Depends(get_db)

    @router.get("/api/v1/school")
    def list(self):
        schoolList = school_api_controller.getAll(self.session)

        return schoolList
