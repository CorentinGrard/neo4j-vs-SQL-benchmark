import argparse
from pprint import pprint
from Neo4jDatabase import Neo4jDatabase
from PostgreDatabase import PostgreDatabase


def search(personne_id, depth, database):
    print('task a', personne_id, depth, database)
    if database == "postgres":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        followers_produit = postgre.list_achat_products_followers(personne_id, depth)
        postgre.close()
        pprint(followers_produit)
        
    elif database == "neo4j":
        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
        neo4j.close()
    elif database == "pg4j":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        followers_produit = postgre.list_achat_products_followers(personne_id, depth)
        postgre.close()
        pprint(followers_produit)
        
        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
        neo4j.close()
    else:
        print("Invalid database argument")


def add_user(beta):
    print('', beta)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subparser')

parser_search = subparsers.add_parser('search', help="Recherche en profondeur des followers d'une personne")
parser_search.add_argument('-pid', '--personneid', dest='personne_id', help="ID de la personne recherché", type=str)
parser_search.add_argument('-de', '--depth', dest='depth', help="Profondeur de la recherche", default=1, type=int)
parser_search.add_argument('-d', '--database', dest='database', help="nom de la database", type=str, choices=['postgres', 'neo4j', 'pg4j'], default="pg4j")



kwargs = vars(parser.parse_args())
globals()[kwargs.pop('subparser')](**kwargs)