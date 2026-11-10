**Investiga y describe brevemente los siguientes elementos de Tomcat**:

* Catalina: Es el motor contenedor de servlets y de JSP (JavaServer Pages) de Apache Tomcat. Se encarga procesar las peticiones HTTP que llegan al servidor, ejecuta los servlets y páginas JSP, cumple con las especificaciones de Jakarta/Sun Microsystems para tecnologías web basadas en Java y administra el arranque, la carga, la ejecución y el apagado de los componentes de las aplicaciones web.
En la arquitectura de Tomcat es el núcleo del servidor; mientras que en el sistema de archivos se encuentra dentro de la estructura de carpetas de la instalación de Apache Tomcat.

* Coyote: Es el conector HTTP que actúa como la interfaz de red del servidor. Se encarga de recibir las respuestas HTTP/HTTPS que envían los navegadores u otras aplicaciones, está a la escucha en un puerto TCP determinado (8080 para HTTP) y toma los datos de la solicitud entrante, los traduce y se los pasa a Catalina para que procese la lógica de la aplicación.
En la arquitectura de Tomcat se encuentra en la capa de conectores, justo en la frontera entre la red externa (el cliente o navegador) y el núcleo de procesamiento de Java.

* Jasper: Es el motor de JSP (JavaServer Pages engine) integrado dentro del servidor Apache Tomcat. Se encarga de leer los archivos con código JSP y los compila convirtiéndolos en servlets de Java ejecutables, detecta cambios en las páginas JSP y puede recompilarlas en segundo plano sin interrumpir las peticiones del servidor y administra el pooling (reutilización) de etiquetas personalizadas para optimizar el rendimiento.
En la arquitectura de Tomcat forma parte del núcleo del contenedor de Apache Tomcat junto con Catalina y Coyote; mientras que en el sistema de archivos, las librerías de Jasper (jasper.jar, jasper-el.jar, etc.) están en la carpeta /lib del directorio raíz de Tomcat.
  
* Manager y Host Manager

* Estructura básica de directorios (bin, conf, webapps, lib, logs)
* Flujo interno de funcionamiento: recepción de peticiones, contenedores, despliegue de aplicaciones.

**BIBLIOGRAFÍA**
* [Catalina](https://es.wikipedia.org/wiki/Tomcat#Tomcat_Catalina)
* [Coyote](https://www.hostgator.mx/blog/apache-tomcat-que-es-para-que-sirve-y-como-usarlo-en-la-practica/)
* [Jasper](https://tomcat.apache.org/tomcat-9.0-doc/jasper-howto.html)
* [Manager y Host Manager]()
* [Estructura básica de directorios]()
* [Flujo interno de funcionamiento]()

