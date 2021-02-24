CREATE TABLE personne (
    id serial NOT NULL,
    first_name VARCHAR(128) NOT NULL,
    last_name VARCHAR(128) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE follower (
    id_follower serial NOT NULL REFERENCES personne(id),
    id_followed serial NOT NULL REFERENCES personne(id),
    PRIMARY KEY (id_follower, id_followed)
);

CREATE TABLE produit (
    id_produit serial NOT NULL,
    name VARCHAR(128) NOT NULL,
    price INTEGER NOT NULL,
    PRIMARY KEY(id_produit)
);

CREATE TABLE achat (
    id_achat serial NOT NULL,
    id_personne serial NOT NULL REFERENCES personne(id),
    id_produit serial NOT NULL REFERENCES produit(id_produit),
    PRIMARY KEY (id_achat)
);

