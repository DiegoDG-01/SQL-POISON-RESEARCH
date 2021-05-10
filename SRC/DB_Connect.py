import pymysql
from time import sleep
from pymysql.constants import ER

class DB:

    ErrCodesMysql = {
        ER.BAD_DB_ERROR: "Unknown your database, check Configuration_Script.json file",
        ER.ACCESS_DENIED_ERROR: "Access denied, check access credentials in Configuration_Script.json file"
    }

    def __init__(self, Data = None):

        if(Data is not None):
            self.Host = Data['Host']
            self.User = Data['User']
            self.Password = Data['Pass']
            self.DB = Data['DB']
            self.Charset = Data['Charset']

            self.__connect__()
        else:
            print("\x1b[1;31mINFO TO CONNECT DATABASE IS EMPTY")
            print("\x1b[1;31mERROR CODE: DB000")
            exit()   
        
    def __connect__(self) -> None:

        try:
            self.connection = pymysql.connect(host=self.Host, user=self.User, password=self.Password, db=self.DB, charset=self.Charset, cursorclass=pymysql.cursors.DictCursor)
            self.con = self.connection.cursor()
        except pymysql.err.MySQLError as err:
            code, args = err.args

            print("\x1b[1;31mERROR CODE: DB001")
            print(self.ErrCodesMysql.get(code, args)) 
            exit()      

    def __disconnect__(self) -> bool:
        print("Conexion terminada")

    def __check__(self) -> bool:
        print("TODO BIEN :b")

    def __commit__(self, sql) -> bool:
        result = self.con.execute(sql)
        return result