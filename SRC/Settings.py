# Init: 09/23/2020
# Last Update: 04/19/2021
# Create by: DiegoDG-01

import os
import json

class Settings:

    # Inicializa la carga de los datos para la configuracion
    def __init__(self):
        
        # Obtenemos la ruta actual de donde se esta ejecutando el script
        FilePath = os.path.abspath(__file__)
        path, _ = os.path.split(FilePath)
        
        # Variables de control
        self.info_Database = None
        self.GeneralConfiguration = None
        self.info_Database_recents = None
        
        # En caso que exista algun error con la carga del archivo de configuracion mostramos
        # una mensaje al usuario y detenemos la ejecucion del script
        try:
            # Cargamos el archivo json para obtener la configuracion del script y
            # la informacion de la Base de datos
            with open(path + "/Data/Configuration_Script.json", "r") as file:
                GlobalData = json.load(file)
            
            # Asignacion de los datos guardados de la Base de datos
            if(GlobalData['Database']["actually"]['Status'] == 1):
                self.info_Database = GlobalData['Database']['actually']
            else:
                self.info_Database = False

            # Asignacion de los id de las bases de datos previamente abiertas con el script
            # Funcion en desarrollo
            if(GlobalData['Database']['recent']['ID'] is not None):
                self.info_Database_recents = GlobalData['Database']['recent']['ID']
            else:
                self.info_Database_recents = False
                
            # Variable que almacena la configuracion general del script
            self.GeneralConfiguration = GlobalData['General']
            
        except FileNotFoundError:
            # Manejo de execpciones
            # Muetra el error si el archivo de configuracion inicial no se encuentra.
            print("\x1b[1;31mCRITICAL ERROR, FILE FOR CONFIGURATION NOT FOUND")
            print("FILE REQUIRED: Configuration_Script.json")
            print("ERROR CODE: D0000\n")
            exit()
 
    # Obtencion de la informacion de la Base de datos actualmente cargada
    def GetInfoDataBase(self):
        """[summary]
        Funcion que retorma la informacion de la base de datos que se usuara durante la ejecucion del script

        Returns:
            [dict]: [Retorna un diccionario con la informacion de la BD (Host, nombre, usuario, etc.)]
        """
        return self.info_Database

    # Obtencion de las bases de datos anteriormente cargadas
    def GetDataBaseRecents(self):
        """[summary]
        Funcion que retorma el historial de las BD que han sido usadas por el script

        Returns:
            [dict]: [Retorna un diccionario con los ID correspondientes a las BD usadas por el script]
        
        Notes:
            Funcion en desarrollo.
        """
        return self.info_Database_recents

    def GetGeneralConfiguration(self):
        """[summary]
        Funcion que retorma la informacion de la configuracion principal del script

        Returns:
            [dict]: [Retorna un diccionario con la informacion.]
            
        Notes:
            Funcion en desarrollo.
        """
        return self.GeneralConfiguration

    # def GetUserData(self):
    #     return self.DataToSearch