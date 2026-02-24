import threading
from collections import defaultdict

# =========================
# Event Bus (Broker)
# =========================
class EventBus:
    def __init__(self):
        # Diccionario: topic -> lista de subscribers
        self.subscribers = defaultdict(list)

    def subscribe(self, topic, subscriber):
        print(f"[EventBus] {subscriber.name} suscrito a '{topic}'")
        self.subscribers[topic].append(subscriber)

    def publish(self, topic, message):
        print(f"\n[EventBus] Publicando mensaje en '{topic}': {message}")
        if topic in self.subscribers:
            for subscriber in self.subscribers[topic]:
                # Ejecutar cada subscriber en un hilo (simula asincronía)
                threading.Thread(
                    target=subscriber.notify,
                    args=(message,)
                ).start()
