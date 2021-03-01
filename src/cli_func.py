from Neo4jDatabase import Neo4jDatabase
from PostgreDatabase import PostgreDatabase
from generate_data import *

import names
import random
from random_word import RandomWords
from time import time
from pprint import pprint

def search(personne_id, depth, database):
    if database == "postgres":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        followers_produit = postgre.influenceur(
            personne_id, depth)
        postgre.close()
        # print(followers_produit)

    elif database == "neo4j":
        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
        followers_produit = neo4j.influenceur(
            personne_id, depth)
        neo4j.close()
        # print(followers_produit)
    elif database == "pg4j":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        followers_produit = postgre.influenceur(
            personne_id, depth)
        postgre.close()
        # print(followers_produit)
        
        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
        followers_produit = neo4j.influenceur(
            personne_id, depth)
        neo4j.close()
        # print(followers_produit)
    else:
        print("Invalid database argument")


def searchproduct(personne_id, produit_id,depth, database):
    if database == "postgres":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        produits = postgre.list_achat_products_specific_produits(personne_id, produit_id, depth)
        postgre.close()
        pprint(produits)
    elif database == "neo4j":
        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
        produits = neo4j.list_achat_products_specific_produits(personne_id, produit_id, depth)
        neo4j.close()
        pprint(produits)
    elif database == "pg4j":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        produits = postgre.list_achat_products_specific_produits(personne_id, produit_id, depth)
        postgre.close()
        pprint(produits)
        
        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
        produits = neo4j.list_achat_products_specific_produits(personne_id, produit_id, depth)
        neo4j.close()
        pprint(produits)
    else:
        print("Invalid database argument")

def viralite(produit_id, depth, database):
    if database == "postgres":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        viralite = postgre.viralite(produit_id, depth)
        postgre.close()
        print(viralite)
    elif database == "neo4j":
        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin") 
        viralite = neo4j.viralite(produit_id, depth)
        neo4j.close()
        print(viralite)
    elif database == "pg4j":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        viralite = postgre.viralite(produit_id, depth)
        postgre.close()
        print(viralite)

        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin") 
        viralite = neo4j.viralite(produit_id, depth)
        neo4j.close()
        print(viralite)
    else:
        print("Invalid database argument")


def gendata(number_personne, number_produit):

    # Init connection
    neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
    postgre = PostgreDatabase("database", "admin", "admin", "localhost")

    # Clear database
    neo4j.clearDatabase()
    postgre.clear_database()

    # Create Indexes
    neo4j.createIndexes()

    # Start timers
    timeStartAll = time()
    timeNeo4j = 0
    timePostgre = 0
    timeGenerate = 0

    # Generate data
    # Generate personnes
    print("---------------------------------------------------------")
    print("Génération des personnes....")
    tic = time()
    personnes = generate_personne(number_personne)
    toc = time()
    temps = toc - tic
    timeGenerate += temps
    print("\tTemps d'exécution : " + str(temps) + " s")
    print("Génération des personnes - DONE")

    timeNeo4j += neo4j.createPersonnes(personnes)
    # timePostgre += postgre.createPersonnes(personnes)

    # Generate produits
    print("---------------------------------------------------------")
    print("Génération des produits....")
    tic = time()
    produits = generate_produit(number_produit)
    toc = time()
    temps = toc - tic
    timeGenerate += temps
    print("\tTemps d'exécution : " + str(temps) + " s")
    print("Génération des produits - DONE")

    timeNeo4j += neo4j.createProduits(produits)
    # timePostgre += postgre.createProduits(produits)

    # Generate achats
    print("---------------------------------------------------------")
    print("Génération des achats....")
    tic = time()
    achats = generate_achat(personnes, produits, number_produit)
    toc = time()
    temps = toc - tic
    timeGenerate += temps
    print("\tTemps d'exécution : " + str(temps) + " s")
    print("Génération des achats - DONE")

    timeNeo4j += neo4j.createAchats(achats)
    # timePostgre += postgre.createAchats(achats)

    # Generate follows
    print("---------------------------------------------------------")
    print("Génération des follows....")
    tic = time()
    follows = generate_follow(personnes, number_personne)
    toc = time()
    temps = toc - tic
    timeGenerate += temps
    print("\tTemps d'exécution : " + str(temps) + " s")
    print("Génération des follows - DONE")

    timeNeo4j += neo4j.createFollows(follows)
    # timePostgre += postgre.createFollows(follows)

    timeEndAll = time()
    print("---------------------------------------------------------")
    print("Temps de generation : " + str(timeGenerate) + " s")
    print("Temps d'exécution total Neo4j : " + str(timeNeo4j) + " s")
    print("Temps d'exécution total Postgre : " + str(timePostgre) + " s")
    print("Temps d'exécution total : " + str(timeNeo4j + timePostgre) + " s")
    print("Temps d'exécution total (avec génération ): " +
          str(timeEndAll - timeStartAll) + " s")
    print("---------------------------------------------------------")
    # Close sockets
    postgre.close()
    neo4j.close()