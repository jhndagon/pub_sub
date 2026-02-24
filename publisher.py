

# =========================
# Publisher
# =========================
class Publisher:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def publish(self, topic, message):
        self.event_bus.publish(topic, message)