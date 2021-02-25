from Neo4jDatabase import Neo4jDatabase
from PostgreDatabase import PostgreDatabase

from generate_data import *

import names
import random
from random_word import RandomWords

if __name__ == "__main__":
    nombrePersonnes = 1000
    nombreProduits = 1000

    # Init connection
    neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
    postgre = PostgreDatabase("database", "admin", "admin", "localhost")

    # Clear database
    neo4j.clearDatabase()
    postgre.clear_database()

    # Generate data
    # Generate personnes
    print("Génération des personnes....")
    personnes = generate_personne(nombrePersonnes)
    print("Génération des personnes - DONE")

    neo4j.createPersonnes(personnes)
    postgre.createPersonnes(personnes)

    # Generate produits
    print("Génération des produits....")
    produits = generate_produit(nombreProduits)
    print("Génération des produits - DONE")

    neo4j.createProduits(produits)
    postgre.createProduits(produits)

    # Generate achats
    print("Génération des achats....")
    achats = generate_achat(personnes, produits, nombreProduits)
    print("Génération des achats - DONE")

    neo4j.createAchats(achats)
    postgre.createAchats(achats)

    # Generate follows
    print("Génération des follows....")
    follows = generate_follow(personnes, nombrePersonnes)
    print("Génération des follows - DONE")
    neo4j.createFollows(follows)
    postgre.createFollows(follows)

    # Close sockets
    postgre.close()
    neo4j.close()