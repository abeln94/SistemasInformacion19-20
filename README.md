### Añadir superusuario (de momento tiramos con esos)
- ```python migrate.py createsuperuser``` y meter datos segun va diciendo

### Rehacer la base de datos (si se cambian los modelos y no nos importa perder los datos)
- Borrar los ficheros dentro de las carpetas 'migration'
- Borrar db.sqlite3 (o equivalente)
- ```python manage.py makemigrations```
- ```python manage.py migrate```