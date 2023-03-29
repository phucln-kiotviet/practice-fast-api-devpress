import email
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


class ArticleBase(BaseModel):
    title: str
    body: Optional[str] = None


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    author: EmailStr
    created_at: datetime
    updated_at: Optional[datetime]


    class Config:
        orm_mode = True # Make Pydantic read the data even if it is not a dict

class ArticleUpdate(BaseModel):
    title: Optional[str]
    body: Optional[str]

    class Config:
        orm_mode = True # Make Pydantic read the data even if it is not a dict




class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    articles: list[Article] = []

    class Config:
        orm_mode = True # Make Pydantic read the data even if it is not a dict