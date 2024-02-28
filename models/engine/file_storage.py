#!/usr/bin/python3
"""
This is a file for the class FileStorage
"""
from models.base_model import BaseModel
import json
from os import path


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
        key = obj.__class__.__name__ + "." + obj.id
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
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                data = json.loads(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    cls = globals()[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
