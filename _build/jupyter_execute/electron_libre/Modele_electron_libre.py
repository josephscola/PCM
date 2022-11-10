#!/usr/bin/env python
# coding: utf-8

# # Modèle de l'électron libre

# ## Décrire le comportement d'un électron comme une onde

# Durant le XIXème siècle se sont accumulées des preuves expérimentales  montrant tantôt le comportement ondulatoire de la lumière, tantôt son comportement corpusculaire.
# 
# Au début du XXème siècle, De Broglie propose de généraliser le mouvement de tout corps ayant une énergie $E$ et une quantité de mouvement $\vec{p}$ à celui d'une onde de fréquence $\nu$ et de longueur d'onde $\lambda$.:
# $$
# \left\{
# \begin{align}
# E &= h\nu \\
# p &= h/\lambda
# \end{align}
# \right.
# $$
# avec $h = 6.6263\cdot 10^{-34}$ J$\cdot$s représente la constante de Planck.
# 
# En pratique cette description ne s'applique qu'à des particules de masse voisine de celles d'un électron.
# Pour des masses supérieures, les longueurs d'onde correspondantes n'ont pas de sens.
# 
# E. Schödinger (Physicien autrichien) postule une formulation générale du mouvement ondulatoire d'une telle particule sur la base du formalisme mathématique récemment établi pour les ondes.
# 
# L'état de la particule, _i.e._ son mouvement, est réprésenté par une onde, par exemple plane propagative :
# $$
# \psi (\vec{r}, t) = A e^{i(\vec{k}\cdot\vec{r} + \phi)}
# $$
# On considérera dans ce cours des états stationnaires, déterminés par l'environnement 

# Le problème de la dynamique des électrons dans un solide est alors traité en remplaçant les particules par des ondes électroniques.
# 
# La constante $A \in \mathbb {C}$ est l'amplitude de l'onde électronique; elle représente la **densité de probabilité de présence** de la particule à la position $\vec{r}$ et à l'instant $t$.
# 
# L'intensité $\psi\psi^*$ correspond à la **densité de présence** (ou densité) de la particule à la position $\vec{r} = x\vec{u}_x + y\vec{u}_y+ z\vec{u}_z$ :
# $$
# \psi (\vec{r})\psi(\vec{r})^* = \rho(\vec{r})
# $$
# La particule ne pouvant être _intégralement_ à plusieurs endroits en même temps, $\rho(\vec{r})$ est nécessairement inférieur ou égal à 1.
# Soit $\Omega$ l'espace dans lequel se trouve la particule.
# En cumulant sur $\Omega$ les densités locales de la particule, on obtient la particule elle-même :
# $$
# \int_\Omega \rho (\vec{r}) d^3\tau = 1
# $$

# ## Mouvement de l'électron libre : équation de Schrödinger

# ###  Position du problème stationnaire

# Dès lors que le système a atteint son régime permanent, _i.e._ après le régime transitoire consécutif à une modification de l'environnement, les ondes électroniques sont les solutions de l'équation de Schrödinger stationnaire.
# $$
# \frac{-\hbar^2}{2m} \Delta \psi (\vec{r}) + V (\vec{r}) \psi (\vec{r}) = \mathcal{E} \psi (\vec{r}).
# $$
# Les paramètres de l'équations sont:
# - $\mathcal{E}\psi (\vec{r})$ : l'énergie totale de la particule décrite par $\psi$, à la position $\vec{r}$
# - $V(\vec{r})\psi$ :  énergie potentielle de la particule décrite par $\psi$ à la position $\vec{r}$; $V (\vec{r})$ représente le potentiel d'interaction de la particule avec son environnement à la position $\vec{r}$
# - $\hbar = h/2\pi$

# ### Analogie avec les phénomènes ondulatoires

