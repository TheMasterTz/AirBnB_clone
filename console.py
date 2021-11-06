#!/usr/bin/python3
import cmd, json, shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    	"""Interprete de comandos"""
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
        """Quit command to exit the program\n"""
       		 return True

    	def do_EOF(self, *args):
        """Quit command to exit the program\n"""
        	return True

    	def emptyline(self):
        """baseline"""
        	pass

    	def do_create(self, arg):
        """Create new instance of class\n"""
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
        """Show Class Instance by ID #"""
        	args = arg.split(' ')

        	if len(args[0]) == 0:
            		print("** class name missing **")
        	elif args[0] not in self.classes:
            		print("** class doesn't exist **")
        	elif len(args) == 1:
            		print("** instance id missing **")

       	else:
            string = "[{}] ({})".format(args[0], args[1])
            valida = 0
            for ins in self.ins:
                if string in ins.__str__():
                    print(ins)
                    valida = 1
            if valida == 0:
                print("** no instance found **")

    	def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.\n"""
        	args = arg.split(" ")
        	flag = 0

        	if len(args[0]) == 0:
            		print("** class name missing **")
        	elif args[0] not in self.classes:
            		print("** class doesn't exist **")
        	elif len(args) == 1:
            		print("** instance id missing **")

        	else:
            		idn = "[{}] ({})".format(args[0], args[1])
            		for ins in self.ins:
                		if idn in ins.__str__():
                    		self.ins.remove(ins)
                    		flag = 1
            		if flag == 0:
                		print("** no instance found **")
            	else:
                	with open(HBNBCommand.file_path, 'r', encoding='utf-8') as f:
                    	file_json = json.loads(f.read())

                	del file_json['{}.{}'.format(args[0], args[1])]

                	with open(HBNBCommand.file_path, 'w', encoding='utf-8') as f:
                    	json.dump(file_json, f)

    	def do_all(self, arg):
        """function all\n"""
        	args = arg.split(" ")
        	if len(args[0]) == 0:
            		for i in self.ins:
                		print(i.__str__())
        	elif args[0] not in self.classes:
            		print("** class doesn't exist **")
        	else:
            		for x in self.ins:
                		if args[0] in x.__str__():
                    			print(x)
	def do_update(self, arg):
        """update instance"""
        	if arg == "":
            		print("** class name missing **")
        	args = shlex.split(arg)

        	if args[0] not in self.classes:
            		print("** class doesn't exist **")

        	elif len(args) == 1:
            		print("** instance id missing **")

        	else:
            		flag = 0
            		idn = "[{}] ({})".format(args[0], args[1])
            		for ins in self.ins:
                		if idn in ins.__str__():
                    			flag = 1
            		if flag == 0:
                		print("** no instance found **")
            		elif len(args) == 2:
                		print("** attribute name missing **")
            		elif len(args) == 3:
                		print("** value missing **")
            		else:
                		idn = "[{}] ({})".format(args[0], args[1])
                		for ins in self.ins:
                    			if idn in ins.__str__():
                        			try:
                            				value = int(args[3])
                        			except ValueError:
                            				try:
                                				value = float(args[3])
                            				except ValueError:
                                				value = args[3]
                        			setattr(ins, args[2], value)
                        			ins.save()



if __name__ == "__main__":
    	interprete = HBNBCommand()
    	interprete.cmdloop()
