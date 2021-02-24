# from neo4j import GraphDatabase
import neo4j
import json


class Neo4jDatabase:
    def __init__(self, uri, user, password):
        self.driver = neo4j.GraphDatabase.driver(uri, auth=(user, password))
        print("Neo4j connected")

    def close(self):
        self.driver.close()
        print("Neo4j closed")

    def createPersonnes(self, personnes):
        data = []
        for personne in personnes:
            data.append({"prenom": personne.prenom, "nom": personne.nom})
        with self.driver.session() as session:
            result = session.write_transaction(lambda tx: list(tx.run(
            "UNWIND $props AS map "
            "CREATE (n:Personne) SET n = map",
            { "props": data})))
    
    def createProduits(self, produits):
        data = []
        for produit in produits:
            data.append({"prix": produit.prix, "nom": produit.nom})
        with self.driver.session() as session:
            result = session.write_transaction(lambda tx: list(tx.run(
            "UNWIND $props AS map "
            "CREATE (n:Produits) SET n = map",
            { "props": data})))

    def clearDatabase(self):
        with self.driver.session() as session:
            result = session.write_transaction(lambda tx: list(tx.run(
                "MATCH (n) "
                "DELETE n"
                )))