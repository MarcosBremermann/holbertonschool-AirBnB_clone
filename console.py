#!/usr/bin/python3
"""
This module contains the Console and its methods
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""
    
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Exit the program."""
        return True
    
    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)."""
        print("\n")
        return True
    
    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
