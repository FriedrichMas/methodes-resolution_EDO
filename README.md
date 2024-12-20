# Méthodes-resolution_EDO

## Présentation

Les équations différentielles jouent un rôle crucial dans de nombreuses disciplines scientifiques, donc dans la vie quotidienne, car elles permettent de modéliser des phénomènes dynamiques où des quantités changent au fil du temps ou autre variable. 

En guise d'exemples, nous pouvons citer: 
1. Physique : Modélisation du mouvement (lois de Newton), systèmes thermiques, electromagnétiques...
2. Ingénierie : Contrôle automatique, systèmes mécaniques, électriques ou thermiques...
3. Biologie : Croissance des populations, propagation des maladies...
4. Economie : modèles de croissance économique, évolution des marchers financiers...

Ce pendant, certaines EDO n'ont pas de solution analytique (une formule explicite). D'où l'intérêt d'avoir des méthodes numériques telles que Euler explicite, Euler implicite, Runge-Kutta 4, Cranck-Nicholson, Heun... qui permettent d'approcher numériquement la slution exacte. 

Et sans surprise, ces méthodes n'ont pas la même vitesse de convergence ni la même stabilité. D'où l'objet de ce mini projet : comparer des méthodes de résolution des équation différentilles ordinaires (EDO).
## A propos des méthodes

Sans aller trop dans les détailles, nous allons dire un mot sur chaque méthode que nous allons implémenter. 

soit y' = f(t,y), l'EDO

#Euler explicite
Méthode classique à un pas c'est-à-dire, dans la suite des itérerés, yn+1 ne dépend que de yn. Donnée par la formule: yn+1 = yn + h*f(tn, yn)
avec h = pas de temps. 

Avantages : simple à implémenter et peu coûteux en calcul
Inconvénients : peux précis pour des h grands et instable pour certaines EDO raides. 

#Euler implicite
Donnée par la formule: yn+1 = yn + h*f(tn+1, yn+1)
elle demande à résoudre un système d'équations qui peut-être non-linéaire afin d'obtenir yn+1.

Avantages : plus stable particulièrement adaptée aux EDO raides. 
Inconvénients : plus complexe et coûteux(nécessite des solveurs pour des systèmes no-linéaires)

#RK_4
Utilisant la quadrature de Simpson, elle est donnée par: 
K1 = f(tn, yn)
K2 = f(tn + h/2, yn + h/2 * K1)
K3 = f(tn + h/2, yn + h/2 * K2)
K4 = f(tn + h, yn + h * K3)
yn+1 = yn + h/6 * (K1 + 2K2 + 2K3 + K4)

Avantages : très précis pour des h raisonnables, bonne stabilité sans compléxité excessive. 
Inconvénients : plus coûteux en calcul que les méthodes d'Euler. 


## A propos du code

Nous avons considéré l'EDO y' = -2.y , y(0) = 1
qui a pour solution analytique exp(-2.t)

En utilisant deux librairies python Numpy et Matplotlib.pyplot, nous avons impléter les méthodes et ce code nous renvoie la courbe de la solution analytique (exacte) comparée à celles des méthodes numériques pour différentes valeurs de h. 

Avec h = 0.1
![Capture d’écran h](https://github.com/user-attachments/assets/a6537d14-b955-49c2-a846-cb8c3e83db06)


Avec h = 0.9
![Capture d’écran EDO, h=0 9](https://github.com/user-attachments/assets/a213b41c-d3e4-441b-8c0c-8d3afdba7561)

Nous voyons que RK4 diverge moins par rapport aux Euler et Euler explicite est celle qui diverge le plus. 

## Conclusion

En conclusion, l'utilisation d'une méthode ou d'une autre dépend de la nature de l'équation à approchée, de la précision voulu, du pas de temps considéré ...


## Documentation

Cours magistraux d'analyse numérique II pour Licence 3 Mathématiques d'Anaïs Crestetto, Nantes Université.

