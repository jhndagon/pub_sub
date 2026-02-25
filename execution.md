---

# ▶️ Instrucciones de Ejecución

## ✅ 1. Requisitos Previos

Asegúrate de tener instalado:

- Docker
- Docker Compose
- Python 3.9 o superior
- pip

Verificar versiones:

```bash
docker --version
docker compose version
python --version
```

---

## 🐳 2. Levantar RabbitMQ con Docker

Desde la raíz del proyecto, ejecutar:

```bash
docker compose up -d
```

Verificar que el contenedor esté corriendo:

```bash
docker ps
```

Deberías ver un contenedor llamado:

```
rabbitmq_pubsub
```

---

## 🌐 3. Acceder al Panel de RabbitMQ (Opcional)

Abrir en el navegador:

```
http://localhost:15672
```

Credenciales:

- Usuario: `admin`
- Password: `admin`

---

## 📦 4. Instalar Dependencias de Python

Instalar la librería `pika`:

```bash
pip install -r requirements.txt
```

---

## 🔵 5. Ejecutar el Subscriber (Consumidor)

En una terminal:

```bash
python subscriber.py
```

El sistema mostrará:

```
📥 Esperando mensajes...
```

---

## 🟢 6. Ejecutar el Publisher (Productor)

En otra terminal:

```bash
python publisher.py
```

Se mostrará:

```
📤 Mensaje enviado: {...}
```

Y en la terminal del subscriber:

```
✅ Mensaje recibido: {...}
```

---

# 🧠 ¿Qué está ocurriendo?

1. RabbitMQ actúa como broker.
2. El Publisher envía un mensaje al exchange tipo `fanout`.
3. RabbitMQ distribuye el mensaje a todas las colas suscritas.
4. El Subscriber recibe el mensaje de manera asíncrona.

---

## 🛑 7. Detener el Sistema

Para detener RabbitMQ:

```bash
docker compose down
```

---

# 🚀 Flujo Completo de Ejecución

```bash
docker compose up -d
pip install -r requirements.txt
python subscriber.py
python publisher.py
docker compose down
```