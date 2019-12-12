# Comandos y explicaciones:

Nota: De momento por comodidad el servicio incluye por defecto 4 tipos de vehículos y un superusuario (correos=user@user.user, contraseña=user) con el que poder acceder a la página de administración '/admin'

## Instalar/Lanzar
- El sistema está implementado como docker-compose, basta lanzar ```docker-compose up``` (por comodidad se proporciona el script ```rundocker``` que ejecuta exactamente eso).
- Si el servicio ha sido lanzado correctamente se deberá mostrar como último log en la consola la siguiente información:
```
web_1  | Starting development server at http://0.0.0.0:80/
web_1  | Quit the server with CONTROL-C.
```

## Iniciar
- Si el servidor ha sido lanzado correctamente, basta dirigirse a la dirección web http://localhost para usar el servicio.

### Administración
- Para añadir viajes al usuario registrado (lo que la 'api' de la aplicación proporciona) se debe ir a '/api' una vez se ha iniciado sesión, rellenar los datos del viaje y aceptar.
- La página de administración accesible desde '/admin' para usuarios administradores 
(superusuarios) permite de manera visual crear, modificar y/o borrar los datos del sistema, lo que incluye usuarios, tipos de vehículos, noticias y viajes guardados. Desde esta página se puede además añadir otro superusuario.