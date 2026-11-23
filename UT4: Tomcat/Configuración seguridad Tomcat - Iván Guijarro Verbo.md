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


