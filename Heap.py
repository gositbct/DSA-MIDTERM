import heapq
class Heap:
    def __init__(self, mode='max'):
        self.mode = mode
        self.data = []

    def insert(self, val):
        heapq.heappush(self.data, -val if self.mode == 'max' else val)

    def pop(self):
        if not self.data:
            return None
        val = heapq.heappop(self.data)
        return -val if self.mode == 'max' else val

    def list(self):
        return [-x if self.mode == 'max' else x for x in self.data]