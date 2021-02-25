²²²²²²²²²²²²²²# from neo4j import GraphDatabase
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

    # Génération

    def clearDatabase(self):
        with self.driver.session() as session:
            session.write_transaction(
                lambda tx: list(tx.run("MATCH (n) "
                                       "DETACH DELETE n")))

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
            session.write_transaction(lambda tx: list(
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
            session.write_transaction(lambda tx: list(
                tx.run(
                    "UNWIND $props AS map "
                    "CREATE (n:Produit) SET n = map", {"props": data})))
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")

    def createAchats(self, achats):
        print("\tNEO4J | create achat")
        data = []
        for achat in achats:
            data.append({
                "idPersonne": achat.idPersonne,
                "idProduit": achat.idProduit,
            })
        tic = time()
        for pos in range(0, len(data), 1000):
            with self.driver.session() as session:
                session.write_transaction(lambda tx: list(
                    tx.run(
                        "UNWIND $props AS row "
                        "MATCH (a:Personne), (b:Produit) "
                        "WHERE a.id = row.idPersonne AND b.id = row.idProduit "
                        "CREATE (a)-[r:Achat]->(b)", {"props": data[pos:pos + 1000]})))
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
        for pos in range(0, len(data), 1000):
            with self.driver.session() as session:
                session.write_transaction(lambda tx: list(
                    tx.run(
                        "UNWIND $props AS row "
                        "MATCH (a:Personne), (b:Personne) "
                        "WHERE a.id = row.idFollower AND b.id = row.idFollowed "
                        "CREATE (a)-[r:Follow]->(b)", {"props": data[pos:pos + 1000]})))
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")

    # Search

    def list_achat_products_followers(self, idPersonne, profondeur):
        print("\tNEO4J | list_achat_products_followers")
        tic = time()
        with self.driver.session() as session:
            result = session.write_transaction(lambda tx: list(
                tx.run(
                    "MATCH (a:Personne{id:$idPersonne})-[:Follow*.." + str(
                        profondeur) + "]->(b:Personne)-[:Achat]->(p:Produit) "
                    "WITH DISTINCT b, p ORDER BY p.id "
                    "RETURN p.id, COUNT(b)", {
                        "idPersonne": idPersonne,
                    })))
        toc = time()
        # print(result)
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")

    def list_achat_products_specific_followers(self, idPersonne, idProduit, profondeur):
        print("\tNEO4J | list_achat_products_specific_followers")
        tic = time()
        with self.driver.session() as session:
            result = session.write_transaction(lambda tx: list(
                tx.run(
                    "MATCH (a:Personne{id:$idPersonne})-[:Follow*.." + str(
                        profondeur) +
                    "]->(b:Personne)-[:Achat]->(p:Produit{id:$idProduit}) "
                    "WITH DISTINCT b, p ORDER BY p.id "
                    "RETURN p.id, COUNT(b)", {
                        "idPersonne": idPersonne,
                        "idProduit": idProduit,
                    })))
        toc = time()
        print(result)
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")

    def nb_achat_produit(self, idProduit, profondeur):
        print("\tNEO4J | nb_achat_produit")
        tic = time()
        with self.driver.session() as session:
            result = session.write_transaction(lambda tx: list(
                tx.run(
                    "MATCH (p:Produit{id:1})<-[:Achat]-(a:Personne)<-[:Follow*.."
                    + str(profondeur) + "]-(b:Personne) "
                    "WITH DISTINCT b "
                    "RETURN COUNT(b)", {
                        "idProduit": idProduit,
                    })))
        toc = time()
        print(result)
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")