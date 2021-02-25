import psycopg2
from time import time
from pprint import pprint

class PostgreDatabase:
    def __init__(self, dbname, user, password, host):
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')

            self.driver = psycopg2.connect("dbname=" + dbname + " user=" +
                                           user + " password=" + password +
                                           " host=" + host)
            # create a cursor
            cur = self.driver.cursor()


            # close the communication with the PostgreSQL
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close(self):
        self.driver.close()
        print('Database Postgre connection closed.')

    def clear_database(self):
        cur = self.driver.cursor()
        # Clean all
        cur.execute('TRUNCATE personne CASCADE')
        cur.execute('TRUNCATE produit CASCADE')
        cur.execute('TRUNCATE achat CASCADE')
        cur.execute('TRUNCATE follower CASCADE')

    def createPersonnes(self, personnes):
        print("\tPOSTGRES | create personne")
        tic = time()
        cur = self.driver.cursor()
        for personne in personnes:
            cur.execute(
                "INSERT INTO personne (id, first_name, last_name) VALUES(%s, %s, %s)",
                (personne.id, personne.nom, personne.prenom))
        self.driver.commit()
        cur.close()
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")

    def createProduits(self, produits):
        print("\tPOSTGRES | create produit")
        tic = time()
        cur = self.driver.cursor()
        for produit in produits:
            cur.execute(
                "INSERT INTO produit (id_produit, name, price) VALUES(%s, %s, %s)",
                (produit.id, produit.nom, produit.prix))
        self.driver.commit()
        cur.close()
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")

    def createAchats(self, achats):
        print("\tPOSTGRES | create achat")
        tic = time()
        cur = self.driver.cursor()
        for achat in achats:
            cur.execute(
                "INSERT INTO achat (id_achat, id_produit, id_personne) VALUES(%s, %s, %s)",
                (achat.id, achat.idProduit, achat.idPersonne))
        self.driver.commit()
        cur.close()
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")

    def createFollows(self, follows):
        print("\tPOSTGRES | create follow")
        tic = time()
        cur = self.driver.cursor()
        for follow in follows:
            cur.execute(
                "INSERT INTO follower (id_follower, id_followed) VALUES(%s, %s)",
                (follow.idFollower, follow.idFollowed))
        self.driver.commit()
        cur.close()
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")

    def list_achat_products_followers(self, personneID, depth):
        print("\tPOSTGRES | list_achat_products_followers")
        
        request = "SELECT id_followed FROM follower WHERE id_follower = %s"
        for i in range(1, depth):
            request = "SELECT DISTINCT id_followed FROM follower WHERE id_follower IN (" + request + ")"
        request = "SELECT id_produit, count(id_produit) FROM achat WHERE id_personne IN (" + request + ") GROUP BY id_produit"
        tic = time()
        cur = self.driver.cursor()
        cur.execute(request, (personneID,))
        followers_produit = cur.fetchall()
        cur.close()
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")
        return followers_produit

    def list_achat_products_specific_followers(self, personneID, idProduit, depth):
        print("\tPOSTGRES | list_achat_products_specific_followers")
        request = "SELECT id_followed FROM follower WHERE id_follower = %s"
        for i in range(1, depth):
            request = "SELECT DISTINCT id_followed FROM follower WHERE id_follower IN (" + request + ")"
        request = "SELECT id_produit, count(id_produit) FROM achat WHERE id_produit = %s and id_personne IN (" + request + ") GROUP BY id_produit"
        tic = time()
        cur = self.driver.cursor()
        cur.execute(request, (idProduit,personneID,))
        produit = cur.fetchall()
        pprint(produit)
        cur.close()
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")
        return produit
    
    def list_achat_products_specific_followers(self, personneID, idProduit, depth):
        print("\tPOSTGRES | list_achat_products_specific_followers")
        tic = time()
        cur = self.driver.cursor()
        
        request = "SELECT id_followed FROM follower WHERE id_follower = %s"
        for i in range(1, depth):
            request = "SELECT DISTINCT id_followed FROM follower WHERE id_follower IN (" + request + ")"
        request = "SELECT id_produit, count(id_produit) FROM achat WHERE id_produit = %s and id_personne IN (" + request + ") GROUP BY id_produit"
        
        cur.execute(request, (idProduit,personneID,))
        produit = cur.fetchall()
        pprint(produit)
        cur.close()
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")
        return produit