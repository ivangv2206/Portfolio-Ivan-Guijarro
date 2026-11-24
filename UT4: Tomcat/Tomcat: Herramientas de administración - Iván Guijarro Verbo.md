#**1. Configuración y acceso a las interfaces**
Por seguridad, Apache Tomcat bloquea el acceso a estas herramientas hasta que defines un usuario con los roles adecuados.
1. Abrimos el archivo conf/tomcat-users.xml dentro del directorio de instalación de Tomcat y añade los siguientes roles y usuario antes del cierre </tomcat-users>:
<img width="1209" height="533" alt="imagen" src="https://github.com/user-attachments/assets/960afb3a-d6ef-4469-a3ee-96fc2bad16bd" />
2. Reiniciaremos el servicio de Tomcat para aplicar los cambios.
3. Accederemos desde el navegador mediante las siguientes rutas:
   * __Manager:__ http://localhost:8080/manager/html
   * __Host Manager:__ http://localhost:8080/host-manager/html

#**2. Ficha descriptiva: Tomcat Web Application Manager**

