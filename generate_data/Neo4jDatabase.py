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
        data = {
            'props': []
        }
        for personne in personnes:
            data["props"].append({"prenom": personne.prenom, "nom": personne.nom})
        with self.driver.session() as session:
            result = session.write_transaction(self._create_personnes, data)
            print(result)

    @staticmethod
    def _create_personnes(tx, data):
        result = tx.run(
            "UNWIND $props AS map"
            "CREATE (n:Personne) SET n = map",
            props=data)
        return result