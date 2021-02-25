import json
import names
import random
from random_word import RandomWords

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

def generate_personne(nombrePersonnes):
    personnes = []
    for i in range(0, nombrePersonnes):
        id = i
        prenom = names.get_first_name()
        nom = names.get_last_name()
        personne = Personne(id, prenom, nom)
        personnes.append(personne)
    return personnes

def generate_produit(nombreProduits):
    r = RandomWords()
    produits = []
    nomProduits = r.get_random_words(limit=500)
    for i in range(0, nombreProduits):
        id = i
        nomProduit = nomProduits[random.randint(0, 499)]
        prix = random.randint(1, 500)
        produit = Produit(id, nomProduit, prix)
        produits.append(produit)
    return produits

def generate_achat(personnes, produits, nombreProduits):
    achats = []
    j = 0
    for personne in personnes:
        nbAchats = random.randint(0, 5)
        for i in range(0, nbAchats):
            produit = produits[random.randint(0, nombreProduits - 1)]
            achat = Achat(j, produit.id, personne.id)
            j += 1
            achats.append(achat)
    return achats

def generate_follow(personnes, nombrePersonnes):
    follows = []
    banList = []
    for myPersonne in personnes:
        nbFollow = random.randint(0, 20)
        for i in range(0, nbFollow):
            personneToFollow = random.randint(0, nombrePersonnes - 1)
            if personneToFollow in banList:
                i -= i
                continue
            banList.append(personneToFollow)

            follow = Follow(myPersonne.id, personneToFollow)
            follows.append(follow)
        banList = []
    return follows