import menu
import Settings


"""
[summary]

Archivo que inicializa el script, es el encargado de validar que todo la configuracion
y archivos esten correctamente configurados.

"""

# Valida que el archivo ejecutado sea el archivo principal
if( __name__ == '__main__'):
    
    # Inicializa un objeto que precarga la configuracion inicial
    initialize = Settings.Settings()
    
    # Obtenemos los datos correspondientes a la configuracion inicial y de base de datos
    DataBaseMainInfo = initialize.GetInfoDataBase()
    
    # Funciones en desarrollo
    """
    DataBaseRecents = initialize.GetDataBaseRecents()
    MainConfiguration = initialize.GetGeneralConfiguration()
    """
    
    # Inicilizamos el modulo de menu y le pasamos como parametro la configuracion de la Base de datos
    menu = menu.menu(DataBaseMainInfo)
    
    # Evita mostrar errores cuando el usuario cancela de manera automatica la ejecucion del script
    try:
        
        # Creamo un bucle para mantener el script siempre funcionando
        while(True):
            # Mostramos el menu inicial
            menu.ShowMenu()
            # Habilitamos la obtencion de dato del usuario
            menu.SelectFunction()
            # Forzamos la detencion del script (TEMPORAL)
            break
    except KeyboardInterrupt:
        print("\n\n\x1b[1;31mSTOP RUNNING SCRIPT!!!!\n")