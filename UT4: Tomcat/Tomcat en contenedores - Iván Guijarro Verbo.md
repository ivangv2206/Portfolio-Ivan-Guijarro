# **1. Descargar imagen oficial de Tomcat**
1. Para poder descargar la imagen de Tomcat desde docker tendremos que utilizar el siguiente comando:
```
docker pull tomcat:latest
```
<img width="983" height="283" alt="imagen" src="https://github.com/user-attachments/assets/76164694-398c-43e9-b319-3d30b3b4f02a" />
<img width="1294" height="256" alt="imagen" src="https://github.com/user-attachments/assets/8f861717-3c2c-4789-91d4-f57daee34d40" />

## 2. Montar la aplicación
1. Prepararemos la carpeta local con nuestra aplicación web para montarla en el contenedor
```
mkdir -p ~/tomcat-webapps/hola-mundo
echo "<h1>Hola Mundo desde Tomcat en Docker</h1>" > ~/tomcat-webapps/hola-mundo/index.html
```
<img width="1281" height="224" alt="imagen" src="https://github.com/user-attachments/assets/a2681a5e-d793-405b-b699-0ee5623dc057" />

2. Arrancaremos el contenedor montando la aplicación en /usr/local/tomcat/webapps:
```
docker run -d --name tomcat-contenedor -p 8081:8080 -v ~/tomcat-webapps:/usr/local/tomcat/webapps tomcat:latest
```
<img width="1286" height="302" alt="imagen" src="https://github.com/user-attachments/assets/47451095-8028-4920-bfe7-47aad8853089" />
_Una vez que hemos puesto el contenedor en marcha, si entramos en http://localhost:8081/hola-mundo/, veremos la página web que hemos creado anteriormente_
<img width="1299" height="305" alt="imagen" src="https://github.com/user-attachments/assets/f9a68b76-6081-4f19-be27-20e85094ef99" />

# **3. Comparativa: Tomcat nativo vs. Tomcat en contenedor**
| Criterio | Tomcat Nativo | Tomcat en Contenedor (Docker) |
| :--- | :--- | :--- |
| **Aislamiento** | Comparte sistema operativo, librerías y versión de Java (`JDK`) con el anfitrión. | Entorno aislado mediante *namespaces* y *cgroups* con su propio runtime de Java y Tomcat. |
| **Instalación y ciclo de vida** | Instalación manual en `/opt/tomcat` y actualización modificando archivos en el servidor. | Inmutable y desechable: se actualiza descargando una nueva etiqueta de imagen y recreando el contenedor. |
| **Persistencia de datos** | Archivos de configuración (`conf/`) y aplicaciones (`webapps/`) persistentes en disco por defecto. | Sistema de archivos efímero; requiere volúmenes o *bind mounts* (`-v`) para conservar aplicaciones y configuración. |
| **Red y puertos** | Enlaza directamente con las interfaces de red del anfitrión (puerto `8080`). | Red virtual interna (*bridge*) que exige mapeo explícito de puertos (`-p 8081:8080`). |
| **Portabilidad y escalado** | Requiere replicar configuraciones o clonar máquinas virtuales completas. | Alta portabilidad entre entornos y capacidad de escalar réplicas en segundos. |


