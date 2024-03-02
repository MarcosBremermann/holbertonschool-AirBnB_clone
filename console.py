#!/usr/bin/python3
"""Console module"""

import cmd
import sys
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel", "User"]: # add more classes if necessary
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]: # add more classes if necessary
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if obj_key in all_objects:
                print(all_objects[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]: # add more classes if necessary
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if obj_key in all_objects:
                del all_objects[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        all_objects = storage.all()
        if not arg:
            print([str(obj) for obj in all_objects.values()])
        elif args[0] not in ["BaseModel", "User"]: # add more classes if necessary
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in all_objects.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]: # add more classes if necessary
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if obj_key in all_objects:
                obj = all_objects[obj_key]
                setattr(obj, args[2], args[3])
                obj.save()
            else:
                print("** no instance found **")

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
