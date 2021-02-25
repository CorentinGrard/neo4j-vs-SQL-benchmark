1) Optimiser les inserts V
1b) Ajout TIMING INSERT V
2) Faire le rapport ~
3) Faire le CLI ~ 
4) Faire les requetes de recherche en statique
5) Faire les requetes de recherche en dynamique

Obtenir la liste et le nombre des produits commandés par les cercles de followers d’un individu (niveau 1, ..., niveau n)

Même requête mais avec spécification d’un produit particuliercette requête permet d’observer le rôle d’influenceur d’un individusuite à un «post» mentionnant un article spécifique

Pour une référence de produit donné, obtenir le nombre de personnes l’ayant commandé dans un cercle de followers«orienté» de niveau n (à effectuer sur plusieurs niveaux: 0, 1, 2 ...)


./cli.py search -o Personne -p nom=Patrick -d postgres
./cli.py search -o Personne -p nom=Patrick -d postgres
./cli.py generate