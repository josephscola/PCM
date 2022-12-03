#!/usr/bin/env python
# coding: utf-8

# # Modèle des liaisons fortes 

# ## Limites forte et faible de l'intéraction électron-réseau
# Dans l'approche de l'électron presque libre, le potentiel est supposé suffisamment faible pour être considéré comme une légère perturbation de l'électron tout à fait libre.
# Les électrons sont d'autant plus libres (relation de dispersion parabolique, $\mathcal{E} \propto k^2$) que la norme de leur vecteur d'onde est petite par rapport à la première zone de Brillouin ($\Vert \vec{k} \Vert \ll \frac{\pi}{a}$).
# Autrement dit, l'influence du réseau sur les électrons est d'autant plus faible que leur longueur d'onde est grande devant le pas du réseau ($\lambda \gg a$).
# 
# Au contraire, l'approche des liaisons fortes (*tight binding model*) postule que le potentiel atomique est la contribution principale de l'énergie des électrons. 
# On suppose que les électrons sont aussi fortement liés à leur atome que si chaque atome du cristal était isolé;  ce sont les interactions avec les atomes voisins qui sont considérés comme des perturbations subies par les électrons dans leurs orbitales atomiques.
# Cette approche est valide lorsque le paramètre de maille $a$ s'étend : les conditions pour que les électrons soient libres sont de plus en plus restrictives et le potentiel est de moins en moins négligeable.
# De fait, plus les atomes sont éloignés les uns des autres, plus il est réaliste de les considérer comme des atomes isolés; il suffit d'imaginer un cristal dont le paramètre de maille est de l'ordre du kilomètre !

# ## Description du potentiel du réseau
# Dans ces conditions, le potentiel $V$ du réseau s'exprime comme la répétition, sur chaque site $\vec{T}$ du réseau, du potentiel électrostatique créé par les noyaux vus comme des charges ponctuelles $q$ : 
# 
# $$
# V (\vec{r}) = \sum_{\vec{T}} \frac{q}{4\pi\varepsilon_0 \Vert \vec{r} - \vec{T} \Vert}
# $$

# La fonction $V (\vec{r})$ possède par construction la périodicité du réseau.
# Elle peut donc s'exprimer comme la superposition de fonctions périodiques dans chaque direction ($x$, $y$, $z$) de l'espace :
# 
# $$
# V (x) = \sum_{n\ge 1} g_n \cos \left( n\frac{2\pi}{a}x \right).
# $$
# 
# En effet, en première approximation, le potentiel périodique considéré comme une oscillation sinusoïdale de période $a$.
# Les termes d'ordre supérieurs ($n\ge 2$) sont périodique de période $a/n$, ce qui conserve la périodicité de période $a$. 
# Ces termes apportent des corrections de plus en plus fines à cette approximation jusqu'à faire tendre la série vers la fonction originale, éventuellement à la limite $n\rightarrow \infty$ (c'est la *décomposition en série de Fourier*).

# Dans sa version complexe (décomposition en ondes planes), cette série prend la forme suivante :
# 
# $$
# V (x) = \sum_{n\in \mathbb{Z}} G_n e^ { in\frac{2\pi}{a}x }.
# $$

# 

# Parmi toutes les solutions de l'équation de Schroëdinger intégrant le potentiel $V$ du réseau, on recherche celles qui :
# - ont un comportement ondulatoire décrit par leur vecteur d'onde $\vec{k}$
# - sont susceptibles de s'éteindre avec la distance à un atome (celui dont l'électron est issu)
# - possèdent la périodicité du réseau
# 
# La combinaison de ces 3 critères conduit à rechercher des fonctions d'onde de la forme :
# $\psi (\vec{r}) = e^{i\vec{k}\cdot \vec{x}} \phi (\vec{r})$ où $\phi$ est une fonction qui tend vers zéro à l'infini.
# 
# 
# $$
# \psi (\vec{r} + \vec{T}) = \psi (\vec{r})
# $$
# 
# $$
# \psi_\vec{k} (\vec{r} + \vec{T}) = e^{i\vec{k}\cdot \vec{T}} \psi_\vec{k} (\vec{r})
# $$

# Etats électroniques 
# 
# $$
# \psi (\vec{r}) = \sum_{\vec{T}} a_{\vec{k},\vec{T}} \phi_j (\vec{r} + \vec{T})
# $$
# 
# où $\phi_j$ est une orbitale atomique.
# 

# Intégrales de transfert

# ![Hydrogen_orbitals](./Atomic_orbitals_n123_m-eigenstates.png)
# 
# By Geek3 - Own work, Created with hydrogen 1.1, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=67681892
# 
