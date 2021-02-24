import json


class Personne:
    def __init__(self, id, prenom, nom):
        self.id = id
        self.prenom = prenom
        self.nom = nom


class Produit:
    def __init__(self, id, nom, prix):
        self.id = id
        self.nom = nom
        self.prix = prix

class Achat:
    def __init__(self, id, idProduit, idPersonne):
        self.id = id
        self.idProduit = idProduit
        self.idPersonne = idPersonne

class Follow:
    def __init__(self, idFollower, idFollowed):
        self.idFollower = idFollower
        self.idFollowed = idFollowed