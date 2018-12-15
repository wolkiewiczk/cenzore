from abc import ABC
import json


class DictionaryLoader(ABC):

    def __init__(self, **kwargs):

        if kwargs is None:
            raise ValueError("There need to be at least one str argument passed")

        self.dictionaries = {}
        for key, arg in kwargs.items():

            if arg.split(".", maxsplit=1)[1] == "txt":
                # loading txt files

                if type(arg) not in [str]:
                    print("Loading of the file failed - path needs to be str type")
                    continue

                try:
                    with open(arg, "r") as file:
                        self.dictionaries[key] = file.readlines()
                    self.dictionaries[key] = [x.strip() for x in self.dictionaries[key]]
                except IOError:
                    print("Loading of the " + arg + " file failed - couldn't find path")

            elif arg.split(".", maxsplit=1)[1] == "json":
                # loading json files
                try:
                    with open(arg, "r") as file:
                        self.dictionaries[key] = json.load(file)
                except IOError:
                    print("Loading of the " + arg + " file failed - couldn't find path")
            else:
                print("Loading of the" + arg + "file failed - unresolved extension")
