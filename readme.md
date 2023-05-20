>  :tv: Informations avec Thésée sur la SAÉ23

| Module       | Enseignant       | Fichiers                                                              |
| :---         |    :----         |          :---                                                         |
| saé23        | Munier           | [Cours de Munier](https://munier.perso.univ-pau.fr/temp/SAE23/)       |
 

## Sujet

Informations sur ce qui est demandé dans cette SAÉ.

# first practice

## first marks w/ sql

### 1. easy queries

- [x] (a) noms des fournisseurs situés à Paris
```sql
  select nomfour from fournisseur where (origine = 'Paris');
```

- [x] (b) numéros des produits provenant de Paris et dont le poids est supérieur ou égal à 0.3
```sql
select nomprod from produit where (origine = 'Paris') and (poids >= 0.3);
```

- [x] (c) idem précédent, mais triés par poids décroissant
```sql
select nomprod from produit where (origine = 'Paris') and (poids >= 0.3) order by poids desc;
```

- [x] (e) correspondance entre les numéros de produits de la même ville
```sql
select distinct a.numprod, b.numprod 
from produit a, produit b 
where (A.origine = b.origine) and (a.numprod < b.numprod);
```
dernière condition car distinct ne peut pas fonctionner +
inférieur strict ou supérieur strict pour garder que l'un des deux (mêmes)

- [x] (f) noms des produits dont le numéro est p1, p2, p3 ou p4
```sql
select nomprod from produit where (numprod <= 'p4');
```
```sql
select nomprod from produit where numprod in ('p1', 'p2', 'p3', 'p4');
```

### 2. subqueries

- [x] (a) noms des fournisseurs ayant livré des produits de couleur rouge
```sql
select nomfour 
from fournisseur 
where numfour 
in (select numfour from stock where numprod 
in (select numprod from produit where (couleur = 'rouge')));
```

- [x] (b) noms des fournisseurs ayant livré le produit p2
```sql
select nomfour 
from fournisseur 
where numfour 
in (select numfour from stock where (numprod = 'p2'));
```

- [x] (c) numéros des fournisseurs ayant livré au moins un article identique à ceux livrés par f2
```sql
select distinct numfour 
from stock 
where numprod 
in (select numprod from stock where (numfour = 'f2'));
```

- [x] (d) numéros des produits originaires de la même ville que p1
```sql
select numprod 
from produit 
where origine 
in (select origine from produit where (numprod = 'p1'));
```

### 3. "exists" and "not exists"

- [x] (a) noms des fournisseurs ayant livré le produit p2
```sql
select nomfour 
from fournisseur 
where exists (select a.numfour from stock a where (numprod = 'p2') 
and fournisseur.numfour = a.numfour);
```

- [x] (b) noms des fournisseurs n'ayant pas livré le produit p2
```sql
select nomfour 
from fournisseur 
where not exists (select a.numfour from stock a where (numprod = 'p2') 
and fournisseur.numfour = a.numfour);
```

- [ ] (c) noms des fournisseurs tels qu'il n'y ait pas de produit qu'ils n'aient pas livré (. . .)
```sql
select distinct a.numfour, b.numprod from stock a, stock b where (a.numprod = b.numprod) order by a.numfour asc;
```
liste des fournisseurs et de leur produits livrés


### 4. "group by" and "having"

- [x] (a) total des quantités livrées pour chaque produit
```sql
select numprod, sum(qte) from stock group by numprod;
```

- [x] (b) idem précédent, mais p1 non pris en compte
```sql
select numprod, sum(qte) from stock where numprod > 'p1' group by numprod;
```
fallait faire avec un count

- [x] (c) numéros des fournisseurs ayant livré au moins deux produits
```sql
select nomfour 
from fournisseur 
where numfour 
in (select numfour from stock group by numfour having count(*) >= 2);
```
## more querries

- [ ] (a) numéros des produits livrés par plus d'un fournisseur (donner 3 solutions différentes)
- [ ] (b) numéros des fournisseurs ayant livré au moins tous les produits livrés par f2
- [ ] (c) numéro, nom et poids du produit le plus lourd de la liste
- [ ] (d) numéro, nom et poids de tous les produits pour lesquels il existe au moins un produit plus léger dans la liste
- [ ] (e) numéros des fournisseurs dont la remise est strictement inférieure à la remise maximale
- [ ] (f ) numéros des produits (ainsi que leur poids et leur origine) dont le poids est supérieur ou égal au poids moyen des produits originaires de la même ville
- [ ] (g) total des quantités livrées pour chaque pro duit
- [ ] (h) numéros des produits ayant été livrés au moins un fois (donner 3 solutions différentes)
- [ ] (i) pour tous les produits rouges ou bleus dont la quantité totale livrée est supérieure à 350 (en excluant du total les commandes dont la quantité est inférieure à 200), donner le numéro du produit, le poids en pounds (sachant qu'une livre vaut 450 grammes), la couleur et la plus grande
quantité livrée pour ce produit
- [ ] (j) liste des couples de nom de fournisseurs installés dans la même ville et ayant livré au moins un produit identique
- [ ] (k) commande SQL permettant de rajouter une colonne PU (prix unitaire) dans la table Produit
- [ ] (l) valeur marchande du stock pour chacun des fournisseurs (avec leur nom)
- [ ] (m) dans la table Produit, convertir le poids des articles en livres (pounds)
- [ ] (n) supprimer tous les founisseurs n'ayant pas livré le moindre produit

1.
Afficher le nom de étudiants avec au moins une absence à tous les cours
```sql
select nomEtud from Etudiants where idEtud in (select distinct IdEtud from absence group by idEtud having count(absence.idCours) = (select count(*) from cours));```
(donne le nom des étudiants pour lequels sans doublon le nombre de leur absence à chaque cours vaut le nombre total de cours)

version julien sur discord
```sql
select nomEtud from Etudiant where not exists (select idCours from Cours where not exists (select * from absence where (etudiant.idetud = absence.idetud) and (cours.idCours = absence.idCours))))```

2.
Afficher le nom des étudiants et leur nombre d'absence pour chaque étudiant
```sql
select nomEtud, from Etudiants where ```


3.
Afficher la date où Elsa a été absente sans utiliser idEtud = ...
```sql
select dateAbsence from Absence, Etudiant where (absence.NomEtud = "Elsa") and (Absence.id = Etudiant.id);
```

4.
Nom de tous les étudiants avec aucune absence
```sql
select nomEtud from Etudiant where idEtudiant not in (select idEtudient from absence);
```
