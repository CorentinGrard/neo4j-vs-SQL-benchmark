import argparse
from pprint import pprint
from Neo4jDatabase import Neo4jDatabase
from PostgreDatabase import PostgreDatabase
from cli_func import *

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subparser')

parser_search = subparsers.add_parser(
    'search', help="Recherche en profondeur des followers d'une personne")
parser_search.add_argument('-pid', '--personneid', dest='personne_id',
                           help="ID de la personne recherché", type=str)
parser_search.add_argument('-de', '--depth', dest='depth',
                           help="Profondeur de la recherche", default=1, type=int)
parser_search.add_argument('-d', '--database', dest='database', help="nom de la database",
                           type=str, choices=['postgres', 'neo4j', 'pg4j'], default="pg4j")


parser_gendata =  subparsers.add_parser(
    'gendata', help="détruit la BDD et construit n éléments de produits/personnes")
parser_gendata.add_argument('-np', '--numberPersonne', dest='number_personne',
                           help="Nombre de personnes à générer", default=100000, type=int)
parser_gendata.add_argument('-npr', '--numberProduit', dest='number_produit',
                           help="Nombre de produits à générer", default=10000, type=int)


parser_searchproduct = subparsers.add_parser(
    'searchproduct', help="Permet de rechercher les produits viraux jusqu'à profonder de")
parser_searchproduct.add_argument('-pid', '--personneid', dest='personne_id',
                           help="ID de la personne recherché", type=str)
parser_searchproduct.add_argument('-prid', '--produitid', dest='produit_id',
                           help="ID du produit", type=str)
parser_searchproduct.add_argument('-de', '--depth', dest='depth',
                           help="Profondeur de la recherche", default=1, type=int) 
parser_searchproduct.add_argument('-d', '--database', dest='database', help="nom de la database",
                           type=str, choices=['postgres', 'neo4j', 'pg4j'], default="pg4j")



parser_circle = subparsers.add_parser(
    'circle', help="Observe le rôle d'influenceur d'un individu suite à un post mentionnant un article")
parser_circle.add_argument('-prid', '--produitid', dest='produit_id',
                           help="ID du produit", type=str)
parser_circle.add_argument('-de', '--depth', dest='depth',
                           help="Profondeur de la recherche", default=1, type=int) 
parser_circle.add_argument('-d', '--database', dest='database', help="nom de la database",
                           type=str, choices=['postgres', 'neo4j', 'pg4j'], default="pg4j")




kwargs = vars(parser.parse_args())
globals()[kwargs.pop('subparser')](**kwargs)
