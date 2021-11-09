#!/usr/bin/python3
"""file storage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """Returns dictionary"""
        return self.__objects

    def new(self, obj):
        """Assigns objects"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Writes an object to a file"""
        dic = {}
        for key, value in self.__objects.items():
            dic[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(dic, indent=4))

    def reload(self):
        """Retrieves objects from a file"""
        new = {}
        try:
            with open(self.__file_path, "r") as f:
                new = json.loads(f.read())

                for key, value in new.items():
                    self.__objects[key] = self.classes[
                        value["__class__"]](**value)
        except FileNotFoundError:
            pass