# Le formalisme de l'équation reprend celui des ondes ordinaires.
# Pour mémoire, le déplacement $u(x)$ au point $x$ d'une corde vibrante homogène est déterminé par l'équation 
# $$
# - \frac{\mathrm{d}^2 u}{\mathrm{d} x^2} = k^2u
# $$
# où $k$ dépend des propriétés de la corde (longueur, masse linéique, raideur).
# 
# Dans le cas d'un volume vibrant (_i.e._ le volume d'air dans le conduit d'une trompette), les déplacements d'air locaux, au point $\vec{r} = x\vec{u}_x + y \vec{u}_y + z \vec{u}_z$, sont déterminés de façon analogue :
# $$
# \begin{align}
# - \left( \frac{\partial^2 u}{\partial x^2}
#                     + \frac{\partial^2 u}{\partial y^2}
#                     + \frac{\partial^2 u}{\partial z^2} 
#                \right)  &= k^2u \\
# - \Delta u &= k^2u          
# \end{align}
# $$

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
#             &= \frac{\hbar^2}{2m} k^2 \psi \\
#             &= \frac{\hbar^2}{2m} \frac{p^2}{\hbar^2} \psi, \qquad (p = h/\lambda \equiv \hbar k) \\
#             &= \frac{\hbar^2}{2m} \frac{2m}{\hbar^2} \mathcal {E}_\mathrm{cin} \psi \\
#             &= \mathcal {E}_\mathrm{cin} \psi
# \end{align}
# $$
# Ainsi, le premier terme l'équation est l'énergie cinétique à la position $\vec{r}$ de la particule décrite par $\psi(\vec{r})$.
# Le second terme, $V(\vec{r})\psi(\vec{r})$, est l'énergie potentielle de la particule au voisinage de la position  $\vec{r}$.
# Finalement, l'équation de Schrödinger décompose donc l'énergie totale de l'onde électronique en énergies cinétique et potentielle.
# Elle est équivalente à l'approche utilisé pour les particules vues comme des corpuscules.

# ## Etats des électrons libres dans un édifice 3D

# ### Position du problème
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
# Sans erte de généralité, on considérera un édifice parallélépipédique de volume $V = L_x L_y L_z$.

# ### Calcul des solutions
# On cherche des solutions de la forme:
# $$ \psi (x,y,z) = \psi_x(x) \psi_y(y) \psi_z(z)$$
# L'équation de Schrödinger peut alors être séparée en 3 équations indépendnantes correspondant à chacune des 3 directions de l'espace :
# $$
# \frac{\hbar^2}{2m} \frac{\partial ^2 \psi_\alpha}{\partial \alpha^2} + \mathcal{E}_\alpha \psi_\alpha,
# \quad \alpha = x,y,z .
# $$
# Ces équations admettent des solutions de la forme :
# $$
# \psi_\alpha (\alpha) = A e^{ik_\alpha \alpha} + B e^{-ik_\alpha \alpha},
# \quad A, B \in \mathbb{C},\, \forall \alpha \in [0,L_\alpha]
# $$
# 
# La condition au premier bord ($\psi_\alpha (0) = 0$) impose $A + B =0$.
# Il s'ensuit que la condition au second bord ($\psi_\alpha (L_\alpha) = 0$) s'exprime :
# $$
# A (e^{ik_\alpha L_\alpha} - e^{-ik_\alpha L_\alpha}) = 0 \quad
#     \Rightarrow \quad A \sin (k_\alpha L_\alpha) = 0 \quad
#     \Rightarrow \quad 
#     k_\alpha = n_\alpha \pi / L_\alpha,\, n_\alpha \in \mathbb {N}^*
# $$
# Les $k_\alpha$ représentent les nombres d'onde ($k \equiv 2\pi/\lambda$) dans les directions $\alpha = x,y,z$, c'est-à-dire les composantes du vecteur d'onde représentant l'électron libre décrit par la solution $\psi$.

# Finalement, les solutions de l'équation du mouvement des électrons libres s'expriment :
# $$
# \psi (\vec{r}) = ABC \sin (\frac{n_x\pi}{L_x}x) \sin (\frac{n_y\pi}{L_y}y) \sin (\frac{n_z\pi}{L_z}z)
# $$
# avec $ABC = \sqrt {8/V}$ afin de respecter l'unicité de l'électron décrit par $\psi$ dans l'édifice : $\int_\mathrm{\acute{e}difice}\psi (\vec{r}) \psi^* (\vec{r}) d^3\tau = 1$.

