#!/usr/bin/python3
"""
command interpreter
"""
import cmd
import json
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Interpreted commands"""
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }
    file_path = "file.json"
    ins = []
    prompt = "(hbnb) "

    def do_quit(self, *args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, *args):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Empty Line does not execute previous command
        """
        pass

    def do_create(self, arg):
        """Create new instance of class
        """
        args = arg.split(' ')

        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")

        else:
            var = self.classes[args[0]]()
            print(var.id)
            self.ins.append(var)
            var.save()

    def do_show(self, arg):
        """Show Class Instance by ID #
        """
        args = arg.split(' ')

        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")

        else:
            dicIns = models.storage.all()
            key = args[0] + '.' + args[1]
            if key in dicIns:
                print(dicIns[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        """
        args = arg.split(" ")

        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")

        else:
            dicIns = models.storage.all()
            key = args[0] + '.' + args[1]
            if key in dicIns:
                del dicIns[key]
                flag = 1
            if flag == 0:
                print("** no instance found **")
            else:
                with open(HBNBCommand.file_path, 'r', encoding='utf-8') as f:
                    file_json = json.loads(f.read())

                del file_json['{}.{}'.format(args[0], args[1])]

                with open(HBNBCommand.file_path, 'w', encoding='utf-8') as f:
                    json.dump(file_json, f, indent=4)

    def do_all(self, arg):
        """Prints all string representation of all instances based or
            not on the class name.
        """
        args = arg.split(" ")
        dicIns = models.storage.all()

        if len(args[0]) == 0:
            for key in dicIns:
                self.ins.append(dicIns[key].__str__())
            print(self.ins.__str__())
            self.ins = []

        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key in dicIns:
                if arg in key:
                    self.ins.append(dicIns[key].__str__())
            print(self.ins.__str__())
            self.ins = []

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
            or updating attribute (save the change into the JSON file)
        """
        if arg == "":
            print("** class name missing **")
            return
        args = shlex.split(arg)

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
                print("** attribute name missing **")
                return
        elif len(args) == 3:
            print("** value missing **")
            return

        else:
            dicIns = models.storage.all()
            key = args[0] + '.' + args[1]
            if key not in dicIns:
                print("** no instance found **")
                return
            else:
                if key in dicIns:
                    insAC = dicIns.get(key)
                    try:
                        value = int(args[3])
                    except ValueError:
                        try:
                            value = float(args[3])
                        except ValueError:
                            value = args[3]
                    setattr(insAC, args[2], value)
                    models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
