# EX3, Probabilité pour un joueur

Dans un univers parallèle, il existe n éléments chimiques, numérotés de 1 à n.
L'élément numéro n n'a pas encore été découvert, et sa découverte constituerait un sommet de la recherche et apporterait à son auteur une gloire éternelle et le prix dit "j'ai eu l'exo B".
Un chercheur solitaire (Alice) tente de découvrir cet élément.
Actuellement, il dispose d'un échantillon de l'élément 0.
Chaque année, il effectue indépendamment une expérience de fusion.
Lors d'une expérience de fusion, si le chercheur dispose actuellement d'un échantillon de l'élément a, il produit un échantillon d'un élément b qui est choisi uniformément au hasard entre a + 1 et n, et il perd l'échantillon de l'élément a.
Le chercheur recevra le prix "j'ai un exo intermédiaire" s'il parvient à découvrir l'élément k.
Vous devez calculer la probabilité que le chercheur découvre l'élément k et remporte le prix en x année.

## Input
```
n le nombre d'éléments,
k position initial,
x le nombre d'année 
```
## Output
```
La probabilité de trouver l'élément b en n essais
```


