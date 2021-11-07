#!/usr/bin/python3
"""User Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class inherit from BaseModel"""
    state_id = ""
    name = ""
