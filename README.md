#### TAREA - ENCUESTAS -

Para visualizar el README.md, favor de presionar _Ctrl+Shift+V_ aquí.

#### El APP ENCUESTAS contiene

- Seguridad : Autentificación de Usuarios; Rutas Protegidas y Registros de Usuarios
- Backend: python
- Frontend: Django
- Base de Datos: PostgreSQL vinculado a Docker Desktop
- Las Encuestas (surveys) y las Preguntas (Questions) se crean desde el admin de Django
- Una Encuesta puede tener varias preuntas, es decir, se pueden tener varias encuentas.
- Y una pregunta puede tener varias opciones y cada opción suma los VOTOS.
- El proyecto final se encuentra en: [Repositorio github Ohmicat GO](https://github.com/OhmiCat/djang-poll-tarea).

#### Descargar el proyecto ENCUESTAS:

---

1. Clonar el repositorio en github: git clone https://github.com/OhmiCat/djang-poll-tarea.gits
2. Crear un archivo venv en la raiz del proyecto (en caso ya va incluido, pero no debe ir):
   - py -3.10 -m venv venv
3. Activar el entorno virtual:
   - ./venv/Scripts/activate
4. Instalar las dependencias:
   - pip install -r requirements.txt
5. Ejecutar Postgres en docker desktop
6. Crear la base de datos
7. Ejecutar las migraciones:
   - python manage.py migrate
8. Crear un superusuario:
   - python manage.py createsuperuser
9. Ejecutar el servidor en el puerto 8002 (por default utilizan el 8000 ):
   - python manage.py runserver 8002
10. Para ejecutar el proyecto en el navegador puede utilizar cualquiera de las dos ligas:

- http://127.0.0.1:8002/
- http://localhost:8002/
