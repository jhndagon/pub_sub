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

- 📜 Explicación teórica del patrón.
- 💻 Ejemplo práctico de implementación en Python.
- 📊 Presentación en PowerPoint.
- 🎥 Video explicativo del trabajo.

---

## 📦 Enlace al Repositorio

Repositorio oficial del proyecto:

🔗 https://github.com/jhndagon/pub_sub

---

## ⚙️ Requisitos

- Python 3.9 o superior  
- Git instalado (opcional, si se va a clonar el repositorio)  
- No requiere librerías externas (solo librerías estándar de Python)

---

## ▶️ Instrucciones para Ejecutar el Proyecto

Las instrucciones detalladas de ejecución se encuentran en el archivo:

📄 **execution.md**

En este archivo encontrarás:

- Cómo clonar el repositorio
- Cómo verificar requisitos
- Cómo ejecutar el proyecto paso a paso
- Resultado esperado en consola
- Cómo detener correctamente los servicios (si aplica)

Por favor, consulta ese archivo para realizar la ejecución completa del sistema.

---

## 👥 Integrantes

1. John David Gonzalez Alzate  
2. Jorge Rolando Maradey Duran  
3. Sergio Mauricio Aparicio Hernandez  
4. Hernan David Rodriguez Garcia  
5. William Steven Clavijo Valero  

---

## 📊 Presentación (PPT)

Puedes acceder a la presentación del trabajo en el siguiente enlace:

https://unisabanaedu-my.sharepoint.com/:p:/r/personal/johngoal_unisabana_edu_co/Documents/Patron_Arquitectura_PubSub_ESTILO_limpio.pptx?d=w6f55ce459a8c43408cd595af319a5e4c&csf=1&web=1&e=yH8MDo

---

## 🎥 Video Explicativo

El video de sustentación del trabajo está disponible en:

https://drive.google.com/file/d/1aESU8vJhpLyZujbezpB35v53jRGLvz-t/view?usp=drive_link

---

## 🧠 Conclusión

El patrón Pub/Sub es una arquitectura clave en sistemas modernos debido a su capacidad de desacoplamiento, escalabilidad y comunicación asincrónica. Su comprensión es fundamental para el diseño de arquitecturas distribuidas y orientadas a eventos.