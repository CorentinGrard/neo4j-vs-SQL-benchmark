from Neo4jDatabase import Neo4jDatabase
from PostgreDatabase import PostgreDatabase
from generate_data import Personne
from generate_data import Produit


import names
import random
from random_word import RandomWords

if __name__ == "__main__":
    # Init connection
    neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
    postgre = PostgreDatabase("bolt://localhost:7687", "neo4j", "admin", )
    # Generate data
    # Generate personnes
    personnes = []
    for i in range(0, 100):
        prenom = names.get_first_name()
        nom = names.get_last_name()
        personne = Personne(prenom, nom)
        personnes.append(personne)

    
    postgre.createPersonnes(personnes)
    neo4j.createPersonnes(personnes)
    
    # Generate produits
    r = RandomWords()
    produits = []
    nomProduits = r.get_random_words(limit=500)
    for i in range(0, 100):
        nomProduit = nomProduits[random.randint(0, 499)]
        prix = random.randint(1, 500)
        produit = Produit(nomProduit, prix)
        produits.append(produit)

    # Neo4jDatabase.createProduits(produits)
    # PostgreDatabase.createProduits(produits)

    # Generate achats

    # Generate follow

    postgre.close()
    neo4j.close()