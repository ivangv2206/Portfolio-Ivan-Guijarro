# Práctica: Pruebas de Funcionamiento y Rendimiento en Apache Tomcat

## 1. Entorno de Pruebas

| Parámetro | Detalle |
| :--- | :--- |
| **Servidor de aplicaciones** | Apache Tomcat [Versión, ej. 10.1 / 11.0] |
| **Aplicación evaluada** | `http://localhost:8080/[nombre-app]/` |
| **Herramienta de carga** | ApacheBench (`ab`) |
| **Comando ejecutado** | `ab -n 3000 -c 250 -k http://localhost:8080/[nombre-app]/` |
| **Carga simulada** | 3.000 peticiones totales con 250 usuarios concurrentes |

---

## 2. Ajustes Realizados en `conf/server.xml`

Se modificó el elemento `<Connector>` del puerto `8080` con los siguientes valores:

| Atributo | Valor por defecto (Antes) | Valor optimizado (Después) | Objetivo del ajuste |
| :--- | :---: | :---: | :--- |
| `maxThreads` | `200` | `400` | Aumentar los hilos simultáneos para atender mayor concurrencia sin encolamiento. |
| `minSpareThreads` | `10` | `50` | Mantener hilos pre-inicializados listos ante picos repentinos de tráfico. |
| `acceptCount` | `100` | `200` | Ampliar la cola de espera de conexiones cuando todos los hilos están ocupados. |
| `maxConnections` | `8192` | `10000` | Permitir un mayor número de conexiones NIO simultáneas abiertas. |
| `connectionTimeout` | `20000` ms | `10000` ms | Liberar más rápido las conexiones abiertas que no envían datos. |
| `compression` | `off` | `on` | Comprimir respuestas HTTP de texto/HTML/JSON para reducir latencia de red. |

---

## 3. Comparativa de Resultados (Antes vs. Después)

| Métrica de rendimiento | Antes (Defecto) | Después (Optimizado) | Variación / Mejora |
| :--- | :---: | :---: | :---: |
| **Peticiones completadas** | `3000` | `3000` | — |
| **Peticiones fallidas (`Failed requests`)** | `[ej. 12]` | `[ej. 0]` | `[ej. -100 %]` |
| **Peticiones por segundo (`Requests/sec`)** | `[ej. 845.20 #/s]` | `[ej. 1420.50 #/s]` | `[ej. +68.0 %]` |
| **Tiempo medio por petición (`Time/request`)** | `[ej. 295.80 ms]` | `[ej. 176.00 ms]` | `[ej. -40.5 %]` |
| **Tiempo medio concurrente (`across all`)** | `[ej. 1.18 ms]` | `[ej. 0.70 ms]` | `[ej. -40.7 %]` |
| **Percentil 95 % de respuesta** | `[ej. 510 ms]` | `[ej. 240 ms]` | `[ej. -52.9 %]` |
| **Percentil 99 % de respuesta** | `[ej. 890 ms]` | `[ej. 310 ms]` | `[ej. -65.2 %]` |
| **Tasa de transferencia (`Transfer rate`)** | `[ej. 1250.40 KB/s]` | `[ej. 1890.10 KB/s]` | `[ej. +51.2 %]` |

---

## 4. Conclusiones

* **Eliminación de cuellos de botella en hilos:** Con la configuración por defecto (`maxThreads="200"`), las 250 peticiones concurrentes superaban la capacidad inmediata de procesamiento, provocando esperas en la cola de red y elevando el percentil 99 %. Al ampliar `maxThreads` a `400` y `minSpareThreads` a `50`, Tomcat absorbió toda la concurrencia de forma paralela.
* **Estabilidad bajo carga:** El aumento de `acceptCount` junto con la reducción de `connectionTimeout` evitó descartes de paquetes y liberó conexiones ociosas con mayor rapidez.
* **Impacto en latencia y rendimiento:** El rendimiento global (`Requests/sec`) aumentó significativamente y el tiempo medio de respuesta percibido por cada usuario disminuyó de forma notable sin comprometer la estabilidad del servidor.
