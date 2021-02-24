from Neo4jDatabase import Neo4jDatabase
from PostgreDatabase import PostgreDatabase
from generate_data import Personne
from generate_data import Produit
from generate_data import Achat
from generate_data import Follow

import names
import random
from random_word import RandomWords

if __name__ == "__main__":
    nombrePersonnes = 100
    nombreProduits = 100


    # Init connection
    neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
    postgre = PostgreDatabase("bolt://localhost:7687", "neo4j", "admin", )
    # Clear database   
    neo4j.clearDatabase()

    # Generate data
    # Generate personnes
    personnes = []
    for i in range(0, nombrePersonnes):
        id = i
        prenom = names.get_first_name()
        nom = names.get_last_name()
        personne = Personne(id, prenom, nom)
        personnes.append(personne)

    
    postgre.createPersonnes(personnes)
    neo4j.createPersonnes(personnes)
    
    # Generate produits
    r = RandomWords()
    produits = []
    nomProduits = r.get_random_words(limit=500)
    for i in range(0, nombreProduits):
        id = i
        nomProduit = nomProduits[random.randint(0, 499)]
        prix = random.randint(1, 500)
        produit = Produit(id, nomProduit, prix)
        produits.append(produit)

    neo4j.createProduits(produits)
    postgre.createProduits(produits)

    # Generate achats
    achats = []
    for personne in personnes:
        nbAchats = random.randint(0, 5)
        for i in range(0, nbAchats):
            produit = produits[random.randint(0, nombreProduits -1)]
            achat = Achat(id, produit.id, personne.id)
            achats.append(achat)

    neo4j.createAchats(achats)
    postgre.createAchats(achats)
    
    # Generate follow
    follows = []
    for myPersonne in personnes:
        nbFollow = random.randint(0, 20)
        for i in range(0, nbFollow):
            personneToFollow = personnes[random.randint(0, nombrePersonnes -1)]
            follow = Follow(myPersonne.id, personneToFollow.id)
            follows.append(follow)

    neo4j.createFollows(follows)
    postgre.createFollows(follows)
    # Close sockets
    postgre.close()
    #neo4j.close()