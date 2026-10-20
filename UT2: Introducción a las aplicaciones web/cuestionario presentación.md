# Cuestionario presentación

**1. ¿Qué significa las siglas HTTP y para qué se utiliza?**
HTTP significa *Hypertext Transfer Protocol* (Protocolo de Transferencia de Hipertexto). Se utiliza para la comunicación y transferencia de datos (páginas web, imágenes, videos) en la World Wide Web entre un cliente (como un navegador) y un servidor web.

**2. ¿En qué puerto funciona normalmente el protocolo HTTP?**
El protocolo HTTP utiliza por defecto el puerto **80**.

**3. ¿Cuál es la diferencia principal entre HTTP y HTTPS?**
La diferencia principal es la seguridad. HTTPS incluye la "S" de *Secure*, ya que utiliza un protocolo de cifrado (SSL/TLS) para proteger la información que viaja entre el cliente y el servidor, mientras que en HTTP la información viaja en texto plano y puede ser interceptada. Funciona en el puerto 443.

**4. ¿Qué función cumple el servidor web Apache dentro de una arquitectura web?**
Apache actúa como intermediario entre el servidor y las peticiones del cliente. Su función principal es recibir las solicitudes HTTP/HTTPS de los navegadores, buscar los recursos solicitados (archivos HTML, imágenes, etc.) o pasarlos al servidor de aplicaciones, y devolver la respuesta adecuada al cliente.

**5. ¿Cómo puedes comprobar si el servicio de Apache está activo en un sistema Ubuntu?**
Puedes comprobarlo abriendo la terminal y ejecutando el siguiente comando:
`sudo systemctl status apache2`

**6. Explica brevemente en qué consiste una arquitectura cliente-servidor.**
Es un modelo de diseño de software en el que las tareas se reparten entre los proveedores de recursos o servicios, llamados **servidores**, y los demandantes, llamados **clientes**. El cliente realiza peticiones y el servidor las procesa y devuelve una respuesta.

**7. ¿Qué diferencia hay entre una arquitectura de dos capas y una de tres capas en entornos web?**
- **Dos capas:** El cliente (interfaz de usuario) se comunica directamente con un servidor que maneja tanto la lógica de la aplicación como la base de datos de forma conjunta.
- **Tres capas:** Se divide en una capa de presentación (cliente), una capa de lógica de negocio (servidor de aplicaciones) y una capa de datos (servidor de base de datos), lo que permite mayor escalabilidad, seguridad y mantenimiento.

**8. ¿Qué es el protocolo FTP y para qué se usa?**
FTP significa *File Transfer Protocol* (Protocolo de Transferencia de Archivos). Se utiliza para transferir archivos a través de una red TCP/IP entre un cliente y un servidor, permitiendo subir, descargar, renombrar o eliminar archivos en remoto. Funciona típicamente en los puertos 20 y 21.

**9. Menciona un ejemplo de cliente FTP y un ejemplo de servidor FTP.**
- **Cliente FTP:** FileZilla o Cyberduck.
- **Servidor FTP:** vsftpd o ProFTPD.

**10. ¿Qué diferencia existe entre FTP y SFTP?**
Al igual que con HTTP y HTTPS, la diferencia es la seguridad. FTP envía los datos (incluyendo credenciales) en texto plano. SFTP (*SSH File Transfer Protocol*) transmite todos los datos de forma cifrada a través de una conexión segura SSH.

**11. Indica tres tipos de alojamiento web y explica brevemente en qué se diferencian.**
- **Alojamiento Compartido:** Múltiples sitios web comparten los recursos físicos (CPU, RAM, disco) de un mismo servidor. Es el más económico pero el de menor rendimiento.
- **VPS (Servidor Privado Virtual):** Un servidor físico se divide en máquinas virtuales. Cada sitio tiene recursos dedicados y mayor control (acceso root), simulando un servidor propio.
- **Servidor Dedicado:** Se alquila un servidor físico completo en exclusiva para un solo cliente. Ofrece el máximo rendimiento, control y seguridad, pero a un coste mucho mayor.

**12. ¿Qué ventajas ofrece un servidor VPS frente a un alojamiento compartido?**
Un VPS ofrece recursos garantizados e independientes (la sobrecarga de otras webs no te afecta), mayor seguridad y privacidad debido al aislamiento virtual, y control total sobre la configuración del sistema (acceso *root* para instalar el software que desees).

**13. Describe brevemente los componentes principales de una arquitectura web moderna.**
Suele estar compuesta por:
- **Frontend / Cliente:** Navegadores o apps que consumen la aplicación.
- **Balanceador de carga:** Distribuye el tráfico entrante entre varios servidores.
- **Servidor Web:** (Ej: Apache, Nginx) Maneja las peticiones estáticas y redirige el tráfico dinámico.
- **Servidor de Aplicaciones (Backend):** Procesa la lógica de negocio y maneja frameworks (Ej: Node.js, PHP, Python).
- **Servidor de Base de Datos:** Almacena la información de forma persistente (Ej: MySQL, PostgreSQL, MongoDB).

**14. ¿Qué papel cumple el servidor de aplicaciones dentro de dicha arquitectura?**
Su papel es ejecutar la lógica de negocio de la aplicación. Actúa como puente procesando datos dinámicos, comunicándose con la base de datos para recuperar o guardar información, y generando la respuesta (JSON, HTML dinámico) que el servidor web enviará de vuelta al cliente.

**15. ¿Qué software o paquete puedes usar para instalar Apache fácilmente en Windows?**
Los paquetes más comunes son **XAMPP** o **WampServer**, que incluyen Apache, MySQL, PHP y otras herramientas preconfiguradas.

**16. ¿Qué carpeta suele contener los archivos del sitio web en una instalación de Apache en Windows (por ejemplo, con XAMPP)?**
Normalmente es la carpeta `htdocs` que se encuentra dentro del directorio de instalación de XAMPP (por ejemplo, `C:\xampp\htdocs\`).

**17. Escribe el comando para instalar Apache en Ubuntu desde la terminal.**
`sudo apt update && sudo apt install apache2`

**18. ¿Qué comando se usa para iniciar el servicio Apache en Ubuntu?**
`sudo systemctl start apache2`

**19. ¿En qué ruta se almacena normalmente la página web por defecto de Apache en Ubuntu?**
La ruta del directorio raíz web por defecto es: `/var/www/html/`.

**20. ¿Qué es el protocolo SSH y cuál es su propósito principal?**
SSH (*Secure Shell*) es un protocolo de administración remota que permite a los usuarios controlar y modificar sus servidores a través de Internet. Su propósito principal es establecer una conexión segura y cifrada entre un cliente y un servidor, sustituyendo a protocolos inseguros antiguos como Telnet.

**21. ¿Qué comando se usa para conectarse a un servidor remoto mediante SSH?**
`ssh nombre_usuario@direccion_ip` (o usando un nombre de dominio en lugar de la IP).

**22. Menciona una ventaja de usar autenticación mediante claves SSH frente a contraseñas.**
La principal ventaja es una seguridad muy superior. Las claves criptográficas son prácticamente imposibles de adivinar mediante ataques de fuerza bruta o diccionario, a diferencia de las contraseñas. Además, permiten el inicio de sesión automático sin tener que escribir una clave cada vez, facilitando la automatización de tareas.

> Iván Guijarro Verbo 2º DAW
