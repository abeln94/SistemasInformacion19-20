# Comandos y explicaciones:

Nota: De momento por comodidad el servicio incluye por defecto 4 tipos de vehículos y un superusuario (nombre=user, contraseña=user) con el que poder acceder a la página de administración '/admin'

## Instalar/Lanzar
- El sistema está implementado como docker-compose, basta lanzar ```docker-compose up``` (por comodidad se proporciona el script ```rundocker``` que ejecuta exactamente eso).
- Si el servicio ha sido lanzado correctamente se deberá mostrar como último log en la consola la siguiente información:
```
web_1  | Starting development server at http://0.0.0.0:8000/
web_1  | Quit the server with CONTROL-C.
```

## Iniciar
- Si el servidor ha sido lanzado correctamente, basta dirigirse a la dirección web http://localhost:8000 para usar el servicio.

### Añadir superusuario
- En caso de querer añadir otro superusuario de momento se debe hacer por comando ```python migrate.py createsuperuser``` y meter los datos segun va preguntando
