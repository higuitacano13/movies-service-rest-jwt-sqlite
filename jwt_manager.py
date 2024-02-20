from jwt import encode, decode

SECRET_KEY = "my_secret_key"

def create_token(data: dict):
    token = encode(payload=data, key=SECRET_KEY, algorithm="HS256")
    print(f'Se ha generado el token: {token}')
    return token

def validate_token(token: str): 
    data = decode(token, SECRET_KEY, algorithms=["HS256"])
    return dict(data)
