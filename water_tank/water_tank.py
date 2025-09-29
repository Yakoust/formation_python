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

