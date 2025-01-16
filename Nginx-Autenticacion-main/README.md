## Comprueba desde tu máquina física/anfitrión que puedes acceder a `http://nombre-sitio-web` y que se te solicita autenticación.
![alt text](img/1.png)
##  Comprueba que si decides cancelar la autenticación, se te negará el acceso al sitio con un error. ¿Qué error es?
![alt text](img/2.png)

# T.1
## Intenta entrar primero con un usuario erróneo
![alt text](img/3.png)

Logs:
- `access.log`
Usuario erroneo:
![alt text](img/4.png)
Usuario correcto:
![alt text](img/5.png)
- `error.log`
![alt text](img/6.png)
# T.2
Borra las dos líneas que hacen referencia a la autenticación básica en el location del directorio raíz.
Tras ello, añade un nuevo location debajo con la autenticación básica para el archivo/sección
contact.html únicamente.
![alt text](img/7.png)
![alt text](img/8.png)
![alt text](img/9.png)
# T.3
## 3.1
Configura Nginx para que no deje acceder con la IP de la máquina anfitriona al directorio raíz de
una de tus dos webs. Modifica su server block o archivo de configuración. Comprueba como se
deniega el acceso:
- Muestra la página de error en el navegador
![alt text](img/10.png)
![alt text](img/11.png)
- Muestra el mensaje de error de error.log
![alt text](img/12.png)
## 3.2
Configura Nginx para que desde tu máquina anfitriona se tenga que tener tanto una IP válida como
un usuario válido, ambas cosas a la vez, y comprueba que sí puede acceder sin problemas
![alt text](img/13.png)
![alt text](img/14.png)
`access.log`
![alt text](img/15.png)