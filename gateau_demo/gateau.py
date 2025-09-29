class Gateau:
    """ Représentation d'un gâteau """
    def __init__(self, nom: str, temps_cuisson: int, ingredients: list[str], etapes: list[str], createur: str):
        self.nom = nom
        self.temps_cuisson = temps_cuisson
        self.ingredients = ingredients
        self.etapes = etapes
        self.createur = createur

    def afficher_ingredient(self):
        print( "\n".join(self.ingredients))


    def afficher_etapes(self):
        print( "\n".join(self.etapes))

