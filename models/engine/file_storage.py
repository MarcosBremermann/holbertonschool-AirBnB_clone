#!/usr/bin/python3
"""
This is a file for the class FileStorage
"""
import json
from os import path
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)

            for key, obj_data in data.items():
                class_name, obj_id = key.split('.')
                if class_name == 'User':
                    cls = User
                else:
                    cls = globals()[class_name]
                obj = cls(**obj_data)
                FileStorage.__objects[key] = obj
        else:
            pass
