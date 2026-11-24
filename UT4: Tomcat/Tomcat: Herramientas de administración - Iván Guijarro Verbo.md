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

## Funciones principales
* Despliegue (Deploy): Instala nuevas aplicaciones web en caliente sin detener el servidor. Permite subir directamente un paquete WAR desde el equipo local o indicar una ruta del servidor (Context Path y ubicación del directorio o archivo).
* Arranque (Start): Pone en marcha una aplicación previamente detenida para que vuelva a responder peticiones HTTP.
* Parada (Stop): Detiene una aplicación en ejecución sin eliminar sus archivos del servidor. Útil para tareas de mantenimiento mientras se devuelve un error 404 controlado a los usuarios.
* Recarga (Reload): Reinicia exclusivamente el contexto de una aplicación concreta para aplicar cambios en sus clases Java (WEB-INF/classes) o librerías (WEB-INF/lib) sin reiniciar todo el servidor Tomcat.
* Retirada (Undeploy): Detiene la aplicación y elimina por completo su directorio y archivo .war del directorio webapps.Diagnóstico y estado (Server Status / sesiones): Muestra el número de sesiones activas por aplicación, permite expirar sesiones inactivas para liberar memoria y ofrece métricas de la máquina virtual Java (JVM) y los hilos de conexión.

# **3. Ficha descriptiva: Tomcat Virtual Host Manager**
| Campo | Descripción |
| :--- | :--- |
| **Nombre oficial** | Tomcat Virtual Host Manager |
| **URL de acceso** | `http://localhost:8080/host-manager/html` (interfaz web) / `/host-manager/text` (scripts) |
| **Ubicación en disco** | `<CATALINA_BASE>/webapps/host-manager` |
| **Roles necesarios** | `admin-gui` (interfaz web), `admin-script` (automatización) |
| **Ámbito de gestión** | Gestión de dominios y alojamientos virtuales (*Virtual Hosts*) a nivel de motor (`Engine`) |
| **Persistencia** | Temporal en memoria (desaparece al reiniciar salvo que se guarde/declare en `conf/server.xml`) |

## Funciones principales
* Creación de hosts virtuales (Add Virtual Host): Permite alojar múltiples sitios web con distintos nombres de dominio (por ejemplo, app1.empresa.local y app2.empresa.local) sobre una misma instancia y puerto de Tomcat. Al dar de alta un host se configuran sus parámetros clave:
  * Name: Nombre de dominio completamente cualificado (FQDN) al que responderá el host.
  * App base: Directorio base en el servidor donde se almacenarán las aplicaciones propias de ese host virtual.
  * AutoDeploy / DeployOnStartup: Opciones para activar el despliegue automático al iniciar Tomcat o al copiar nuevos archivos en su appBase.
  * UnpackWARs: Indica si Tomcat debe descomprimir automáticamente los paquetes .war en carpetas.
* Arranque y parada de hosts: Habilita o deshabilita el servicio completo de un host virtual específico sin afectar al resto de dominios alojados en el servidor.
* Eliminación de hosts (Remove): Da de baja un host virtual activo de la memoria del servidor.
* Persistencia de configuración: Los hosts virtuales creados desde esta interfaz web se cargan dinámicamente en memoria, pero desaparecen al reiniciar Tomcat. Para hacerlos permanentes, la herramienta permite guardar la configuración o requiere declararlos mediante etiquetas <Host> dentro del archivo conf/server.xml (además de registrar los dominios en el servidor DNS o archivo hosts del sistema operativo).

# **4. Comparativa rápida entre ambas herramientas**
| Criterio | Web Application Manager | Virtual Host Manager |
| :--- | :--- | :--- |
| **Nivel de actuación** | Aplicación web (contexto) | Servidor / Dominio (host virtual) |
| **Rol gráfico principal** | `manager-gui` | `admin-gui` |
| **Operación habitual** | Subir archivos `.war` y recargar código | Crear nuevos dominios en una misma instancia |
| **Persistencia de cambios** | Permanente en disco (`webapps`) | Temporal en memoria (salvo ed
