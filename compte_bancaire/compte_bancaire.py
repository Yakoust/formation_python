class CompteBancaire:
    def __init__(self, numero: int, nom: str, solde: int):
        self.numero = numero
        self.nom = nom
        self.solde = solde

    def versement(self, montant: int):
        self.solde = self.solde + montant

    def retrait(self, montant: int):
        self.solde = self.solde - montant

    def agios(self):
        self.solde = self.solde*0.95

    def afficher(self):
        print(f"Numéro de compte: {self.numero} \nNom: {self.nom} \nSolde: {self.solde}")