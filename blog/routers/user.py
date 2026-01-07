from fastapi import APIRouter , Depends , HTTPException , status
from .. import schemas , models , database
from sqlalchemy.orm import Session 
from ..repository import user

get_db = database.get_db


router = APIRouter(
    prefix='/user',
    tags=["User"]
)

#now create a user

@router.post('/' , response_model = schemas.UserShow)
def create_user(request: schemas.UserCreate , db: Session = Depends(get_db)):
    return user.create(request , db)

@router.get('/{id}' , response_model = schemas.UserShow)
def get_user(id: int , db: Session = Depends(get_db)):
    return user.show(id , db)