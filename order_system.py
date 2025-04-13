import heapq

class Order:
    def __init__(self, order_id, sku, quantity, priority):
        self.order_id = order_id
        self.sku = sku
        self.quantity = quantity
        self.priority = priority  # Lower number = higher priority

    def __lt__(self, other):
        return self.priority < other.priority

class OrderQueue:
    def __init__(self):
        self.queue = []

    def add_order(self, order):
        heapq.heappush(self.queue, order)

    def process_next(self):
        return heapq.heappop(self.queue) if self.queue else None
