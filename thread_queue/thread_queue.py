import queue
import random
import time
from threading import Thread

class Producer(Thread):
    def __init__(self, q):
        Thread.__init__(self)
        self.q = q

    def run(self):
        for i in range(10):
            item = random.randint(1, 100)
            print(f"Producer => {item}")
            self.q.put(item)
            time.sleep(random.random() * 0.5)
        self.q.put(0)

class Consumer(Thread):
    def __init__(self, q):
        Thread.__init__(self)
        self.q = q

    def run(self):
        while True:
            item = self.q.get()
            if item == 0:
                break
            print(f"Consumer => {item}")
            time.sleep(random.random() * 0.5)


if __name__ == "__main__":
    q = queue.Queue()

    producer = Producer(q)
    consumer = Consumer(q)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("Fin du programe")