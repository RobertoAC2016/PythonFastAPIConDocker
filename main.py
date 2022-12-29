#   Voy a crear un app de python de tipo web con un EP de tipo GET
#   Usare la libreria fast API y validaremos el acceso
#   Finalmente montaremos la APP web en un contenedor docker y validaremos el acceso <--
#   las librerias a utilizar es fastapi y uvicorn, hay q generar el archivo de requirement.txt para la referencia
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    #aqui voy a regresar un json
    return {"message":"Hola mundo!"}
#No hace reload, a la linea de comandos agregaremos --reaload para recargar al modificar codigo

# ya esta corriendo el servicio de docker, deben isntalar docker desktop
# vamos a crear la imagen => docker build -t mi_app .
# falto crear el archivo de dockerfile
# ahora vamos a crear el contenedor y ejecutarlo, si lo detenemos ya no se usara la misma isntruccion de docker run
# veamos q instruccion usar