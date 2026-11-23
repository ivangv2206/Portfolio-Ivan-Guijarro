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

# **2. Restringir el acceso al Manager por IP**
Por seguridad, Tomcat bloquea por defecto el acceso remoto a /manager y /host-manager permitiendo solo conexiones desde localhost (127.0.0.1). Vamos a verificar y ajustar esa regla para documentar cómo se restringe (o cómo permitir una IP específica de tu red local si accedes desde fuera de la VM).
1. Abriremos el archivo context.xml de la aplicación Manager con el siguiente comando:
```
sudo nano /opt/tomcat/webapps/manager/META-INF/context.xml
```
2. Localizaremos la etiqueta <Valve ... className="org.apache.catalina.valves.RemoteAddrValve"/>. Para mantener la restricción estricta solo a la máquina local (o añadir una IP de administración concreta, por ejemplo 192.168.1.50), nos aseguraremos que quede así:
```
<Context antiResourceLocking="false" privileged="true" >
  <CookieProcessor className="org.apache.tomcat.util.http.Rfc6265CookieProcessor"
                   sameSiteCookies="strict" />
  <Valve className="org.apache.catalina.valves.RemoteAddrValve"
         allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />
</Context>
```
# **3. Configurar HTTPS con un Keystore y un Conector SSL**
## Generar el certificado autofirmado
1. Crearemos un almacén de claves PKCS12 dentro de /opt/tomcat/conf/ usando el siguiente comando:
```
sudo keytool -genkey -alias tomcat -keyalg RSA -keysize 2048 -storetype PKCS12 -keystore /opt/tomcat/conf/tomcat.p12 -validity 365 -storepass changeit -dname "CN=localhost, OU=Desarrollo, O=Practica, L=Madrid, ST=Madrid, C=ES"
```
2. Aseguraremos los permisos del keystore para que Tomcat pueda leerlo con los siguientes comandos:
```
sudo chmod 640 /opt/tomcat/conf/tomcat.p12
sudo chown root:tomcat /opt/tomcat/conf/tomcat.p12 2>/dev/null || sudo chmod 644 /opt/tomcat/conf/tomcat.p12
```
## Activar el Conector SSL en server.xml
1. Abriremos server.xml con el siguiente comando:
```
sudo nano /opt/tomcat/conf/server.xml
```
2. Buscaremos la sección donde está el conector del puerto 8080 (<Connector ... port="8080"/>) y añadiremos justo debajo el conector HTTPS en el puerto 8443 de la siguiente manera:
```
<Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"
           maxThreads="150" SSLEnabled="true" scheme="https" secure="true">
    <SSLHostConfig>
        <Certificate certificateKeystoreFile="conf/tomcat.p12"
                     certificateKeystorePassword="changeit"
                     certificateKeystoreType="PKCS12"
                     type="RSA" />
    </SSLHostConfig>
</Connector>
```
3. Reiniciaremos Tomcat para aplicar todos los cambios de seguridad con el siguiente comando:
```
sudo systemctl restart tomcat
```
4. Comprobaremos que Tomcat está escuchando tanto en el puerto 8080 como en el 8443 ejecutando:
```
ss -tlnp | grep -E "8080|8443"
```
# **4. Realizar la prueba de acceso autenticado y tomar evidencias**
1. Prueba de conexión cifrada HTTPS
* Entraremos en https://localhost:8443/hola-mundo/ (o https://localhost:8443/).
* Firefox mostrará una advertencia de seguridad ("Riesgo potencial de seguridad" por ser un certificado autofirmado). Haremos clic en Avanzado... $\rightarrow$ Aceptar el riesgo y continuar.

*Veremos el candado con aviso en la barra de direcciones junto a https://localhost:8443 y la página cargada.*
<img width="1855" height="450" alt="image" src="https://github.com/user-attachments/assets/401fc0b4-a39d-41b2-9ebe-416dcc01e500" />

2. Prueba de autenticación en el Manager App
* Entraremos en https://localhost:8443/manager/html
* Aparecerá una ventana emergente pidiendo Nombre de usuario y contraseña. Introduciremos admin y PasswordSegura2026
<img width="1857" height="429" alt="image" src="https://github.com/user-attachments/assets/60da1790-9e65-41cf-a8e1-b461abe96461" />

*Una vez que hayamos entrado, veremos que se listan nuestras aplicaciones desplegadas y también veremos la página de hola-mundo)*
<img width="1852" height="856" alt="image" src="https://github.com/user-attachments/assets/b6a6df6c-04a0-452f-b18e-adf0515b57e1" />

# **5. Nota sobre el Security Manager**
* El Java Security Manager limita los permisos a nivel de código Java (acceso a archivos, sockets o propiedades del sistema) mediante el archivo conf/catalina.policy, arrancando Tomcat con ./catalina.sh start -security.
* En versiones modernas de Java (Java 17 en adelante, JEP 411) y Tomcat 10.1/11, el Security Manager de Java ha quedado obsoleto (deprecated), por lo que en entornos actuales se prioriza el aislamiento mediante contenedores, permisos del sistema operativo y proxy inverso con TLS/HTTPS como acabas de configurar.
