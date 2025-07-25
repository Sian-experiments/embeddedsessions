import time
import random

class Elevator:
    def __init__(self, floors=5):
        self.current_floor = 1
        self.requests = []
    
    def request_floor(self, floor):
        if floor not in self.requests:
            self.requests.append(floor)
    
    def move(self):
        while self.requests:
            target_floor = min(self.requests, key=lambda x: abs(x - self.current_floor))
            print(f"Moving to floor {target_floor}")
            time.sleep(1)  # Simulating movement
            self.current_floor = target_floor
            self.requests.remove(target_floor)
            print(f"Arrived at floor {self.current_floor}")

elevator = Elevator()
elevator.request_floor(random.randint(1, 5))
elevator.move()
