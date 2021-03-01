def search(personne_id, depth, database):
    print('task a', personne_id, depth, database)
    if database == "postgres":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        followers_produit = postgre.list_achat_products_followers(
            personne_id, depth)
        postgre.close()
        pprint(followers_produit)

    elif database == "neo4j":
        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
        neo4j.close()
    elif database == "pg4j":
        postgre = PostgreDatabase("database", "admin", "admin", "localhost")
        followers_produit = postgre.list_achat_products_followers(
            personne_id, depth)
        postgre.close()
        pprint(followers_produit)

        neo4j = Neo4jDatabase("bolt://localhost:7687", "neo4j", "admin")
        neo4j.close()
    else:
        print("Invalid database argument")