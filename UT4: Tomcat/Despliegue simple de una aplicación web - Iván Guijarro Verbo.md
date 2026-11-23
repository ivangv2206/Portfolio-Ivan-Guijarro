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

# **3. ¿Qué hace Tomcat internamente?**
Cuando depositas un archivo .war en /opt/tomcat/webapps/ con el servidor en marcha (gracias a las propiedades autoDeploy="true" y unpackWARs="true" definidas en conf/server.xml), Tomcat ejecuta de forma automática el siguiente ciclo de despliegue en caliente (hot deployment):

1. Detección del artefacto: El hilo de monitorización en segundo plano del componente <Host> (background processor) escanea periódicamente el directorio appBase (webapps/) y detecta un archivo .war nuevo que no tiene un contexto asociado.
2. Descompresión (Unpacking): Al estar activo unpackWARs="true", Tomcat extrae el contenido del archivo comprimido hola-mundo.war creando un directorio homónimo (webapps/hola-mundo/).
3. Creación del Contexto (StandardContext): Tomcat instancia un nuevo contexto web asociado a la ruta URL /hola-mundo (derivada directamente del nombre del archivo .war).
4. Carga de configuración y descriptores:
    * Aplica primero la configuración global de conf/context.xml y conf/web.xml.
    * Busca dentro de la aplicación el archivo META-INF/context.xml y el descriptor WEB-INF/web.xml (si existen) para fusionar o sobrescribir la configuración específica de la app.

5. Inicialización del ClassLoader y Servlets: Crea un cargador de clases aislado (WebappClassLoader) para cargar las librerías (WEB-INF/lib) y clases (WEB-INF/classes) de la aplicación sin interferir con otras apps del servidor, e inicializa los Listeners, Filters y Servlets marcados para cargar al inicio.

6. Registro en los logs y puesta en servicio: Registra el evento en logs/catalina.out (con mensajes como Deploying web application archive [.../hola-mundo.war] y Deployment of web application archive [...] has finished in X ms) y deja la ruta lista para recibir peticiones HTTP a través de los conectores (8080).

# **4. Acceder a la aplicación y tomar la evidencia**
1. Abrimos el navegador web dentro de tu máquina virtual Ubuntu (Firefox) y entra en:http://localhost:8080/hola-mundo/Verificación: Aparecerá la página web mostrando el título "¡Hola Mundo desde Apache Tomcat!" junto con la fecha y hora actual generada por el servidor JSP.

<img width="1299" height="367" alt="imagen" src="https://github.com/user-attachments/assets/307fa722-aa88-4c3b-a79f-25536a46140c" />


