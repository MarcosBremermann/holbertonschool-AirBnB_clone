#!/usr/bin/python3
#!/usr/bin/python3
"""
This module contains the Console and its methods
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name, instance_id = args[0], args[1] if len(args) > 1 else None
        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        if not instance_id:
            print("** instance id missing **")
            return
        instance = None  # Get the instance from your storage system
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    # Implement other commands similarly

if __name__ == '__main__':
    HBNBCommand().cmdloop()