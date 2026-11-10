**Investiga y describe brevemente los siguientes elementos de Tomcat**:

* **Catalina:** Es el motor contenedor de servlets y de JSP _(JavaServer Pages)_ de Apache Tomcat. Se encarga procesar las peticiones HTTP que llegan al servidor, ejecuta los servlets y páginas JSP, cumple con las especificaciones de Jakarta/Sun Microsystems para tecnologías web basadas en Java y administra el arranque, la carga, la ejecución y el apagado de los componentes de las aplicaciones web.
En la arquitectura de Tomcat es el núcleo del servidor; mientras que en el sistema de archivos se encuentra dentro de la estructura de carpetas de la instalación de Apache Tomcat.

* **Coyote:** Es el conector HTTP que actúa como la interfaz de red del servidor. Se encarga de recibir las respuestas HTTP/HTTPS que envían los navegadores u otras aplicaciones, está a la escucha en un puerto TCP determinado **(8080 para HTTP)** y toma los datos de la solicitud entrante, los traduce y se los pasa a Catalina para que procese la lógica de la aplicación.
En la arquitectura de Tomcat se encuentra en la capa de conectores, justo en la frontera entre la red externa (el cliente o navegador) y el núcleo de procesamiento de Java.

* **Jasper:** Es el motor de JSP _(JavaServer Pages engine)_ integrado dentro del servidor Apache Tomcat. Se encarga de leer los archivos con código JSP y los compila convirtiéndolos en servlets de Java ejecutables, detecta cambios en las páginas JSP y puede recompilarlas en segundo plano sin interrumpir las peticiones del servidor y administra el pooling (reutilización) de etiquetas personalizadas para optimizar el rendimiento.
En la arquitectura de Tomcat forma parte del núcleo del contenedor de Apache Tomcat junto con Catalina y Coyote; mientras que en el sistema de archivos, las librerías de Jasper (jasper.jar, jasper-el.jar, etc.) están en la carpeta /lib del directorio raíz de Tomcat.
  
* Tomcat Manager y Host Manager: Son dos aplicaciones web administrativas que se utilizan para gestionar el servidor de forma remota o mediante interfaz visual.
  * Manager: Se encarga de desplegar y eliminar archivos .war y hacer deploy o undeploy de aplicaciones sin reiniciar Tomcat, inicia, detiene o recarga aplicaciones específicas, ve el uso de memoria de la JVM, hilos activos y sesiones de usuario abiertas y permite gestionar comandos vía script.
    Se encuentra dentro de la estructura de directorios del servidor en la carpeta webapps/manager/ y en la URL de acceso web poniendo la dirección http://localhost:8080/manager
    
  * Host Manager: Sirve para administrar los hosts virtuales, añade o elimina nuevos dominios al servidor sin modificar manualmente los archivos de configuración en disco y configurar cómo responde Tomcat ante distintas peticiones de dominio.
    Se encuentra dentro dentro de la estructura de directorios del servidor en la carpeta webapss/host-manager/ y en la URL de acceso web poniendo la dirección http://localhost:8080/host-manager.
    
* Estructura básica de directorios (bin, conf, webapps, lib, logs):
  | Left columns  | Right columns |
| ------------- |:-------------:|
| left foo      | right foo     |
| left bar      | right bar     |
| left baz      | right baz     |
* Flujo interno de funcionamiento: recepción de peticiones, contenedores, despliegue de aplicaciones.

**BIBLIOGRAFÍA**
* [Catalina](https://es.wikipedia.org/wiki/Tomcat#Tomcat_Catalina)
* [Coyote](https://www.hostgator.mx/blog/apache-tomcat-que-es-para-que-sirve-y-como-usarlo-en-la-practica/)
* [Jasper](https://tomcat.apache.org/tomcat-9.0-doc/jasper-howto.html)
* [Manager y Host Manager](https://codigoelectronica.com/blog/administrador-de-apache-tomcat)
* [Estructura básica de directorios]()
* [Flujo interno de funcionamiento]()