# Dans un édifice 1D, les solutions de l'équation de Schrödinger stationnaires sont analogues aux modes de vibration d'une corde de guitare.

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
nrows = 4
fig, ax = plt.subplots (nrows = nrows, ncols = 1, figsize = (5,6))
x = np.linspace (0,1)
for i in range (nrows):
    ax [i].plot (x, np.sin ((i+1) * np.pi * x),  color = f'C{i:d}')
    ax [i].text (0.92, 0.87,f'n = {i+1:d}', color = f'C{i:d}')
    
    # use set_position
    
    ax [i].spines ['top'].set_color ('none')
    ax [i].spines ['left'].set_position ('zero')
    ax [i].spines ['right'].set_color ('none')
    ax [i].spines ['bottom'].set_position ('zero')
    ax [i].set_ylim ((-1,1))
    ax [i].set_ylabel (r'$\psi$'+f'{i+1:d} (x)')
            

ax [nrows-1].set_xlabel ('x/L_x')
ax [nrows-1].xaxis.set_label_coords(0.5, -0.05)
ax [0].set_title (f"Allure des {nrows:d} premières fonctions d'onde de l'électron libre (1D)")


plt.tight_layout ()
plt.show ()


# Les états accessibles aux électrons libres dans le puits de potentiel sont donc définis par l'ensemble des fonctions d'ondes solutions de l'équation de Schrödinger.
# Chacun de ces états se distingue par son vecteur d'onde $\vec{k}$.
# Ces vecteurs d'onde pointent vers des positions ponctuelles constituant un réseau régulier dans l'espace réciproque.
# 

# In[2]:


# espace des $k$ à 2 dimensions
fig, ax = plt.subplots (nrows = 1, ncols = 1, figsize = (5,5))

n, m = 14,14
col = 'C0'

for y in range (n+1):
    for x in range (m+1):
        if x*y == 0:
            ax.plot (x, y, marker = 'o', color = col, markersize = 8, alpha = 0.02)
        else:
            if x*x + y*y > m*n:
                ax.plot (x, y, marker = 'o', color = col, markersize = 6, alpha = 0.2)
            else:
                ax.plot (x, y, marker = 'o', color = col, markersize = 6)
x = np.linspace (0, m)
ax.plot (x, np.sqrt (m*m-x*x), color = 'C1', alpha = 0.5)
ax.set_aspect (1)
ax.set_xlabel (r'$n_x =  \frac{k_x}{\pi/L_x}$')
ax.set_ylabel (r'$n_y =  \frac{k_y}{\pi/L_y}$')

ax.annotate (s = '', xy = (7,12), xytext = (0,0),
            arrowprops = dict (facecolor = 'C1', edgecolor = 'C1', width = 1.2))
ax.text (7.5,12.2, r'$\Vert\vec{k}\Vert = k_F$', color = 'C1')

ax.set_title ("Etats accessibles aux électrons libres dans l\'espace des $k$ (2D)")

ax.set_xlim (0,m)
ax.set_ylim (0,n)
plt.show ()


# Chaque vecteur d'onde permis est séparé de son plus proche voisin d'une distance $\pi/L_\alpha$ suivant la direction $\alpha = x, y, z$.
# De ce fait, chaque vecteur d'onde permis occupe une surface $\frac{\pi^2}{L_xL_y}$ en 2D ou un volume $\frac{\pi^3}{L_xL_yL_z}$ en 3D.
# 
# Dans un édifice de _volume_ $V$ dimension $D$, on définit ainsi la **densité d'états dans l'espace des $k$**, en tenant compte du fait qu'au maximum deux électrons $(\uparrow\downarrow)$ peuvent partager le même vecteur d'onde :
# $$ 
# g(k) = \frac{2}{\pi^D/V}
# $$

# Il est commode de décrire les électrons par leur énergie de sorte qu'on définit également la ** densité d'états** en fonction de l'énergie.
# 
# Dans un édifice à 3D, on l'exprime en exprimant le nombre d'états d'énergie comprise entre $\mathcal{E}$ et $\mathcal{E}+\mathrm{d}\mathcal{E}$ comme le nombre d'états dans le 1/8$^\mathrm{ème}$ de coquille sphérique de rayons intérieur et extérieur $k$ et $k+\mathrm{d}k$, 
# $$
# \begin{align}
# g^{(3D)}(\mathcal{E}) \mathrm{d}\mathcal{E} &= g^{(3D)}(k) \frac{4 \pi k^2 \mathrm{d}k}{8} \\
# \Rightarrow g^{(3D)}(\mathcal {E}) &= \frac{V}{2\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} \mathcal{E}^{1/2}
# \end{align}
# $$
# 
