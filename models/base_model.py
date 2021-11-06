#!/usr/bin/python3
"""class Base Model"""
import uuid
import models
from datetime import datetime
class BaseModel:
    """class Base Model"""
    def __init__(self, *args, **kwargs):
        """ initialize Base Model """
	if not kwargs:
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = self.created_at
		models.storage.new(self)
	else:
