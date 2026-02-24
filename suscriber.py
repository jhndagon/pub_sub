import time

# =========================
# Subscriber
# =========================
class Subscriber:
    def __init__(self, name):
        self.name = name

    def notify(self, message):
        time.sleep(1)  # Simula procesamiento
        print(f"[{self.name}] recibió mensaje: {message}")
