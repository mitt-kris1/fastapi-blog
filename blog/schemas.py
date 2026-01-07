from pydantic import BaseModel
from typing import List , Optional


class BlogBase(BaseModel):
    title : str
    body : str

class Blog(BlogBase):
    class Config():
        orm_mode = True

#if we want to show only eg- title or body not id then we set a response model and then put this showblog as a parameter in @app.get('/blogs/{id}')

class UserCreate(BaseModel):
    name: str
    email : str
    password :str

class UserShow(BaseModel):
    name: str
    email : str
    blogs : List[Blog]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title : str
    body : str
    creator : UserShow
    class Config():
        orm_mode = True

class login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type : str

class TokenData(BaseModel):
    email : Optional[str] = None
