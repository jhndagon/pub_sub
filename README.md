# 📌 Patrón de Arquitectura Publicador–Suscriptor (Pub/Sub)

## 📖 Arquitectura de Software I

Este repositorio contiene el desarrollo del trabajo académico sobre el **Patrón de Arquitectura Publicador–Suscriptor (Publish–Subscribe)**, realizado como parte de la asignatura **Arquitectura de Software I**.

El objetivo principal de este trabajo es analizar, explicar e implementar el patrón Pub/Sub, comprendiendo su funcionamiento, ventajas, desventajas y aplicaciones en sistemas modernos.

---

## 🎯 Objetivos del Trabajo

- Explicar el funcionamiento del patrón **Publish–Subscribe**.
- Describir sus componentes principales: Publisher, Subscriber y Broker.
- Analizar ventajas y desventajas del patrón.
- Presentar un ejemplo práctico de implementación.
- Comprender su aplicación en arquitecturas orientadas a eventos.

---

## 🏗️ ¿Qué es el patrón Pub/Sub?

El patrón **Publicador–Suscriptor (Pub/Sub)** es un modelo de comunicación en el que:

- Un **Publicador (Publisher)** envía mensajes o eventos.
- Uno o varios **Suscriptores (Subscribers)** reciben los mensajes.
- Un **Intermediario (Broker o Event Bus)** gestiona la distribución de los mensajes a los suscriptores correspondientes.

Este patrón permite un **alto desacoplamiento**, ya que los publicadores no necesitan conocer directamente a los suscriptores. La comunicación suele ser **asíncrona**, lo que mejora la escalabilidad y flexibilidad del sistema.

Es ampliamente utilizado en:

- Sistemas distribuidos  
- Microservicios  
- Arquitecturas orientadas a eventos  
- Sistemas de notificaciones  
- Plataformas de mensajería como Kafka o RabbitMQ  

---

## 📂 Contenido del Proyecto

Este repositorio contiene **dos implementaciones del patrón Pub/Sub**:

1. ✅ Implementación básica en Python (sin broker externo).
2. 🐰 Implementación con RabbitMQ utilizando Docker (rama `feature/with-rabbit`).

---

## 📦 Enlace al Repositorio

Repositorio oficial del proyecto:

🔗 https://github.com/jhndagon/pub_sub

---

## 🌿 Versiones Disponibles

### 🔹 Rama principal (`main`)
Contiene la implementación básica del patrón Pub/Sub en Python, utilizando estructuras internas y simulación asincrónica.

### 🔹 Rama `feature/with-rabbit`
Contiene una implementación más cercana a un entorno real de producción, utilizando:

- RabbitMQ como broker
- Docker Compose para levantar el servicio
- Publisher y Subscriber desacoplados
- Comunicación real vía AMQP

Para usar esta versión:

```bash
git checkout feature/with-rabbit
```

---

## ⚙️ Requisitos

- Python 3.9 o superior  
- Git instalado  
- (Para la versión con RabbitMQ) Docker y Docker Compose  

---

## ▶️ Instrucciones para Ejecutar el Proyecto

### 🔹 Opción 1 – Implementación Básica (rama `main`)

1️⃣ Clonar el repositorio:

```bash
git clone https://github.com/jhndagon/pub_sub.git
```

2️⃣ Ingresar a la carpeta del proyecto:

```bash
cd pub_sub
```

3️⃣ Ejecutar:

```bash
python main.py
```

---

### 🔹 Opción 2 – Implementación con RabbitMQ (rama `feature/with-rabbit`)

1️⃣ Cambiar a la rama correspondiente:

```bash
git checkout feature/with-rabbit
```

2️⃣ Seguir las instrucciones detalladas en el archivo:

📄 **execution.md**

En ese archivo encontrarás el paso a paso para:

- Levantar RabbitMQ con Docker
- Instalar dependencias
- Ejecutar Subscriber
- Ejecutar Publisher
- Validar el funcionamiento

---

## 🖥️ Resultado Esperado

Dependiendo de la implementación utilizada:

- Se visualizará la publicación de eventos.
- Los suscriptores recibirán los mensajes.
- Se demostrará el desacoplamiento entre componentes.
- En la versión con RabbitMQ, la comunicación se realiza mediante un broker real.

---

## 👥 Integrantes

1. John David Gonzalez Alzate  
2. Jorge Rolando Maradey Duran  
3. Sergio Mauricio Aparicio Hernandez  
4. Hernan David Rodriguez Garcia  
5. William Steven Clavijo Valero  

---

## 📊 Presentación (PPT)

https://unisabanaedu-my.sharepoint.com/:p:/r/personal/johngoal_unisabana_edu_co/Documents/Patron_Arquitectura_PubSub_ESTILO_limpio.pptx?d=w6f55ce459a8c43408cd595af319a5e4c&csf=1&web=1&e=yH8MDo

---

## 🎥 Video Explicativo

https://drive.google.com/file/d/1aV29YR9OkgqaBesIOHzLp153rVholRKw/view?usp=sharing

---

## 🧠 Conclusión

El patrón Pub/Sub es una arquitectura clave en sistemas modernos debido a su capacidad de desacoplamiento, escalabilidad y comunicación asincrónica. Su comprensión es fundamental para el diseño de arquitecturas distribuidas y orientadas a eventos.