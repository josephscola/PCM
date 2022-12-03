#!/usr/bin/env python
# coding: utf-8

# # Densité d'états

# ## Densité $g(\vec{k})$
# Les points de l'espace des $\vec{k}$ vers lesquels pointent les vecteurs d'onde des solutions de l'équation de Schrödinger sont distants les uns les autres de $\pi/L_\alpha,\quad \alpha = x,y,z$ suivant les trois directions de l'espace.
# Le volume de l'espace des $\vec{k}$ qu'occupe un vecteur d'onde est donc $\frac{\pi^3}{V}$ ($V = L_xL_yL_z$, volume de l'édifice).
# Chaque vecteur d'onde permis peut être occupé au maximum par deux états électroniques de spins opposé($\uparrow\downarrow$) et la densité d'état s'exprime dans un édifice de _volume_ $V$ dans un espace de dimensions $D$ :
# 
# $$
# g(\vec{k}) = \frac{2}{\pi^D/V}.
# $$

# ## Densité $g(\mathcal{E})$
# Il est commode de décrire les électrons par leur énergie de sorte qu'on définit également la **densité d'états** en fonction de l'énergie.
# 
# Dans un édifice à 3D, on l'exprime en exprimant le nombre d'états d'énergie comprise entre $\mathcal{E}$ et $\mathcal{E}+\mathrm{d}\mathcal{E}$ comme le nombre d'états dans le 1/8$^\mathrm{ème}$ de coquille sphérique de rayons intérieur et extérieur $k$ et $k+\mathrm{d}k$, 
# 
# $$
# \begin{align}
# g^{(3D)}(\mathcal{E}) \mathrm{d}\mathcal{E} &= g^{(3D)}(k) \frac{4 \pi k^2 \mathrm{d}k}{8} \\
# \Rightarrow g^{(3D)}(\mathcal {E}) &= \frac{V}{2\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} \mathcal{E}^{1/2}
# \end{align}
# $$
# 
# 
# 
# Soit $g(\mathcal{E}) \mathrm{d}\mathcal{E}$ le nombre d'états dont l'énergie est comprise dans l'intervalle $[\mathcal{E}, \mathcal{E}\mathrm{d}\mathcal{E}]$.
# L'énergie $\mathcal{E}$ des électrons libres étant identique à leur énergie cinétique $\frac{\hbar^2k^2}{2m}$, les vecteurs d'onde des états correspondants ont une norme comprise dans l'intervalle $[k;k+\mathrm{d}k]$ qui définit un huitième de coquille sphérique de volume $\mathrm{d}V_\mathrm{coq}$ :
# 
# $$
# \mathrm{d}V_\mathrm{coq} = \frac{1}{8} 4\pi k^2 \mathrm{d}k.
# $$
# 
# On exprime alors :
# 
# $$
# \begin{align}
# g(\mathcal{E}) \mathrm{d}\mathcal{E} &= g(\vec{k})\mathrm{d}V_\mathrm{coq} \\
# g(\mathcal{E}) \frac{\hbar^2}{m}k\mathrm{d}k &= \frac{2}{\pi^3V} \frac{1}{2} \pi k^2 \mathrm{d}k \\
# \rightarrow g(\mathcal{E})                   &= \frac{m}{\hbar^2}\frac{k}{\pi^2V} \\
#                                              &= \frac{m}{\hbar^2}\frac{(2m/\hbar^2\mathcal{E})^{1/2}}{\pi^2V}
# \end{align}
# $$
# 

# ## Population statistique

# Dans tout système thermondnamique, on attribue à chaque état (_i.e._ chaque valeur énergie) une probabilité d'occurrence.
# Cette probabilité est définie comme le rapport entre le _nombre de configurations prises par les $N$ particules du système dont l'énergie est $\mathcal{E}$_ sur le _nombre total de configurations_.
# Une assemblée d'électrons est analogue à un gaz dont les particules seraient soumises à une restriction suplémentaire : l'_exclusion de Pauli_ interdit la double occupation d'un état. 
# Autrement dit un état donné, défini par ses nombres quantiques, ne peut être occupé que par un et un seul électron.

# Le taux d'occupation d'un état d'énergie $\mathcal{E}$ est déterminé par la statistique de Fermi-Dirac :
# 
# $$
# f_\mathrm{FD} (\mathcal{E}) = \frac {1}{1 + e^{(\mathcal{E}-\mathcal{E}_F)/k_BT}}
# $$
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
E = np.linspace (0, 2, 101)
mu = 1
E /= mu

def f_FD (E, kBT):
    return 1 / (1 + np.exp ((E-1)/kBT))

    
fig, ax = plt.subplots ()
kBT = 0.001
ax.plot (E, f_FD (E, kBT), color = 'k', label = '$T$ = 0 K')

kBT = 0.1
ax.plot (E, f_FD (E, kBT), color = 'C0', label = '$k_BT = \mathcal{E}_F/10$')
ax.axvline (x = 1 + 2*kBT, ymin = 0, ymax =  f_FD (1 + 2*kBT, kBT), ls = 'dashed', color = 'k', lw = 0.5, alpha = 0.8)
ax.axhline (y = f_FD (1 + 2*kBT, kBT), xmin = 0, xmax = 0.5+kBT, color = 'k', lw = 0.5, alpha = 0.8)
ax.text ((1 + 2*kBT), f_FD (1 + 2*kBT, kBT) + 0.02, '$(\mathcal {E}+2k_BT)/\mathcal{E}_F$')

