from fastapi import APIRouter
from jwt_manager import create_token
from fastapi.responses import JSONResponse
from dto.user_dto import User

user_router = APIRouter()

# ================== Autenticación ====================== #

@user_router.post('/login', tags=['Authentication'], status_code=200)
def login(user: User):
    try:
        if user.email == "jhiguitac@gmail.com" and user.password == "pass2024":
            token = create_token(dict(user))
        return JSONResponse(status_code=200, content={'Token': token})
    except Exception as error:
        raise Exception(error)