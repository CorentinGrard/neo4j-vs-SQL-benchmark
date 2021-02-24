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
            data.append({
                "id": personne.id,
                "prenom": personne.prenom,
                "nom": personne.nom
            })
        with self.driver.session() as session:
            result = session.write_transaction(lambda tx: list(
                tx.run(
                    "UNWIND $props AS map "
                    "CREATE (n:Personne) SET n = map", {"props": data})))

    def createProduits(self, produits):
        data = []
        for produit in produits:
            data.append({
                "id": produit.id,
                "prix": produit.prix,
                "nom": produit.nom
            })
        with self.driver.session() as session:
            result = session.write_transaction(lambda tx: list(
                tx.run(
                    "UNWIND $props AS map "
                    "CREATE (n:Produit) SET n = map", {"props": data})))

    def clearDatabase(self):
        with self.driver.session() as session:
            result = session.write_transaction(
                lambda tx: list(tx.run("MATCH (n) "
                                       "DETACH DELETE n")))

    def createAchats(self, achats):
        for achat in achats:
            with self.driver.session() as session:
                result = session.write_transaction(lambda tx: list(
                    tx.run(
                        "MATCH (a:Personne), (b:Produit) "
                        "WHERE a.id = $idPersonne AND b.id = $idProduit "
                        "CREATE (a)-[r:Achat]->(b)", {
                            "idPersonne": achat.idPersonne,
                            "idProduit": achat.idProduit
                        })))

    def createFollows(self, follows):
        for follow in follows:
            with self.driver.session() as session:
                result = session.write_transaction(lambda tx: list(
                    tx.run(
                        "MATCH (a:Personne), (b:Personne) "
                        "WHERE a.id = $idFollower AND b.id = $idFollowed "
                        "CREATE (a)-[r:Follow]->(b)", {
                            "idFollower": follow.idFollower,
                            "idFollowed": follow.idFollowed
                        })))
