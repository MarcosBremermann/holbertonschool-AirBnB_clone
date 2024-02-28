#!/usr/bin/python3
"""
This is a file for the class BaseModel
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    This is the base model class that all other
    classes inherit from
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        class_name =  self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance:
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = type(self).__name__
        dict_copy["created_at"] = self.updated_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
