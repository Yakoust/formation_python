class WaterTank:
    """ Défini une citerne """

    total_volume: float = 0

    def __init__(self, poids: float, capacite_max: float, niveau: float):
        self.poids = poids
        self.capacite_max = capacite_max
        self.niveau = niveau

    def remplir(self, quantite):
        if self.niveau + quantite > self.capacite_max:
            quantite = self.capacite_max - self.niveau

        self.niveau += quantite
        WaterTank.total_volume += quantite

    def vider(self, quantite):
        if self.niveau - quantite < 0:
            quantite = self.niveau

        self.niveau -= quantite
        WaterTank.total_volume -= quantite

    @property
    def poids_total(self):
        return self.poids + self.niveau



wt = WaterTank(poids=100, capacite_max=100, niveau=0)
wt2 = WaterTank(poids=150, capacite_max=200, niveau=0)
print(wt.poids_total)
wt.remplir(20)
print(wt.poids_total)
wt2.remplir(250)
print(wt2.poids_total)
print(WaterTank.total_volume)