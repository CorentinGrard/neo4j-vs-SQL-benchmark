from Neo4jDatabase import Neo4jDatabase
from PostgreDatabase import PostgreDatabase
from generate_data import *

import names
import random
from random_word import RandomWords
from time import time

if __name__ == "__main__":
    nombrePersonnes = 100000
    nombreProduits = 100000

    # Init connection
    neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
    postgre = PostgreDatabase("database", "admin", "admin", "localhost")

    # Clear database
    neo4j.clearDatabase()
    postgre.clear_database()

    # Create Indexes
    neo4j.createIndex()

    # Start timers
    timeStartAll = time()
    timeNeo4j = 0
    timePostgre = 0

    # Generate data
    # Generate personnes
    print("---------------------------------------------------------")
    print("Génération des personnes....")
    personnes = generate_personne(nombrePersonnes)
    print("Génération des personnes - DONE")

    timeNeo4j += neo4j.createPersonnes(personnes)
    timePostgre += postgre.createPersonnes(personnes)

    # Generate produits
    print("---------------------------------------------------------")
    print("Génération des produits....")
    produits = generate_produit(nombreProduits)
    print("Génération des produits - DONE")

    timeNeo4j += neo4j.createProduits(produits)
    timePostgre += postgre.createProduits(produits)

    # Generate achats
    print("---------------------------------------------------------")
    print("Génération des achats....")
    achats = generate_achat(personnes, produits, nombreProduits)
    print("Génération des achats - DONE")

    timeNeo4j += neo4j.createAchats(achats)
    timePostgre += postgre.createAchats(achats)

    # Generate follows
    print("---------------------------------------------------------")
    print("Génération des follows....")
    follows = generate_follow(personnes, nombrePersonnes)
    print("Génération des follows - DONE")

    timeNeo4j += neo4j.createFollows(follows)
    timePostgre += postgre.createFollows(follows)

    timeEndAll = time()
    print("---------------------------------------------------------")
    print("Temps d'exécution total Neo4j : " + str(timeNeo4j) + " s")
    print("Temps d'exécution total Postgre : " + str(timePostgre) + " s")
    print("Temps d'exécution total : " + str(timeNeo4j + timePostgre) + " s")
    print("Temps d'exécution total (avec génération ): " + str(timeEndAll - timeStartAll) + " s")
    print("---------------------------------------------------------")
    # Close sockets
    postgre.close()
    neo4j.close()