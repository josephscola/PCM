#!/usr/bin/env python
# coding: utf-8

# # Combinaison linéaire d'orbitales atomiques

# Parmi toutes les solutions de l'équation de Schroëdinger intégrant le potentiel $V$ du réseau, on recherche celles qui vérifient des critères issus de l'observation et des hypothèses du modèle.
# 
# 1. **électrons fortment liés** : comme on considère que les électrons sont fortement liés à leur atome, leurs états accessibles sont les orbitales atomiques de chaque atome de l'édifice cristallin, dont l'amplitude (densité de probabilité de présence électroniques) est concentré au voisinage du noyau et décroît rapidement avec la distance. Leurs fonctions d'onde sont des superposition, c'est-à-dire des combinaisons linéaires, d'orbitales atomiques issus des atomes du cristal. On choisira en priorité la dernière orbitale occupée $n$.
# 2. **comportement ondulatoire** : les fonctions d'onde doivent présenter un comportement ondulatoire afin de rendre compte de l'éventuelle propagation des ondes électroniques, lorsque les conditions le permettent. 
# 3. **périodicité du résseau** : les fonctions d'onde des électrons mobiles doivent avoir la périodicité du réseau. L'invariance des états par translation selon un vecteur du réseau s'écrit $\psi (x + ma) = \psi (x), \quad \forall m \in \mathbb{Z} $.
# 
# Prises ensemble, les deux premières conditions conduisent à rechercher des superpositions d'états orbitaux pour chacun des $N$ sites atomiques de la forme :
# 
# $$
# \psi_m (x) = e^{ikx} \Psi_{n} (x - ma), \quad m,p \in \mathbb{Z}
# $$
# 
# où le vecteur d'onde est imposé par les conditions limites : $k = p\frac{2\pi}{Na}, p \in \mathbb{Z}$.
# 
# Finalement, compte tenu de la périodicité des fonctions d'onde héritée du réseau atomique, la superposition d'états s'écrit :
# $$
# \psi_m (x) = e^{ikma} \psi_0 (x+ma)
# $$
#  
# $$
# \psi (x) \equiv \sum_{m=1}^{N} \psi_m = \sum_{m=1}^{N} e^{ikma} \psi_0 (x+ma),\quad m \in \mathbb{Z}
# $$
# 
# En tenant compte de la périodicité des fonctions d'onde, ces états s'écrivent à partir de l'orbitale de l'atome origine :
# 
# 
# 
