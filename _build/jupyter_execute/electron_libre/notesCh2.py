#!/usr/bin/env python
# coding: utf-8

# Le problème de la dynamique des électrons dans un solide est alors traité en remplaçant les particules par des ondes électroniques.
# 
# La constante $A \in \mathbb {C}$ est l'amplitude de l'onde électronique; elle représente la **densité de probabilité de présence** de la particule à la position $\vec{r}$ et à l'instant $t$.
# 
# L'intensité $\psi\psi^*$ correspond à la **densité de présence** (ou densité) de la particule à la position $\vec{r}$ :
# $$
# \psi (\vec{r})\psi(\vec{r})^* = \rho(\vec{r})
# $$
# La particule ne pouvant être à plusieurs endroit en même temps, $\rho(\vec{r})$ est nécessairement inférieur ou égal à 1.
# Soit $\Omega$ l'espace dans lequel se trouve la particule.
# En cumulant sur $\Omega$ les densités locales de la particule, on obtient la particule elle-même :
# $$
# \int_\Omega \rho (\vec{r}) d^3\tau = 1
# $$
# 
# ## Equation du mouvement : équation de Schrödinger
# 
# Dès lors que le système a atteint son régime permanent, _i.e._ après le régime transitoire consécutif à une modification de l'environnement, les ondes électroniques sont les solutions de l'équation de Schrödinger stationnaire.
# $$
# \frac{-\hbar^2}{2m} \Delta \psi (\vec{r}) + V (\vec{r}) \psi (\vec{r}) = \mathcal{E} \psi (\vec{r}).
# $$
# Les paramètres de l'équations sont:
# - $\mathcal{E}\psi (\vec{r})$ : l'énergie totale de la particule décrite par $\psi$, à la position $\vec{r}$
# - $V(\vec{r})\psi$ :  énergie potentielle de la particule décrite par $\psi$ à la position $\vec{r}$; $V (\vec{r})$ représente le potentiel d'interaction de la particule avec son environnement à la position $\vec{r}$
# - $\hbar = h/2\pi$
# 
# > Le formalisme de l'équation reprend celui des ondes ordinaires.
# Pour mémoire, le déplacement $u(x)$ au point $x$ d'une corde vibrante homogène est déterminé par l'équation 
# $$
# - \frac{\mathrm{d}^2 u}{\mathrm{d} x^2} = k^2u
# $$
# où $k$ dépend des propriétés de la corde (longueur, masse linéique, raideur).
# 
# > Dans le cas d'un volume vibrant (_i.e._ le volume d'air dans le conduit d'une trompette), les déplacements d'air locaux, au point $\vec{r} = x\vec{u}_x + y \vec{u}_y + z \vec{u}_z$, sont déterminés de façon analogue :
# $$
# \begin{align}
# - \left( \frac{\partial^2 u}{\partial x^2}
#                     + \frac{\partial^2 u}{\partial y^2}
#                     + \frac{\partial^2 u}{\partial z^2} 
#                \right)  &= k^2u \\
# - \Delta u &= k^2u          
# \end{align}
# $$
# 
# ### Eléments de justification
# Considérons la propagation de l'onde électronique se produit suivant $\vec{k} = k_x\vec{u}_x + k_y\vec{u}_y + k_z\vec{u}_z$ :
# 
# Le premier terme de l'équation de Schrödinger s'écrit :
# $$
# \begin{align}
# \frac{-\hbar^2}{2m} \Delta \psi &= \frac{-\hbar^2}{2m}
#                                         \left(
#                                         \frac{\partial^2 A e^{i\vec{k}\cdot\vec{r}}}{\partial x^2}
#                                         - \frac{\partial^2 A e^{i\vec{k}\cdot\vec{r}}}{\partial y^2}
#                                         - \frac{\partial^2 A e^{i\vec{k}\cdot\vec{r}}}{\partial z^2}
#                                         \right)\\
#             &= \frac{\hbar^2}{2m} \left( k_x^2 A e^{i\vec{k}\cdot\vec{r}}
#                                         + k_y^2 A e^{i\vec{k}\cdot\vec{r}}
#                                         + k_z^2 A e^{i\vec{k}\cdot\vec{r}} \right) \\
#             &= \frac{\hbar^2}{2m} k^2 \psi
#             &= \frac{\hbar^2}{2m} \frac{p^2}{\hbar^2} \psi, \qquad (p = h/\lambda \equiv \hbar k) \\
#             &= \frac{\hbar^2}{2m} \frac{2m}{\hbar^2} \mathcal {E}_\mathrm{cin} \psi \\
#             &= \mathcal {E}_\mathrm{cin} \psi
# \end{align}
# $$
# Ainsi, le premier terme l'équation est l'énergie cinétique de la particule décrite par $\psi$.
# Le second terme est l'énergie potentielle.
# Finalement, l'équation de Schrödinger décompose donc l'énergie totale de l'onde électronique en énergies cinétique et potentielle.
# Elle est équivalente à l'approche utilisé pour les particules vues comme des corpuscules.
# 
# ## Etats des électrons libres dans un édifice 3D
# 
# Les électrons sont dits libres au sens où ils n'interagissent ni entre eux, ni avec les noyaux du système. 
# Tout se passe comme si l'édifice qu'ils occupent étaient une enceinte fermée et vide; 
# Le problème s'écrit alors :
# $$
# \frac{-\hbar^2}{2m} \Delta \psi + V \psi = \mathcal{E}\psi
# $$
# avec
# $$
# \left\{
# \begin{align}
# V (\vec{r}\in \mathrm{\acute{e}difice}) &= 0\\
#     V (\vec{r}\notin \mathrm{\acute{e}difice}) &\rightarrow \infty
# \end{align}
# \right.
# $$
# Par sa forme infiniment profonde, ce potentiel est usuellement désigné comme un _puits de potentiel_.

# 
# # Brouillon

# laplacien 1D
# Le premier terme de l'équation de Schrödinger s'écrit :
# $$
# \begin{align}
# \frac{-\hbar^2}{2m} \frac{\mathrm{d}^2 \psi}{\mathrm{d}x^2}
#     & = \frac{-\hbar^2}{2m} \frac{\mathrm{d}^2 A e^{ikx}}{\mathrm{d}x^2} \\
#     & = \frac{\hbar^2}{2m} k^2 \psi \\
#     & = \frac{\hbar^2}{2m} \frac{p^2}{\hbar^2} \psi, \qquad (p = h/\lambda \equiv \hbar k) \\
#     & = \frac{\hbar^2}{2m} \frac{2m}{\hbar^2} \mathcal {E}_\mathrm{cin} \psi \\
#     & = \mathcal {E}_\mathrm{cin} \psi
# \end{align}
# $$
