# **1. Configuración y acceso a las interfaces**
Por seguridad, Apache Tomcat bloquea el acceso a estas herramientas hasta que defines un usuario con los roles adecuados.
1. Abrimos el archivo conf/tomcat-users.xml dentro del directorio de instalación de Tomcat y añade los siguientes roles y usuario antes del cierre </tomcat-users>:
<img width="1209" height="533" alt="imagen" src="https://github.com/user-attachments/assets/960afb3a-d6ef-4469-a3ee-96fc2bad16bd" />
2. Reiniciaremos el servicio de Tomcat para aplicar los cambios.
  
3. Accederemos desde el navegador mediante las siguientes rutas:

   * __Manager:__ http://localhost:8080/manager/html
     <img width="1283" height="596" alt="imagen" src="https://github.com/user-attachments/assets/6ba13d7a-8e93-415f-b891-b32ec35a77fb" />

   * __Host Manager:__ http://localhost:8080/host-manager/html
     <img width="1298" height="579" alt="imagen" src="https://github.com/user-attachments/assets/d6f9e525-ae15-493e-a93e-bc5fe0b8603f" />

# **2. Ficha descriptiva: Tomcat Web Application Manager**
| Campo | Descripción |
| :--- | :--- |
| **Nombre oficial** | Tomcat Web Application Manager |
| **URL de acceso** | `http://localhost:8080/manager/html` (interfaz web) / `/manager/text` (scripts) |
| **Ubicación en disco** | `<CATALINA_BASE>/webapps/manager` |
| **Roles necesarios** | `manager-gui` (web), `manager-script` (automatización), `manager-jmx` (monitorización), `manager-status` (solo lectura) |
| **Ámbito de gestión** | Ciclo de vida de aplicaciones web individuales dentro de un host |
| **Persistencia** | Permanente en disco (directorio `webapps`) |
