# pyMontyHall

Ce script Python simule le jeu de Monty Hall, un problème de probabilité célèbre. Le jeu consiste en ce qui suit :

1. Il existe 3 portes (*nombre modifiable*), une seule est gagnante, les autres sont perdantes
2. Le joueur fait un choix de porte parmi les portes sans le découvrir
3. Le présentateur ouvre une porte (*aléatoirement ou non, modifiable*) et la montre au joueur 
     - La porte ne peut pas être gagnante si le présentateur ne la choisit pas aléatoirement. On suppose que dans le cas où le présentateur ne choisit pas la porte aléatoirement, il connait l'emplacement de la porte gagnante et donc ne la choisit pas.
4. Le présentateur propose au joueur de changer son choix initial, et de choisir une autre porte
     - Dans le cas où le présentateur choisit la porte aléatoirement, il est possible qu'il tombe sur la porte gagnante, auquel cas le jeu s'arrète et le joueur a perdu
5. Le joueur peut modifier son choix initial, ou non (*modifiable*)
6. Le joueur est gagnant ou non

### Le script permet de simuler plusieurs jeux avec différentes options :

- Jeu **sans changement de porte** et **sans choix aléatoire** du présentateur.
- Jeu **avec changement de porte** et **sans choix aléatoire** du présentateur.
- Jeu **sans changement de porte** et **avec choix aléatoire** du présentateur.
- Jeu **avec changement de porte** et **avec choix aléatoire** du présentateur.

### Modification des paramètres : 

Assurez-vous de modifier les variables suivantes dans le script selon vos préférences :

- `nb_portes` : Nombre de portes dans le jeu.
- `nb_jeux` : Nombre de jeux à effectuer.

La fonction principale est la suivante : 

```python
jeu(nb_portes, nb_jeux, joueur_change, aleatoire_presentateur)
```
Avec les arguments suivants : 

- `nb_portes` (int) : le nombre de portes dans le jeu
- `nb_jeux` (int) : le nombre de jeux à effectuer
-  `joueur_change` (bool) : Si le joueur change son choix initial
-  `aleatoire_presentateur` (bool) : Si le présentateur choisit la porte aléatoirement

## Exécution :

`python main.py`

![https://github.com/Gyrfalc0n/pyMontyHall/blob/main/result.png](https://github.com/Gyrfalc0n/pyMontyHall/blob/main/result.png)
 
