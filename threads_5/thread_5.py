from threading import Thread
import queue
import random
import time

N = 5
job_queue = queue.Queue()

for _ in range(20):
    job_queue.put(random.randint(0, 5))

def worker(thread_id, job_queue):
    while True:
        try:
            job = job_queue.get(False)
        except queue.Empty:
            print(f"Fin de la pile")
            break

        time.sleep(job)
        print(f"{thread_id} terminé")

        job_queue.task_done()

threads = []
for i in range(N):
    t = Thread(target=worker, args=(i, job_queue))
    threads.append(t)
    t.start()

job_queue.join()

for t in threads:
    t.join()

print("Fin du programme")
