import CRUD
import UserSettings
import structure

class Search():

    def __init__(self, DB_Obj):
        self.CRUD = CRUD.CRUD(DB_Obj)

    def __execute__(self, Tables, Data, DB_Obj, Column="*") -> list:
        
        AllData = []
        
        for Table in Tables:            
            for TypeSearch in Data:
                for value in Data[TypeSearch]['value']:
                    sql = f"select {Column} from {Table} WHERE {Data[TypeSearch]['column']} = {value}"
                    data = self.CRUD.Read(sql)
                    
                    AllData.append(data)
                    
        return AllData        

    # RESTRUCTURE FUNCTION
    def key(self, DB):
        Tables = []
        Data = {"key":{"column":[], "value":[]}}

        iterations = int(input("how many key do you want add to search?\nR="))

        for i in range(iterations):
            key = int(input("What key are you looking for?\nR="))
            Data['key']['value'].append(key)

        column = input("Column where will the search be performed?\nR=")
        Data['key']['column'] = column

        table = input("Table where will the search be performed?\nR=")
        Tables.append(table)

        self.__execute__(Tables, Data, DB)


    def value(self, DB):
        print("Value")

    def patter(self, DB):   
        print("pattern")

    def jsonLoad(self, DB):

        GlobalUserData = UserSettings.Data()
        DataForSearch = GlobalUserData.GetUserData()
        
        if (DataForSearch['ShowData'] is None):
            result = self.__execute__(DataForSearch['tables'], DataForSearch['data'], DB)
        else:
            result = self.__execute__(DataForSearch['tables'], DataForSearch['data'], DB, DataForSearch['ShowData'])
        
        print("\n\nResultado\n")    
        print(result)
        print('\n')
