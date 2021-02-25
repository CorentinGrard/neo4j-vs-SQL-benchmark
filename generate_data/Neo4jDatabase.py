# from neo4j import GraphDatabase
import neo4j
import json
from time import time


class Neo4jDatabase:
    def __init__(self, uri, user, password):
        self.driver = neo4j.GraphDatabase.driver(uri, auth=(user, password))
        print("Neo4j connected")

    def close(self):
        self.driver.close()
        print("Neo4j closed")

    def createPersonnes(self, personnes):
        print("\tNEO4J | create personne")
        data = []
        for personne in personnes:
            data.append({
                "id": personne.id,
                "prenom": personne.prenom,
                "nom": personne.nom
            })
        tic = time()
        with self.driver.session() as session:
            result = session.write_transaction(lambda tx: list(
                tx.run(
                    "UNWIND $props AS map "
                    "CREATE (n:Personne) SET n = map", {"props": data})))
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")

    def createProduits(self, produits):
        print("\tNEO4J | create produit")
        data = []
        for produit in produits:
            data.append({
                "id": produit.id,
                "prix": produit.prix,
                "nom": produit.nom
            })
        tic = time()
        with self.driver.session() as session:
            result = session.write_transaction(lambda tx: list(
                tx.run(
                    "UNWIND $props AS map "
                    "CREATE (n:Produit) SET n = map", {"props": data})))
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")

    def clearDatabase(self):
        with self.driver.session() as session:
            result = session.write_transaction(
                lambda tx: list(tx.run("MATCH (n) "
                                       "DETACH DELETE n")))

    def createAchats(self, achats):
        print("\tNEO4J | create achat")
        data = []
        for achat in achats:
            data.append({
                "idPersonne": achat.idPersonne,
                "idProduit": achat.idProduit,
            })
        tic = time()
        with self.driver.session() as session:
            result = session.write_transaction(lambda tx: list(
                tx.run(
                    "UNWIND $props AS row "
                    "MATCH (a:Personne), (b:Produit) "
                    "WHERE a.id = row.idPersonne AND b.id = row.idProduit "
                    "CREATE (a)-[r:Achat]->(b)", {"props": data})))
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")

    def createFollows(self, follows):
        print("\tNEO4J | create follow")
        data = []
        for follow in follows:
            data.append({
                "idFollower": follow.idFollower,
                "idFollowed": follow.idFollowed,
            })
        tic = time()
        with self.driver.session() as session:
            result = session.write_transaction(lambda tx: list(
                tx.run(
                    "UNWIND $props AS row "
                    "MATCH (a:Personne), (b:Personne) "
                    "WHERE a.id = row.idFollower AND b.id = row.idFollowed "
                    "CREATE (a)-[r:Follow]->(b)", {"props": data})))
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")
