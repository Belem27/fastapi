from fastapi import status, HTTPException, Depends, APIRouter
from app import models, utils
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas import UserCreate, User as UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    email_exist = db.query(models.User).filter(models.User.email == user.email).first()
    if email_exist:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"This email ({user.email}) already exist.")

    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(**dict(user))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}", response_model=UserResponse)
def get_user(id: int, db: Session =  Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"This post with id: {id} does not exist")
    
    return user