# Sistema de Detección de Emociones

Descripción General del proyecto

software de aplicación que permita detectar posibles problemas emocionales en jóvenes universitarios de 19 a 25 años, a través del análisis de un texto en específico redactado con las propias palabras de los chicos.
La idea surge a partir de la detección de problemas emocionales en los jóvenes del centro de trabajo en donde laboro actualmente (una universidad privada), desafortunadamente muchas veces la detección de estos problemas se da ya cuando el chico presenta problemas de comportamiento, escolares y en casos más extremos en atentar contra su vida.


# Problemática

Los jóvenes de 19 a 25 años de una universidad privada en su mayoría no cuentan con un diagnóstico oportuno en temas de trastornos emocionales, lo que provoca problemas de comportamiento, en el rendimiento escolar y en su vida diaria.


#Requisitos

-Python 3.x

-Django 4.x o superior

-MariaDB 10.x o superior

-pip / virtualenv

-Git

#Instalación

Clona el repositorio:

git clone https://github.com/usuario/sistema-deteccion-emociones.git
cd sistema-deteccion-emociones


Crea y activa un entorno virtual:

python3 -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows


Instala las dependencias:

pip install -r requirements.txt

-Configuración


Este proyecto incluye un archivo de respaldo generado con mysqldump llamado:

database/respaldo.sql

1. Crear la base de datos:
CREATE DATABASE Proyecto_emociones
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

2. Importar el dump:
mysql -u tu_usuario -p Proyecto_emociones < database/respaldo.sql

3. Aplicar migraciones adicionales:
python manage.py migrate

#Ejecutar el Proyecto

Inicia el servidor local:

python manage.py runserver


El proyecto quedará disponible en:

http://127.0.0.1:8000/registrar_alumno ó estilos_aprendizaje/1

 
