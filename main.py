import sys
import commands
arguments = sys.argv[1:]
cli = {
    "help": "This is a help message",
    "add": commands.add,
    "delete": commands.delete,
    "list": commands.list,
    "update": commands.update
}

cli[arguments[0]](*arguments[1:])