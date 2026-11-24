# **1. Prueba de carga inicial (Línea base)**
1. Instalar ApacheBench
* Comando de instalación: ```sudo apt update && sudo apt install -y apache2-utils```
2. Ejecutaremos la prueba inicial con ApacheBench apuntando a la URL de nuestra aplicación desplegada con el siguiente comando:
```
ab -n 3000 -c 250 -k http://localhost:8080/hola-mundo/
```
* -n 3000: Envía 3000 peticiones totales.
* -c 250: Simula 250 usuarios concurrentes.
* -k: Activa HTTP Keep-Alive.

3. Anotaremos los valores clave de la salida
<img width="1017" height="553" alt="imagen" src="https://github.com/user-attachments/assets/bf457857-acec-4644-94ef-17b57bf051e6" />
<img width="902" height="422" alt="imagen" src="https://github.com/user-attachments/assets/dfefe222-1b20-46ab-9500-43ee0ed3169e" />




