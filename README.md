Descripción del Proyecto
Este proyecto implementa un sistema básico de gestión de usuarios. El backend ofrece una API REST para consultar y crear usuarios, documentada con Swagger para mayor claridad. El frontend (opcional) es una aplicación React que permite interactuar con la API para visualizar y gestionar datos de usuarios.

Tecnologías Utilizadas
Backend:
Python 3.8+
Flask
Flasgger (Swagger/OpenAPI)

Interfaz de Swagger
La API está documentada con Swagger, que ofrece una interfaz interactiva para explorar y probar los endpoints. Accede a ella en:
http://3.129.44.232:5000/docs/usuarios#/

Backend (API Flask)
Clona el repositorio:

git clone <url-del-repositorio>
cd <carpeta-del-repositorio>

Instala las dependencias: Asegúrate de tener Python instalado y ejecuta:

pip install -r requirements.txt
El archivo requirements.txt debe incluir:

flask
flasgger

Ejecuta el servidor Flask:

python app.py
La API estará disponible en (http://3.129.44.232:5000/docs/usuarios#/)
Accede a la interfaz de Swagger: Abre (http://3.129.44.232:5000/docs/usuarios/apidocs/ en tu navegador.
