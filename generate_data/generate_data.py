import json


class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
