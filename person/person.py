from ftplib import print_line


class Person:
    def __init__(self, nom: str, prenom: str, tel: str, email: str):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.email = email

    def __str__(self):
        return f"Nom: {self.prenom} {self.nom}\nTel: {self.tel}\nEmail: {self.email}"

class Travailleur(Person):
    def __init__(self, nom: str, prenom: str, tel: str, email: str, nom_entreprise: str, adresse_pro: str, tel_pro: str):
        super().__init__(nom, prenom, tel, email)
        self.nom_entreprise = nom_entreprise
        self.adresse_pro = adresse_pro
        self.tel_pro = tel_pro

    def __str__(self):
        return f"{super().__str__()}\nEntreprise: {self.nom_entreprise}\nAdresse pro: {self.adresse_pro}\nTel pro: {self.tel_pro}"

class Scientifique(Travailleur):
    def __init__(self, nom: str, prenom: str, tel: str, email: str, nom_entreprise: str, adresse_pro: str, tel_pro: str, disciplines: list[str], types: list[str]):
        super().__init__(nom, prenom, tel, email, nom_entreprise, adresse_pro, tel_pro)
        self.disciplines = disciplines
        self.types = types

    def __str__(self):
        disciplines_str = "\n".join(self.disciplines)
        types_str = "\n".join(self.types)
        return f"{super().__str__()}\n\nDisciplines:\n{disciplines_str}\n\nTypes:\n{types_str}"


p = Person(
    "Doe",
    "John",
    "+33612121214",
    "john.doe@gcourrier.com"
)
print("Ma personne")
print(p)
print("\n\n")
t = Travailleur(
    "Doe",
    "John",
    "+33612121214",
    "john.doe@gcourrier.com",
    "Work s.a.",
    "Python DC",
    "+33678451236"
)

print("Mon travailleur")
print(t)
print("\n\n")
s = Scientifique(
    "Doe",
    "John",
    "+33612121214",
    "john.doe@gcourrier.com",
    "Work s.a.",
    "Python DC",
    "+33678451236",
    ["Physique", "Chimie"],
    ["Informatique", "Thérorique"]
)
print("Mon scientifique")
print(s)