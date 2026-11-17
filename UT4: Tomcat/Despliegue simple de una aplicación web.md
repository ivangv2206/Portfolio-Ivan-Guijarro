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
