#!/usr/bin/python3
"""
This is a file for the class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
