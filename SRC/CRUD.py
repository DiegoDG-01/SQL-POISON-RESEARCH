class CRUD:

    def __init__(self, DB_Object):
        self.DB_Object = DB_Object

    def Create(self):
        print("CREATE")

    def Update(self):
        print("Update")

    def Read(self,Query):
        result = self.DB_Object.__commit__(Query)

        result = self.DB_Object.con.fetchall()

        return result
        # print("Read")

    def Delete(self):
        print("Delete")