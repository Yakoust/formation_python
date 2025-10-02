import os, json
from functools import reduce

file_path = './catalogue.json'
mon_dict: dict = {
  "produits": [
    {"id": 1, "nom": "Stylo", "prix": 1.8},
    {"id": 2, "nom": "Cahier", "prix": 2.5},
    {"id": 3, "nom": "Sac",   "prix": 19.9}
  ]
}

if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        json.dump(mon_dict, f, indent=2)


with open(file_path, 'r') as f_read:
    data = json.load(f_read)
    produits = data['produits']
    total = reduce(lambda x, y: x + y["prix"], produits, 0)
    data["total"] = total

print(json.dumps(data, indent=2))

with open("./catalogue_total.json", 'w') as f_total:
    json.dump(data, f_total, indent=2)
