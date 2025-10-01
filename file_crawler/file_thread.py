import os
from threading import Thread
from collections import Counter

print("contenu du repertoire")
print(os.listdir("./files"))

files = list(filter(lambda f: os.path.isfile("./files/"+f), os.listdir("./files")))
print(files)

class FileCounter(Thread):
    def __init__(self, path: str):
        Thread.__init__(self)
        self.path = path

    def run(self):
        size = os.path.getsize(self.path)
        char_counter = []
        with open(self.path, "r", encoding="utf-8" ) as f:
            content = f.read()
            compteur = Counter(content)
            for caractere, frequence in compteur.items():
                char_counter.append((frequence, caractere))
        print(f"== Fichier {self.path} ===")
        print(f"taille du fichier: {size}")
        print(f"Apparition de caractères")
        for frequence, caractere  in char_counter:
            print(f"{caractere} : {frequence}")


threads = []
for f in files:
    t = FileCounter("./files/"+f)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("End of programme")