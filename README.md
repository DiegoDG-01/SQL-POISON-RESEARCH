<p align="center">
  <a href="" rel="noopener">
 <img width=150px height=150px src="ReadmeData/IMG/rangoli.png" alt="Project logo"></a>
</p>

<h1 align="center">SQL POISON RESEARCH</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success)]()
[![Status](https://img.shields.io/badge/version-alpha-red)]()
[![Status](https://img.shields.io/badge/release-v0.0.1-informational)]()
[![Status](https://img.shields.io/badge/platform-OSX%20%7C%20Linux%20%7C%20Windows-lightgrey)]()
[![Status](https://img.shields.io/badge/chat-build-blueviolet)]()

</div>

---

<p align="center"> 
  An谩lisis, obtenci贸n y visualizaci贸n de informaci贸n almacenada en bases de datos SQL.
</p>

## 馃摑 Tabla de contenido

- [Acerca de](#about)
- [Comenzar](#getting_started)
- [Pruebas](#tests)
- [Notas](#notes)
- [Desarrolladoa con](#built_using)
- [Autor](#authors)
- [Agradecimientos](#acknowledgement)

## 馃 Acerca de <a name = "about"></a>

Mediante esta herramienta se pretende agilizar el an谩lisis y obtenci贸n de informaci贸n de bases de datos SQL a trav茅s de archivos previamente configurados,
logrando as铆 ahorrar tiempo, adem谩s de mostrar resultados de manera visual o generando reportes con dicha informaci贸n.


## 馃弫 Comenzar <a name = "getting_started"></a>

Estas instrucciones le proporcionar谩n una copia del proyecto en funcionamiento en su m谩quina local esto con fines de desarrollo y prueba. Consulte el apartado de [Comenzar](#getting_started) para obtener notas sobre c贸mo iniciar el proyecto.

El script actualmente este siendo desarrollado y probado en SGBD como MySQL & MariaDB.

### Pre-requisitos

Es necesario contar con un SGBD como:

```
MySQL

O

MariaDB
```

Adem谩s, es necesario contar con Python instalado en nuestro computador.

```
Python 3.8 o superior
```

### Instalaci贸n

Para su instalaci贸n y debido a el estado en que se encuentra actualmente no se requieren configuraciones complejas, ya que solo basta con descarga el proyecto.

- Descargamos el proyecto.

```
git clone https://github.com/DiegoDG-01/SQL-POISON-RESEARCH
```

- Colocamos la carpeta descargada en la ruta que mejor nos parezca.
- Con alg煤n editor abriremos primeramente el archivo "Configuration_Script.json" el cual se encuentra en la ruta "/SRC/Data/"
- Nos dirigimos al apartado de "actually" y colocaremos la informaci贸n de acuerdo con nuestras configuraciones.
  - Host.
  - Usuario.
  - Contrase帽a.
  - Nombre de la base de datos. (Esta ser谩 la base de datos sobre la cual trabajar谩 el script)
  - Stauts (Mantener el valor por default).

```
"actually":
  {
    "Host":"localhost", 
    "User":"TEST", 
    "Pass":"TEST", 
    "DB":"TEST", 
    "Charset":"utf8mb4",
    "Status":1
  }
```

- Por 煤ltimo, configuraremos el archivo "Data_Structure.json" el cual nos permitir谩 ejecutar consultar de manera automatizada, se encuentra en la ruta "/SRC/Data/"
(Actualmente es requerido ya que es la funci贸n que muestra el funcionamiento del script).

  - Estructura:
    - El primer nivel corresponde a la acci贸n a realizar sobre la base de datos consultar, insertar, actualizar o eliminar. (Deber谩 seguir un est谩ndar en los nombres como "search", "delete", "update" o "insert")
      ```
      {
        "search":
        {
            
        }
      }
      ```

    - El segundo nivel se especificar谩 la tabla ("tables" es la palabra clave) sobre la cual realizaremos las acciones, as铆 como los datos que buscaremos.
      ```
      {
        "search":
        {
            "tables":
            [
                "usuarios"
            ]
        }
      }
      ```

    - Data: en este caso es necesario especificar que tipo de b煤squeda se realizara, por claves(key), valores(value) o patrones(patterns) (Este ultimo aun no esta implementado).
      ```
      {
        "search":
        {
            "tables":
            [
                "usuarios"
            ],

            "data":
            {
                "key":
                {

                },

                "value":
                {
                                    
                },

                "ShowData":"Name, Age",
            }
        }
      }
      ```

    - Una vez especificado que tipo de b煤squeda realizara tenemos que detallar que valores buscaremos y opcionalmente que informaci贸n de columnas queremos obtener. (Si no se especifica columnas con "ShowData" retornara todas las disponibles)

      ```
      {
        "search":
        {
            "tables":
            [
                "usuarios"
            ],

            "data":
            {
                "key":
                {
                  "column":"ID",
                  "value":[1,2,3,4]
                },
                
                "value":
                {
                                    
                },

                "ShowData":"Name, Age",
            }
        }
      }
      ```

Esa es la estructura interna necesaria para hacer funcionar el script de manera automatizada, el archivo puede ser modificado para variar el tipo de consultas y datos a obtener, pero siempre manteniendo dicha estructura.


## 馃敡 Pruebas <a name = "tests"></a>

Con el fin de facilitar el entendimiento del proyecto en la ruta "/Other/SQL/" encontraras un base de datos de pruebas con la cual podr谩s ejecutar el script sin ning煤n problema, basta con importarla en tu SGBD.

- Dir铆gete a la ruta "SRC" del proyecto y ejecuta el comando:

  ```
  python3 main.py
  ```

- Seleccionamos la opci贸n #2.

  <img width=400px height=400px src="ReadmeData/IMG/welcome.png" alt="Project logo">

  **Nota:** Actualmente solo la funci贸n #2 (search) esta operativa.

- Elegimos la opci贸n 4. (Cargara y ejecutara el archivo "Data_Structure.json")

  <img width=350px height=200px src="ReadmeData/IMG/submenu.png" alt="Project logo">

- Finalmente mostrara el resultado que obtuvo en la consulta de los datos y finalizara el script.

  <img width=400px height=100px src="ReadmeData/IMG/result.png" alt="Project logo">

## 馃棐 Notas <a name="notes"></a>

Actualmente esta en desarrollo la fase alpha del proyecto, por lo cual su funcionalidad es limitada y existe un gran porcentaje de fallo,
con lo cual se recomienda trabajar con cuidado y no hacer uso de bases de datos con informaci贸n importante para usted.


## 鉀忥笍 Construido con <a name = "built_using"></a>

- [Python](https://www.python.org) - Lenguaje de programaci贸n

## 馃懢 Caracteristicas futuras <a name = "built_using"></a>

- An谩lisis autom谩tico de la estructura interna de la Base de datos.
- Uso de inteligencia artificial que agilice en mayor medida el an谩lisis y tratamiento de la informaci贸n.


## 鉁嶏笍 Autor <a name = "authors"></a>

- [@DiegoDG-01](https://github.com/DiegoDG-01) - Idea & trabajo inicial


## 馃帀 Agradecimientos <a name = "acknowledgement"></a>

- Logo by Good Ware (FlatIcon)
