import psycopg2


class PostgreDatabase:
    def __init__(self, uri, user, password):
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')

            self.driver = psycopg2.connect("dbname=database user=admin password=admin host=localhost")

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
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close(self):
        self.driver.close()
        print('Database Postgre connection closed.')

    def createPersonnes(self, personnes):
        cur = self.driver.cursor()
        for personne in personnes:
            cur.execute("INSERT INTO personne (first_name, last_name) VALUES(%s, %s)", (personne.nom, personne.prenom))
            self.driver.commit()

    def createProduits(self, produits):
        cur = self.driver.cursor()
        for produit in produits:
            cur.execute("INSERT INTO produit (name, price) VALUES(%s, %s)", (produit.nom, produit.prix))
            self.driver.commit()