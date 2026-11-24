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
<img width="712" height="227" alt="imagen" src="https://github.com/user-attachments/assets/710dd76f-f2a0-45ef-985c-c7fff60a73f6" />

## 3.1. Tabla Comparativa de Resultados (Antes vs. Después)

| Métrica de rendimiento | Antes (Defecto) | Después (Optimizado) | Variación |
| :--- | :---: | :---: | :---: |
| **Peticiones completadas (`Complete requests`)** | `3000` | `3000` | `0 %` |
| **Peticiones fallidas (`Failed requests`)** | `0` | `0` | `0 %` |
| **Tiempo total de la prueba (`Time taken`)** | `2.546 s` | `3.664 s` | `+43,9 %` |
| **Peticiones por segundo (`Requests/sec`)** | `1178.41 #/s` | `818.86 #/s` | `-30,5 %` |
| **Tiempo medio por petición (`Time/request`)** | `212.149 ms` | `305.302 ms` | `+43,9 %` |
| **Tiempo medio concurrente (`across all`)** | `0.849 ms` | `1.221 ms` | `+43,8 %` |
| **Tiempo medio de conexión (`Connect`)** | `14 ms` (máx. `1063 ms`) | `1 ms` (máx. `21 ms`) | `-92,9 %` |
| **Percentil 80 % de respuesta** | `265 ms` | `165 ms` | `-37,7 %` |
| **Percentil 95 % de respuesta** | `1098 ms` | `2026 ms` | `+84,5 %` |
| **Percentil 99 % de respuesta** | `2021 ms` | `2998 ms` | `+48,3 %` |
| **Tasa de transferencia (`Transfer rate`)** | `515.56 KB/s` | `358.25 KB/s` | `-30,5 %` |

---

# **4. Conclusiones**

* **Aceleración en el establecimiento de conexiones:** Aumentar `minSpareThreads` a `50` y `acceptCount` a `200` eliminó casi por completo la latencia inicial de conexión (`Connect`), pasando de `14 ms` de media (con picos de `1063 ms`) a `1 ms` (máximo `21 ms`). Gracias a ello, hasta el percentil 80 % de las peticiones redujo su tiempo de respuesta de `265 ms` a `165 ms`.
* **Contención de CPU en entorno virtualizado:** Aunque la aceptación de conexiones fue mucho más rápida, el rendimiento global (`Requests/sec`) descendió de `1178.41 #/s` a `818.86 #/s` y aumentó la latencia en los percentiles altos (`95 %` y `99 %`). Esto ocurre porque la prueba se ejecutó en una máquina virtual (`VirtualBox`) donde Tomcat (con `400` hilos) y ApacheBench (`250` clientes concurrentes) compiten por los mismos núcleos virtuales de CPU, generando sobrecarga por cambios de contexto.
* **Comportamiento de la compresión GZIP:** El volumen total de datos transferidos se mantuvo en `1344000 bytes` (`603000 bytes` de HTML) en ambas pruebas, ya que la página `/hola-mundo/` ocupa `201 bytes` y no supera el umbral mínimo configurado en `compressionMinSize="1024"`.


