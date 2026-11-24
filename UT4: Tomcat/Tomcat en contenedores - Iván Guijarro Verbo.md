# **1. Descargar imagen oficial de Tomcat**
1. Para poder descargar la imagen de Tomcat desde docker tendremos que utilizar el siguiente comando:
```
docker pull tomcat:latest
```
<img width="983" height="283" alt="imagen" src="https://github.com/user-attachments/assets/76164694-398c-43e9-b319-3d30b3b4f02a" />
<img width="1294" height="256" alt="imagen" src="https://github.com/user-attachments/assets/8f861717-3c2c-4789-91d4-f57daee34d40" />

2. Prepararemos la carpeta local con nuestra aplicación web para montarla en el contenedor
```
mkdir -p ~/tomcat-webapps/hola-mundo
echo "<h1>Hola Mundo desde Tomcat en Docker</h1>" > ~/tomcat-webapps/hola-mundo/index.html
```
<img width="1281" height="224" alt="imagen" src="https://github.com/user-attachments/assets/a2681a5e-d793-405b-b699-0ee5623dc057" />

3. Arrancaremos el contenedor montando la aplicación en /usr/local/tomcat/webapps:
```
docker run -d --name tomcat-contenedor -p 8081:8080 -v ~/tomcat-webapps:/usr/local/tomcat/webapps tomcat:latest
```
