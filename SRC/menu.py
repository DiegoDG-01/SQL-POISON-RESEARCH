import Settings
import DB_Connect
from time import sleep

# DELETE
import subprocess
# DELETE

# Importar todos los modulos de las funciones
import Functions.Search
import Functions.Database
# import Functions.Analize
# import Functions.Delete
# import Functions.Rebuild

class menu:

    # 1.- AL crear la clase se intancia todos los modulos con sus funciones y son gaurdados en
    #     un diccionario para se ejecucion posteriormente.

    def __init__(self, DB_Data):
        """[summary]
        AL crear la clase se intancia todos los modulos con sus funciones y son gaurdados en
        un diccionario para su posterior ejecucion.

        Args:
            DB_Data ([dict]): [Contiene un diccionario con la informacion de la BD (Host, nombre, usuario, etc.)]
        """

        # Creacion de instancia y configuracion de la Base de datos
        self.DB = DB_Connect.DB(DB_Data)

        DB = Functions.Database.DB()
        # search = Functions.Search.Search()
        # search = Functions.Search.Search()
        # search = Functions.Search.Search()
        # search = Functions.Search.Search()
        search = Functions.Search.Search(self.DB)


        self.ListAction = {1:{1:DB.key, 2:DB.value},
                           2:{1:search.key, 2:search.value, 3:search.patter, 4:search.jsonLoad}
        }


    # Muestra el logo del script así como el menu principal
    def ShowMenu(self):

        """[summary]
        """
        LogoASCII = ("\n>======>         >>       >====>     ", ">=>    >=>      >>=>      >=>   >=>  ", ">=>    >=>     >> >=>     >=>    >=> ", ">======>      >=>  >=>    >=>    >=> ", ">=>          >=====>>=>   >=>    >=> ", ">=>         >=>      >=>  >=>   >=>  ", ">=>        >=>        >=> >====>\n", "     Development by DiegoDG-01\n")

        self.ListFunction = {1:{0:'1.- DataBase', 1:'\t1.- Load DB Local', 2:'\t2.- Load DB Remote', 3:'\t2.- Select recent\n'},
                             2:{0:'2.- Search',1:'\t1.- Key (ID)', 2:'\t2.- value', 3:'\t3.- pattern', 4:'\t4.- load json\n'},
                             3:{0:'3.- Analize',1:'\t1.- Duplicates', 2:'\t2.- patterns', 3:'\t3.- load json\n'},
                             4:{0:'4.- Delete', 1:'\t1.- Clean pattern', 2:'\t2.- Load json', 3:'\t3.- All (Warning)\n'},
                             5:{0:'5.- Rebuild database (EXPERIMENTAL)', 1:'\t1.- Initialize\n'},
                             6:{0:'6.- Untitled special menu', 1:'\t1.- In development\n'}}

        for i in LogoASCII:
            print("\x1b[1;32m"+i)

        for i in self.ListFunction:
            print(self.ListFunction[i][0])

    # Permite la ejecucion de las funciones disponibles.
    def SelectFunction(self):

        """[summary]

        Returns:
            [type]: [description]
        """

        try:
            Menu = int(input("\n\x1b[1;33mWhat submenu do you want view?\nR= "))

            # DELETE AND CREATE CLASS IN UTILITIES
            subprocess.call(['clear'])
            # DELETE AND CREATE CLASS IN UTILITIES

            if(Menu in self.ListFunction):

                print("Current Menu:\n"+self.ListFunction[Menu][0])

                for a in range(1, len(self.ListFunction[Menu])):
                    print(self.ListFunction[Menu][a])

                SubMenu = int(input("\n\x1b[1;33mWhat function do you want to run?\nR= "))

                if(SubMenu in self.ListFunction[Menu]):

                    resultFunction = self.ListAction[Menu][SubMenu](self.DB)
                    # print(resultFunction)
                else:
                    return False
            else:

                return False
        except ValueError :
            print("\n\n\x1b[1;31mONLY NUMBERS\n")
            sleep(0.5)