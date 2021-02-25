import psycopg2
from time import time


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

            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)

            # close the communication with the PostgreSQL
            cur.close()
            cur = self.driver.cursor()
            # Clean all
            cur.execute('TRUNCATE personne CASCADE')

            cur.execute('TRUNCATE produit CASCADE')

            cur.execute('TRUNCATE achat CASCADE')

            cur.execute('TRUNCATE follower CASCADE')

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close(self):
        self.driver.close()
        print('Database Postgre connection closed.')

    def createPersonnes(self, personnes):
        print("\tPOSTGRES | create personne")
        tic = time()
        cur = self.driver.cursor()
        for personne in personnes:
            cur.execute(
                "INSERT INTO personne (id, first_name, last_name) VALUES(%s, %s, %s)",
                (personne.id, personne.nom, personne.prenom))
        self.driver.commit()
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
        toc = time()
        print("\t\tTemps d'exécution : " + str(toc - tic) + " s")
