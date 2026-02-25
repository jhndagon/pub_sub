import time

from broker import EventBus
from subscriber import Subscriber
from publisher import Publisher


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    event_bus = EventBus()

    # Crear subscribers
    email_service = Subscriber("EmailService")
    sms_service = Subscriber("SMSService")
    analytics_service = Subscriber("AnalyticsService")

    # Suscribirse a tópicos
    event_bus.subscribe("order_created", email_service)
    event_bus.subscribe("order_created", sms_service)
    event_bus.subscribe("order_created", analytics_service)

    # Crear publisher
    order_service = Publisher(event_bus)

    # Publicar evento
    order_service.publish("order_created", {
        "order_id": 1234,
        "user": "John",
        "total": 250.00
    })

    # Esperar para que los hilos terminen
    time.sleep(3)