ax.axvline (x = 1 - 2*kBT, ymin = 0, ymax = f_FD (1 - 2*kBT, kBT), ls = 'dashed', color = 'k', lw = 0.5, alpha = 0.8)
ax.axhline (y = f_FD (1 - 2*kBT, kBT), xmin = 0, xmax = 0.5 - kBT, ls = 'dashed', color = 'k', lw = 0.5, alpha = 0.8)
ax.text ((1 - 2*kBT)-0.4, f_FD (1 - 2*kBT, kBT) - 0.08, '$(\mathcal {E}-2k_BT)/\mathcal{E}_F$')

ax.set_xlabel ('$\mathcal{E}/\mathcal{E}_F$')
ax.set_ylabel ('$f_{FD} (\mathcal{E}/\mathcal{E}_F)$')
ax.set_ylim (0,1.02)
ax.set_xlim (0,2)

ax.legend ()
ax.set_title ('Statistique de Fermi-Dirac')
plt.show ()


# A température nulle, le taux d'occupation passe brutalement de 1 (tous les états d'énergie $\mathcal{E}<\mathcal{E}_F$ sont occupés) à 0 (tous les états $\mathcal{E}>\mathcal{E}_F$ sont vides).
# A mesure que la température augmente, la fonction s'adoucit : sur l'intervalle de largeur $4k_BT$ centré sur $\mathcal{E}_F$, le taux d'occupation varie de 90 % à 10 %.
# La fonction est donc d'autant plus étalée que la température est élevée.
# 
# La statistique de Fermi-Dirac indique que les états de plus basse énergie étant thermodynamiquement les plus stables, ils sont peuplés en priorité. 

# ## Energie de Fermi

# L'énergie des électrons de plus haute énergie de l'assemblée détermine le _potentiel chimique_ $\mu$ du système.
# Cette grandeur est voisine de l'énergie de Fermi $\mathcal{E}_F$ qui est l'énergie caractéristique (indépendante de la température) du taux d'occupation.
# Le potentiel chimique coïncide avec l'énergie de Fermi à température nulle:
# 
# $$\mu (T = 0\,\mathrm{K}) = \mathcal{E}_F$$
# 
# 
# L'énergie de Fermi est donc l'énergie du dernier électron à prendre place dans l'édifice.
# A température nulle, 
# Soit $\mathrm{d}N$ le nombre d'états occupés dont l'énergie est comprise entre $\mathcal{E}$ et $\mathcal{E} + \mathrm{d}\mathcal{E}$.
# Cette quantité est défini par le produit des états dans cet intervalle d'énergie et du taux d'occupation :
# 
# $$
# \mathrm{d}N = g(\mathcal{E}) \mathrm{d}\mathcal{E} f_\mathrm{FD} (\mathcal{E})
# $$
# 
# Ainsi le nombre total d'électrons libres $N = \int_\mathrm{cristal} \mathrm{d}N$ s'exprime :
# 
# $$
# \begin{align}
# N &= \int_0^\infty g(\mathcal{E}) f_\mathrm{FD} (\mathcal{E}) \mathrm{d}\mathcal{E} \\
#   &= \int_0^{\mathcal{E}_F} \frac{V}{2\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} \mathcal{E}^{1/2} \mathrm{d}\mathcal{E},\qquad T = 0 \,\mathrm{K} \\
#   &= \frac{V}{3\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} \mathcal{E}_F^{3/2}
# \end{align}
# $$
# 
# En posant $n = N/V$ la densité d'électrons libres, on obtient une expression de l'_énergie de Fermi_ :
# 
# $$
# \mathcal{E}_F = \frac{\hbar^2}{2m} (3 \pi^2 n)^{3/2}.
# $$
# 
# Par suite, le _vecteur de Fermi_ peut être défini comme la norme du vecteur d''onde des électrons au niveau de Fermi :
# 
# $$
# k_F = (3\pi^2 n)^{1/3}.
# $$

# ## Etats occupés

# La statistique de Fermi-Dirac indique qu'à température nulle, les états occupés sont ceux de plus faibles énergies, soit les états dont l'énergie appartient à l'intervalle $[0;\mathrm{E}_F]$.
# L'_étalement_ de la distribution de probabilité induit part l'agitation thermique conduit à ce que des états occupés soient libérés par des électrons excités dans des états d'énergie supérieur à $\mathcal{E}_F$.

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

def g (E):
    return np.sqrt (E)

kBT = 0.05

fig, ax = plt.subplots ()
ax.plot (E, g (E), color = 'k', alpha = 0.8)
axxlim = ax.get_xlim ()
axylim = ax.get_ylim ()
ax.axvline (x = 1, ymin = 0, ymax = 0.99/axylim [1], color = 'k', lw = 1, ls = 'dashed')
ax.annotate('', xy=(0.02, 0.6), xytext=(0.2, 0.6),
            arrowprops=dict(arrowstyle = '->',color='k', alpha = 0.8))

#ax.plot (E, g (E) * f_FD (E, kBT), color = 'C2')
ax.fill_between (E, 0, g (E) * f_FD (E, kBT), color = 'C1', alpha = 0.2)

ax.set_ylabel ("densité d'états")

ax2 = ax.twinx ()
ax2.plot (E, f_FD (E, kBT), color = 'C0', ls = 'dashed', alpha = 0.8)
ax2.set_ylabel ("taux d'occupation $f_\mathrm{FD}$")
ax.annotate('', xy=(0.98*axxlim[1], 0.2), xytext=(0.8*axxlim[1], 0.2),
            arrowprops=dict(arrowstyle = '->',color='C0', alpha = 0.8))
ax.set_xlabel (r'$\mathcal{E}/\mathcal{E}_F$')
ax.set_title ('Etats occupés par des électrons libres dans un édifice 3D')

ax.set_ylim (0, 1.5)
ax2.set_ylim (0, 1.02)
plt.show ()

