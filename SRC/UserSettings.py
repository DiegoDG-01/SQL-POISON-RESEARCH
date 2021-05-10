import json
from os.path import abspath, split, isfile

class Data:

    def __init__(self):

        FilePath = abspath(__file__)
        path, _ = split(FilePath)

        self.DataToExecute = {"data":[], "tables":[]}

        # Verifica que exista el archivo de configuracion creado por el usuario
        # CHANGE LINE AFTER TO DEBUGGER
        # if(path.isfile("JSON/data.json")):
        if(isfile(path + "/Data/Data_Structure.json")):
            
            # CHANGE LINE AFTER TO DEBUGGER
            # with open("JSON/data.json", "r") as file:
            with open(path + "/Data/Data_Structure.json", "r") as file:
                JsonUserData = json.load(file)

                # BUG

                if(JsonUserData.get("search")):
                    self.DataToExecute['data'] = JsonUserData['search']['data']
                    self.DataToExecute['tables'] = JsonUserData['search']['tables']
                    
                    if("ShowData" in JsonUserData['search']):
                        self.DataToExecute['ShowData'] = JsonUserData['search']['ShowData']
                    else:
                        self.DataToExecute['ShowData'] = None
                        
                else:
                    self.DataToExecute = False
        else:
            print("USER CONFIGURATION FILE NOT FOUND")
            print("INTERNAL ERROR\nERROR CODE: D0D00")
            self.DataToSearch = False

    def GetUserData(self):
        return self.DataToExecute