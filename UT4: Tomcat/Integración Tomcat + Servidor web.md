# **1. Habilitar los módulos de Proxy en Apache**
Abrimos una terminal y activamos los módulos necesarios para que Apache pueda reenviar peticiones HTTP a Tomcat:
```
sudo a2enmod proxy
sudo a2enmod proxy_http
```
# **2. Configurar el VirtualHost de Apache como Reverse Proxy**
Vamos a editar la configuración del sitio por defecto de Apache (000-default.conf) para que todo el tráfico que llegue al puerto 80 (o a la ruta de tu aplicación) se redirija internamente al puerto 8080 de Tomcat.

1. Abriremos el archivo de configuración del VirtualHost con nano:
```
sudo nano /etc/apache2/sites-available/000-default.conf
```
2. Añadiremos las directivas ProxyPreserveHost, ProxyPass y ProxyPassReverse justo antes del cierre </VirtualHost>. Si queremos enrutar específicamente la aplicación hola-mundo de la práctica anterior (o todo el tráfico /), lo dejaremos así:
```
   <VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    # Configuración de Reverse Proxy hacia Tomcat
    ProxyPreserveHost On
    ProxyPass /hola-mundo http://127.0.0.1:8080/hola-mundo
    ProxyPassReverse /hola-mundo http://127.0.0.1:8080/hola-mundo
</VirtualHost>
```
3. Guardaremos y cerraremos el editor: pulsa Ctrl + O, luego Enter, y finalmente Ctrl + X.
4. Comprobaremos que la sintaxis de Apache no tiene errores y reiniciaremos el servicio con los comandos:
```
sudo apache2ctl configtest
sudo systemctl restart apache2
```

# **3. Verificar que la aplicación responde a través de Apache (Puerto 80)**
Nos aseguraremos de que Tomcat sigue encendido (sudo systemctl status tomcat) y realizaremos la comprobación desde el navegador o la terminal
1. Desde el navegador
Entraremos en la URL sin poner el puerto 8080

<img width="1297" height="290" alt="imagen" src="https://github.com/user-attachments/assets/d1921e0e-46ae-4acc-aeb2-6a611e5c7a27" />
Veremos que se cargará nuestra página JSP "¡Hola Mundo desde Apache Tomcat!", pero servida directamente a través del puerto 80 de Apache HTTP Server

3. Desde la terminal
Ejecutaremos curl -I http://localhost/hola-mundo/ para inspeccionar las cabeceras HTTP

<img width="934" height="346" alt="imagen" src="https://github.com/user-attachments/assets/6f0fde94-1940-4a07-907a-93e10662d603" />
Veremos un código de estado HTTP/1.1 200 OK junto con la cabecera Server: Apache/2.4.x (Ubuntu), demostrando que Apache actúa como intermediario delante de Tomcat.

# **4. Resumen técnico para documentar en tu entrega**
* Arquitectura implementada: Proxy Inverso (Reverse Proxy) HTTP entre Apache HTTP Server (puerto 80) y Apache Tomcat (puerto 8080).
* Módulos activados (a2enmod):
  * proxy: Proporciona la infraestructura básica de proxy en Apache.
  * proxy_http: Añade soporte para reenviar peticiones mediante el protocolo HTTP/HTTPS.
* Directivas utilizadas en 000-default.conf:
  * ProxyPreserveHost On: Mantiene la cabecera Host original enviada por el cliente al pasarla a Tomcat.
  * ProxyPass /hola-mundo [http://127.0.0.1:8080/hola-mundo](http://127.0.0.1:8080/hola-mundo): Mapea la URL pública de Apache hacia el servidor interno de Tomcat.
  * ProxyPassReverse /hola-mundo [http://127.0.0.1:8080/hola-mundo](http://127.0.0.1:8080/hola-mundo): Reescribe las cabeceras de redirección (Location) generadas por Tomcat para que el navegador del cliente nunca vea expuesto el puerto interno 8080.



