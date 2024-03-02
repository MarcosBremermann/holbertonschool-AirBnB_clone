#!/usr/bin/python3
"""
This module contains the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel
    """
    state_id = ""
    name = ""