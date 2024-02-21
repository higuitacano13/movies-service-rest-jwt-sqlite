from fastapi import APIRouter, HTTPException, Depends, Request
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schema.user_schema import User
from config.database import Session
from services.user_service import UserService
from middlewares.jwt_bearer import JWTBearer

user_router = APIRouter()

# ================== Autenticación ====================== #


@user_router.post('/login', tags=['Authentication'], status_code=200)
def login(user: User):
    try:
        db = Session()
        result = UserService(db).get_user_by_email(user.email)
        if not result:
            raise HTTPException(status_code=404, detail={"Message": 'User not found'})
        if result.email == user.email and result.password == user.password:
            token = create_token(dict(user))
        return JSONResponse(status_code=200, content={'Token': token})
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
    
@user_router.post('/create_user', tags=['Authentication'], status_code=201, dependencies=[Depends(JWTBearer())])
def create_user(user: User):
    try:
        db = Session()
        UserService(db).create_user(user)
        return JSONResponse(status_code=201, content={'Message': "Se ha guardado el registro de usuario exitosamente"})
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))