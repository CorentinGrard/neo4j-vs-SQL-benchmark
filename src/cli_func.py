from Neo4jDatabase import Neo4jDatabase
from PostgreDatabase import PostgreDatabase
from generate_data import *

import names
import random
from random_word import RandomWords
from time import time

def search(personne_id, depth, database):
    print('task a', personne_id, depth, database)
    if database == "postgres":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        followers_produit = postgre.list_achat_products_followers(
            personne_id, depth)
        postgre.close()
        pprint(followers_produit)

    elif database == "neo4j":
        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
        followers_produit = neo4j.list_achat_products_followers(
            personnes_id, depth)
        neo4j.close()
        pprint(followers_produit)
    elif database == "pg4j":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        followers_produit = postgre.list_achat_products_followers(
            personne_id, depth)
        postgre.close()
        pprint(followers_produit)
       
        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
        followers_produit = neo4j.list_achat_products_followers(
            personnes_id, depth)
        neo4j.close()
        pprint(followers_produit)
    else:
        print("Invalid database argument")


def searchproduct(personne_id, produit_id,depth, database):
    if database == "postgres":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        produits = postgre.list_achat_products_specific_produits(personnes_id, produit_id, depth)
        postgre.close()
        pprint(produits)
    elif database == "neo4j":
        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
        produits = neo4j.list_achat_products_specific_produits(personnes_id, produit_id, depth)
        neo4j.close()
        pprint(produits)
    elif database == "pg4j":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        produits = postgre.list_achat_products_specific_produits(personnes_id, produit_id, depth)
        postgre.close()
        pprint(produits)
        
        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
        produits = neo4j.list_achat_products_specific_produits(personnes_id, produit_id, depth)
        neo4j.close()
        pprint(produit)
    else:
        print("Invalid database argument")

def circle(produit_id, depth, database):
    if database == "postgres":
        print("Invalid database argument")
    elif database == "neo4j":
        print("Invalid database argument")
    elif database == "pg4j":
        print("Invalid database argument")
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

    # Generate data
    # Generate personnes
    print("---------------------------------------------------------")
    print("Génération des personnes....")
    tic = time()
    personnes = generate_personne(number_personne)
    toc = time()
    temps = toc - tic
    print("\t\tTemps d'exécution : " + str(temps) + " s")
    print("Génération des personnes - DONE")

    timeNeo4j += neo4j.createPersonnes(personnes)
    timePostgre += postgre.createPersonnes(personnes)

    # Generate produits
    print("---------------------------------------------------------")
    print("Génération des produits....")
    tic = time()
    produits = generate_produit(number_produit)
    toc = time()
    temps = toc - tic
    print("\t\tTemps d'exécution : " + str(temps) + " s")
    print("Génération des produits - DONE")

    timeNeo4j += neo4j.createProduits(produits)
    timePostgre += postgre.createProduits(produits)

    # Generate achats
    print("---------------------------------------------------------")
    print("Génération des achats....")
    tic = time()
    achats = generate_achat(personnes, produits, number_produit)
    toc = time()
    temps = toc - tic
    print("\t\tTemps d'exécution : " + str(temps) + " s")
    print("Génération des achats - DONE")

    timeNeo4j += neo4j.createAchats(achats)
    timePostgre += postgre.createAchats(achats)

    # Generate follows
    print("---------------------------------------------------------")
    print("Génération des follows....")
    tic = time()
    follows = generate_follow(personnes, number_personne)
    toc = time()
    temps = toc - tic
    print("\t\tTemps d'exécution : " + str(temps) + " s")
    print("Génération des follows - DONE")

    timeNeo4j += neo4j.createFollows(follows)
    timePostgre += postgre.createFollows(follows)

    timeEndAll = time()
    print("---------------------------------------------------------")
    print("Temps d'exécution total Neo4j : " + str(timeNeo4j) + " s")
    print("Temps d'exécution total Postgre : " + str(timePostgre) + " s")
    print("Temps d'exécution total : " + str(timeNeo4j + timePostgre) + " s")
    print("Temps d'exécution total (avec génération ): " +
          str(timeEndAll - timeStartAll) + " s")
    print("---------------------------------------------------------")
    # Close sockets
    postgre.close()
    neo4j.close()