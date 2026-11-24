# **1. Descargar imagen oficial de Tomcat**
1. Para poder descargar la imagen de Tomcat desde docker tendremos que utilizar el siguiente comando:
```
docker pull tomcat:latest
```
2. Prepararemos la carpeta local con nuestra aplicación web para montarla en el contenedor
```
mkdir -p ~/tomcat-webapps/hola-mundo
echo "<h1>Hola Mundo desde Tomcat en Docker</h1>" > ~/tomcat-webapps/hola-mundo/index.html
```
3. Arrancaremos el contenedor montando la aplicación en /usr/local/tomcat/webapps:
```
docker run -d --name tomcat-contenedor -p 8081:8080 -v ~/tomcat-webapps:/usr/local/tomcat/webapps tomcat:latest
```
