#!/usr/bin/env python
# coding: utf-8

# # Mouvement de l'électron libre : équation de Schrödinger

# ##  Position du problème stationnaire

# Dès lors que le système a atteint son régime permanent, _i.e._ après le régime transitoire consécutif à une modification de l'environnement, les ondes électroniques sont les solutions de l'équation de Schrödinger stationnaire.
# 
# $$
# \frac{-\hbar^2}{2m} \Delta \psi (\vec{r}) + V (\vec{r}) \psi (\vec{r}) = \mathcal{E} \psi (\vec{r}).
# $$
# 
# Les paramètres de l'équations sont:
# - $\mathcal{E}\psi (\vec{r})$ : l'énergie totale de la particule décrite par $\psi$, à la position $\vec{r}$
# - $V(\vec{r})\psi$ :  énergie potentielle de la particule décrite par $\psi$ à la position $\vec{r}$; $V (\vec{r})$ représente le potentiel d'interaction de la particule avec son environnement à la position $\vec{r}$
# - $\hbar = h/2\pi$

# ## Analogie avec les phénomènes ondulatoires

# Le formalisme de l'équation reprend celui des ondes ordinaires.
# Pour mémoire, le déplacement $u(x)$ au point $x$ d'une corde vibrante homogène est déterminé par l'équation 
# 
# $$
# - \frac{\mathrm{d}^2 u}{\mathrm{d} x^2} = k^2u
# $$
# 
# où $k$ dépend des propriétés de la corde (longueur, masse linéique, raideur).
# 
# Dans le cas d'un volume vibrant (_i.e._ le volume d'air dans le conduit d'une trompette), les déplacements d'air locaux, au point $\vec{r} = x\vec{u}_x + y \vec{u}_y + z \vec{u}_z$, sont déterminés de façon analogue :
# 
# $$
# \begin{align}
# - \left( \frac{\partial^2 u}{\partial x^2}
#                     + \frac{\partial^2 u}{\partial y^2}
#                     + \frac{\partial^2 u}{\partial z^2} 
#                \right)  &= k^2u \\
# - \Delta u &= k^2u          
# \end{align}
# $$

# ## Eléments de justification
# Considérons la propagation de l'onde électronique se produit suivant $\vec{k} = k_x\vec{u}_x + k_y\vec{u}_y + k_z\vec{u}_z$ :
# 
# Le premier terme de l'équation de Schrödinger s'écrit :
# 
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
#             &= \frac{\hbar^2}{2m} k^2 \psi \\
#             &= \frac{\hbar^2}{2m} \frac{p^2}{\hbar^2} \psi, \qquad (p = h/\lambda \equiv \hbar k) \\
#             &= \frac{\hbar^2}{2m} \frac{2m}{\hbar^2} \mathcal {E}_\mathrm{cin} \psi \\
#             &= \mathcal {E}_\mathrm{cin} \psi
# \end{align}
# $$
# 
# Ainsi, le premier terme l'équation est l'énergie cinétique à la position $\vec{r}$ de la particule décrite par $\psi(\vec{r})$.
# Le second terme, $V(\vec{r})\psi(\vec{r})$, est l'énergie potentielle de la particule au voisinage de la position  $\vec{r}$.
# Finalement, l'équation de Schrödinger décompose donc l'énergie totale de l'onde électronique en énergies cinétique et potentielle.
# Elle est équivalente à l'approche utilisé pour les particules vues comme des corpuscules.
