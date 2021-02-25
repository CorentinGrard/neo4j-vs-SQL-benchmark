from Neo4jDatabase import Neo4jDatabase
from PostgreDatabase import PostgreDatabase

def list_achat_products_followers():
    neo4j.list_achat_products_followers(1,3)
    postgre.list_achat_products_followers(1,3)

def list_achat_products_specific_followers():
    neo4j.list_achat_products_specific_followers(1,1,3)
    postgre.list_achat_products_specific_followers(1,1,3)

def nb_achat_produit():
    neo4j.nb_achat_produit(1,3)
    postgre.nb_achat_produit(1,3)

# Init connection
neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
postgre = PostgreDatabase("database", "admin", "admin", "localhost")

list_achat_products_followers()
list_achat_products_specific_followers()
# nb_achat_produit()

# Close sockets
postgre.close()
neo4j.close()