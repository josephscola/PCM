#!/usr/bin/env python
# coding: utf-8

# # Dopage d'un semiconducteur

# ## Application numérique :
# Le silicium cristallise dans un réseau c.f.c..
# La maille conventionnelle contient 8 atomes et son paramètre est $a = 5.431 020 511 \cdot 10^{-10}$ m.
# 
# On introduit dans le cristal une densité contrôlée $N_d$ d'impuretés de phosphore.
# Les atomes de phosphore occupent des sites de l'élément majeur auquel il se substitue.
# Le phosphore appartient à la colonne V du tableau périodique de sorte qu'après avoir construit les liaisons chimiques avec ses 4 voisins, il reste un électron non lié qui est "donné" à la population de porteurs libres.
# En admettant que la température ambiante est suffisante pour que toutes les impuretés soient ionisées, la densité de électrons libres ainsi introduits dans le cristal est égale à $N_d$.
# Le nombre total de d'électrons libres, intrinséques et issus du dopant, est donc maintenant :
# $$ 
# n = n_i + N_d
# $$

# En inversant l'expression de $n(\mathcal{E}_F)$ on obtient :
# 
# $$
# \mathcal{E}_F = \mathcal{E}_C + k_BT \ln \left( \frac{n}{N_C} \right)
# $$
# 
# et finalement, l'introduction des électrons libres donnés par les impuretés de phosphore décale l'énergie de Fermi de:
# 
# $$
# \mathcal{E}_F - \mathcal{E}_{Fi} = k_BT \ln \left( \frac{n}{ni} \right)
# $$

# Dans le cas d'un dopage par un élément de la troisième colonne, _e.g._ le bore, ce sont des trous libres qui sont introduits dans la bande de valence.
# Par conservation de la neutralité, la densité d'électrons libres s'en trouvent réduits (l'introduction de trous est en fait un déficit d'électrons libres) : $n = \frac{ni^2}{n_i + N_a}$ 

# In[1]:


import numpy as np
from IPython.display import display, Markdown
m = 9.1093837015e-31
kB = 1.380649e-23
T = 300
h = 6.62607015e-34
e = 1.602176634e-19

# Silicium
Eg = 1.12 # eV
me = 1.05 * m
mh = 1.15 * m


NC = 2 * (2*np.pi * me * kB*T / h/h) ** (3/2)
NV = 2 * (2*np.pi * mh * kB*T / h/h) ** (3/2)
NCstr = f"Densité d'états moyenne dans la bande de conduction : NC = {NC:.1e} m" + r"$^{-3}$"
NVstr = f"Densité d'états moyenne dans la bande de valence : NV = {NV:.1e} m" + r"$^{-3}$"

display (Markdown (NCstr))
display (Markdown (NVstr))


ni = np.sqrt (NC * NV * np.exp (-Eg * e / kB / T))

# nombre de porteurs par mailles
a = 5.431020511e-10
V = a*a*a

n_intrinseque = f'Densité de porteurs intrinsèque : ni = {ni * 1e-6:.0e} cm-3'
print (n_intrinseque)
nb_par_maille = f'La densité intrinsèque correspond à {ni * V:.1e} porteurs libres par maille,'
print (nb_par_maille)
distance_moyenne = f'soit 1 porteur libre toutes les {(ni * V) ** (-1/3):.0e} mailles.'
print (distance_moyenne)


# In[2]:


# dopage
Nd = np.array ([1e10, 1e12, 1e14, 1e16, 1e18]) * 1e6
Na = np.array ([1e10, 1e12, 1e14, 1e16, 1e18]) * 1e6

ePhiF_P = kB * T * np.log ( (ni+Nd) / ni) / e
ePhiF_B = kB * T * np.log ( ni*ni/ (ni+Na) / ni) / e

table  = '|Dopage P (cm$^{-3}$)| Décalage de $\mathcal{E}_F$ (eV)|Dopage B (cm$^{-3}$)| Décalage de $\mathcal{E}_F$ (eV)|\n'
table += '|:-:|:-:|:-:|:-:|'
for i in range (len (Nd)):
    table += f'\n|{Nd [i]:.0e} | {ePhiF_P [i]:.2f}|{Na [i]:.0e} | {ePhiF_B [i]:.2f}|'

display (Markdown (table))


# In[3]:


# proportion de Si substitué

Nd * a*a*a

