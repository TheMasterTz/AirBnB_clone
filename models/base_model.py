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
            		for arg, val in kwargs.items():
                		if arg in ('created_at', 'updated_at'):
                    		val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                		if arg != '__class__':
                    			setattr(self, arg, val)

	def __str__(self):
        """string representation"""
        	return "[{0}] ({1}) {2}".format(
            	self.__class__.__name__, self.id, self.__dict__)

	def save(self):
        """save method"""
        	self.updated_at = datetime.now()
        	models.storage.save()
