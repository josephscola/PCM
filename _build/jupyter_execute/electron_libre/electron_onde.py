#!/usr/bin/env python
# coding: utf-8

# # Chapitre 1 : Electrons libres
# Qu'est-ce que la conduction métallique ?

# ## Décrire le comportement d'un électron comme une onde

# Durant le XIXème siècle se sont accumulées des preuves expérimentales  montrant tantôt le comportement ondulatoire de la lumière, tantôt son comportement corpusculaire.
# 
# Au début du XXème siècle, De Broglie propose de généraliser le mouvement de tout corps ayant une énergie $E$ et une quantité de mouvement $\vec{p}$ à celui d'une onde de fréquence $\nu$ et de longueur d'onde $\lambda$.:
# 
# $$
# \left\{
# \begin{align}
# E &= h\nu \\
# p &= h/\lambda
# \end{align}
# \right.
# $$
# 
# avec $h = 6.6263\cdot 10^{-34}$ J$\cdot$s représente la constante de Planck.
# 
# En pratique cette description ne s'applique qu'à des particules de masse voisine de celles d'un électron.
# Pour des masses supérieures, les longueurs d'onde correspondantes n'ont pas de sens.
# 
# E. Schödinger (Physicien autrichien) postule une formulation générale du mouvement ondulatoire d'une telle particule sur la base du formalisme mathématique récemment établi pour les ondes.
# 
# L'état de la particule, _i.e._ son mouvement, est réprésenté par une onde, par exemple plane propagative :
# 
# $$
# \psi (\vec{r}, t) = A e^{i(\vec{k}\cdot\vec{r} + \phi)}
# $$
# 
# On considérera dans ce cours des états stationnaires, déterminés par l'environnement 

# Le problème de la dynamique des électrons dans un solide est alors traité en remplaçant les particules par des ondes électroniques.
# 
# La constante $A \in \mathbb {C}$ est l'amplitude de l'onde électronique; elle représente la **densité de probabilité de présence** de la particule à la position $\vec{r}$ et à l'instant $t$.
# 
# L'intensité $\psi\psi^*$ correspond à la **densité de présence** (ou densité) de la particule à la position $\vec{r} = x\vec{u}_x + y\vec{u}_y+ z\vec{u}_z$ :
# 
# $$
# \psi (\vec{r})\psi(\vec{r})^* = \rho(\vec{r})
# $$
# 
# La particule ne pouvant être _intégralement_ à plusieurs endroits en même temps, $\rho(\vec{r})$ est nécessairement inférieur ou égal à 1.
# Soit $\Omega$ l'espace dans lequel se trouve la particule.
# En cumulant sur $\Omega$ les densités locales de la particule, on obtient la particule elle-même :
# 
# $$
# \int_\Omega \rho (\vec{r}) d^3\tau = 1
# $$
