# Tp.Django
Repositorio del código del proyecto correspondiente al Grupo 13 del curso 
Django, Codo a Codo, 2do Cuatrimestre de 2023
Integrantes:
  Gil, Leandro,
  Avila, Esteban
  Jouan, Juan
  Savia, Martin
  Ricardini, Fabrizio Fabian
Objeto del projecto: Desarrollo de un sitio web de e-commerce

Pasos para levantar proyecto:
- usuario/pw para usar psql en grupo13/settings.py:  
  postgres/Fortin23
- usando aplicacion psql:
  CREATE DATABASE tpdjango;
  \q
- crear venv
  python -m venv c:\proyectos\django_envs\cac2ctig
- Activar environment y configurarlo
  c:\proyectos\django_envs\cac2ctig\Scripts\activate
  cd C:\proyectos\Tp.Django
  pip install -r requirements.txt
- Crear superusuario de python
  python manage.py createsuperuser
- Correr migraciones
  python manage.py makemigrations
  python manage.py migrate
- Correr fixtures para cargar la base de datos
  python manage.py loaddata categorias
  python manage.py loaddata stock_items
  python manage.py loaddata destacados

Puntos pedidos para proyecto:
- Modelos: 
    Stock_item
    Categoria
- Relación muchos a muchos:
    entre Stock_item y Categoria definida en Stock_item 
    mediante clase Destacado_por_categoria
- URL parametrizados. Ejemplos de uso:
	http://127.0.0.1:8000/pagina_principal/destacado_y_relac_x_bd/1/
	http://127.0.0.1:8000/pagina_principal/destacado_y_relac_x_bd/2/
	http://127.0.0.1:8000/pagina_principal/destacado_y_relac_x_bd/Auriculares/
	http://127.0.0.1:8000/pagina_principal/destacado_y_relac_x_bd/Videojuegos/
- Administración
  http://127.0.0.1:8000/admin/
  