#!/usr/bin/env python
# coding: utf-8

# # Relation de dispersion
# Dans ces conditions, le potentiel $V$ du réseau s'exprime comme la répétition, sur chaque site $\vec{T}$ du réseau, du potentiel électrostatique créé par les noyaux vus comme des charges ponctuelles $q$ : 
# 
# $$
# V (\vec{r}) = \sum_{\vec{T}} \frac{q}{4\pi\varepsilon_0 \Vert \vec{r} - \vec{T} \Vert}
# $$
# 
# Soit pour une rangée d'atomes :
# 
# $$
# V (x) = \sum_{m} \frac{q}{4\pi\varepsilon_0 | x + ma |}
# $$
# 

# Vu comme un corpuscule, l'énergie d'un électron situé en $x$ plongé dans un potentiel $V$ vaut $-eV(x)$.
# Dans sa version ondulatoire $\psi(x)$, l'énergie de l'électron doit intégrer l'ensemble de l'espace où l'électron se trouve "dilué" :
# 
# $$
# \mathcal{E}  = -\int \psi^* V \psi \mathrm{d}x 
#  = -\int \sum_{m, m^\prime} \psi^*_0(x + ma) V \psi_{0}(x + m^\prime a) \mathrm{d}x
# $$
# 
# Or, les fonctions $\psi_m$ décroissent très vite et seuls les deux termes de la double somme vérifiant $|m-m^\prime| \le 1$ ne s'annulent pas :
# 
# $$
# \begin{align}
# -\mathcal{E}_0  &= -\int \psi_0^*(x) V\psi_{0}(x) \mathrm{d}x, \\
# t^+  &= -\int e^{ika} \psi_0^*(x + a) V\psi_{0}(x) \mathrm{d}x = -e^{ika} t,\\
# t^-  &= -\int e^{-ika} \psi_0^*(x - a) V\psi_{0}(x) \mathrm{d}x = -e^{-ika} t
# \end{align}
# $$
# 
# - Le terme $U_0$ représente l'énergie de l'électron sur son site : c'est le gain d'énergie à être sur son atome plutôt qu'ailleurs.
# - Le terme $t$ représente l'énergie de transfert : c'est le gain d'énergie associé à la délocalisation (partielle) sur les sites voisins de droite (+) et de gauche (-). C'est une mesure du recouvrement des orbitales voisines. 
# 
# Les termes de transfert électronique sont responsables de la perturbation subies par les orbitales atomiques pures induites par la présence du réseau; en l'occurrence l'influence du réseau se limite aux plus proches voisins.
# 
# Finalement, l'énergie d'un électron s'exprime donc :
# 
# $$
# \mathcal{E} = -\mathcal{E}_0  - t e^{ika}  - t e^{-ika} = \mathcal{E}_0 - 2t \cos (ka)
# $$

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

k = np.linspace (-np.pi, np.pi)
E = 0 - np.cos (k)
fig, ax = plt.subplots ()


ax.plot (k, E)
ax.set_xlabel ('k')
ax.set_xticks([-np.pi, 0, np.pi], [r'-$\dfrac{\pi}{a}$', '0', r'$\dfrac{\pi}{a}$'])
ax.set_yticks([-1, 0, 1],[r'$E_0 - 2t$', '$E_0$', r'$E_0 + 2t$'])
fig.savefig ('./figures/lcao_dispersion.png')
plt.close ()


# ![](./figures/lcao_dispersion.png)
