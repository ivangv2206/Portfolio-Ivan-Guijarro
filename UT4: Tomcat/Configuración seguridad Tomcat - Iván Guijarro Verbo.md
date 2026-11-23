# **1. Definir roles y usuarios en tomcat-users.xml**
1. Abriremos el archivo de usuarios de Tomcat como superusuario con el siguiente comando:
```
sudo nano /opt/tomcat/conf/tomcat-users.xml
```
2. Bajaremos hasta el final del archivo y, justo antes de la etiqueta de cierre </tomcat-users>, añadiremos los roles administrativos y un usuario de prueba:
```
<role rolename="manager-gui"/>
<role rolename="manager-script"/>
<role rolename="admin-gui"/>
<user username="admin" password="PasswordSegura2026" roles="manager-gui,manager-script,admin-gui"/>
```
3. 
