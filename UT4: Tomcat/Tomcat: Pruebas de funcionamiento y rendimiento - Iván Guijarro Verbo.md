# **1. Prueba de carga inicial (Línea base)**
1. Instalar ApacheBench
* Comando de instalación: ```sudo apt update && sudo apt install -y apache2-utils```
2. Ejecutaremos la prueba inicial con ApacheBench apuntando a la URL de nuestra aplicación desplegada con el siguiente comando:
```
ab -n 3000 -c 250 -k http://localhost:8080/hola-mundo/
```
* -n 3000: Envía 3000 peticiones totales.
* -c 250: Simula 250 usuarios concurrentes.
* -k: Activa HTTP Keep-Alive.

3. Anotaremos los valores clave de la salida
<img width="1017" height="553" alt="imagen" src="https://github.com/user-attachments/assets/bf457857-acec-4644-94ef-17b57bf051e6" />
<img width="902" height="422" alt="imagen" src="https://github.com/user-attachments/assets/dfefe222-1b20-46ab-9500-43ee0ed3169e" />
<img width="720" height="232" alt="imagen" src="https://github.com/user-attachments/assets/279124e9-50d4-4e2d-8e0d-0b3845c97541" />

# **2. Ajustes de rendimiento en conf/server.xml**
Antes de modificar la configuración, guardaremos una copia de seguridad del archivo original con el comando: ```cp conf/server.xml conf/server.xml.bak```
1. Abre el archivo conf/server.xml en el directorio de Tomcat y localiza el conector HTTP principal (<Connector ... port="8080" protocol="HTTP/1.1"/>).
2. Sustituiremos o amplía sus atributos para aumentar la capacidad de hilos, ampliar la cola de espera y reducir el tiempo de bloqueo de conexiones inactivas:
```
<Connector port="8080"
           protocol="org.apache.coyote.http11.Http11NioProtocol"
           connectionTimeout="10000"
           maxThreads="400"
           minSpareThreads="50"
           acceptCount="200"
           maxConnections="10000"
           compression="on"
           compressionMinSize="1024"
           compressibleMimeType="text/html,text/xml,text/plain,text/css,text/javascript,application/javascript,application/json"
           redirectPort="8443" />
```
## Qué hace cada parámetro ajustado
* maxThreads="400" (defecto: 200): Duplica el número máximo de hilos simultáneos capaces de procesar peticiones HTTP concurrentes.
* minSpareThreads="50" (defecto: 10): Mantiene 50 hilos siempre activos en reserva para absorber picos repentinos de tráfico sin latencia de creación.
* acceptCount="200" (defecto: 100): Amplía la cola del sistema operativo para peticiones entrantes cuando los 400 hilos están ocupados, evitando errores de conexión rechazada (Connection reset).
* maxConnections="10000" (defecto: 8192 en NIO): Aumenta el límite de conexiones TCP simultáneas abiertas en el conector no bloqueante.
* connectionTimeout="10000" (defecto: 20000): Reduce de 20 a 10 segundos el tiempo de espera antes de cerrar conexiones inactivas, liberando recursos antes.
* compression="on": Activa la compresión GZIP en respuestas de texto/HTML/JSON mayores de 1 KB, reduciendo el ancho de banda y el tiempo de transferencia.
3. Reiniciaremos Tomcat para aplicar la configuración

# **3. Segunda prueba de carga (Comparativa "Después")**
Ejecutaremos el mismo comando del apartado 1 bajos las mismas condiciones para que la comparación sea válida.
Los resultados que obtendremos serán los siguientes:
<img width="961" height="554" alt="imagen" src="https://github.com/user-attachments/assets/01a3fb6d-78e4-430c-8b60-951e1d979555" />
<img width="767" height="416" alt="imagen" src="https://github.com/user-attachments/assets/7d693406-369f-4c60-97df-f15dd2f75baf" />





