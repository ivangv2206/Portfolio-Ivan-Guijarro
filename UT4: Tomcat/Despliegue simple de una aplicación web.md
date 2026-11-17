# **1. Generar un archivo WAR de ejemplo (Hello World JSP)**
1. Abre una terminal y pasa a usuario root o crea el proyecto en /tmp:
```
mkdir -p /tmp/hola-mundo/WEB-INF
```
2. Crea el archivo index.jsp con un saludo dinámico en Java:
```
nano index.jsp
```
El contenido de este archivo será el siguiente:
```
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head><title>Práctica Despliegue Tomcat</title></head>
<body>
    <h1>¡Hola Mundo desde Apache Tomcat!</h1>
    <p>Fecha y hora del servidor: <%= new java.util.Date() %></p>
</body>
</html>
```
3. Empaquetaremos la carpeta en un archivo hola-mundo.war usando la herramienta jar de Java:
```
cd /tmp/hola-mundo
jar -cvf /tmp/hola-mundo.war *
```
# **2.Desplegar el WAR en la carpeta webapps**
1. Nos aseguraremos de que el servicio Tomcat está arrancado con el comando:
```
systemctl status tomcat
```
2. Copiaremos el archivo .war dentro del directorio de despliegue de Tomcat:
```
sudo cp /tmp/hola-mundo.war /opt/tomcat/webapps/
```
*Veremos el archivo hola-mundo.war como una carpeta nueva llamada hola-mundo*
<img width="788" height="240" alt="imagen" src="https://github.com/user-attachments/assets/a17eb4d7-25ed-4289-962b-58a0f6406c9d" />
