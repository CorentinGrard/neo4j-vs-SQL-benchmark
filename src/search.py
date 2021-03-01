from Neo4jDatabase import Neo4jDatabase
from PostgreDatabase import PostgreDatabase


def list_achat_products_followers():
    print("---------------------------------------------------------")
    neo4j.list_achat_products_followers(1, 7)
    postgre.list_achat_products_followers(1, 7)


def list_achat_products_specific_followers():
    print("---------------------------------------------------------")
    neo4j.list_achat_products_specific_followers(1, 1, 7)
    postgre.list_achat_products_specific_followers(1, 1, 7)


def nb_achat_produit():
    print("---------------------------------------------------------")
    neo4j.nb_achat_produit(1, 7)
    postgre.nb_achat_produit(1, 7)


# Init connection
neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
postgre = PostgreDatabase("database", "admin", "admin", "localhost")

list_achat_products_followers()
list_achat_products_specific_followers()
# nb_achat_produit()

# Close sockets
postgre.close()
neo4j.close()
