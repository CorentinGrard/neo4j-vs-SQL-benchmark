import argparse

def search(type_object, property_search, database):
    print('task a', type_object, property_search)


def add_user(beta):
    print('', beta)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subparser')

parser_search = subparsers.add_parser('search')
parser_search.add_argument('-o', '--object', dest='type_object', help="Type d'object de la recherche.", type=string)
parser_search.add_argument('-p', '--property', dest='property_search', help="Propriété recherché, exemple nom=Patrick", type=string)
parser_search.add_argument('-d', '--database', dest='database', help="nom de la database", type=string)



kwargs = vars(parser.parse_args())
globals()[kwargs.pop('subparser')](**kwargs)