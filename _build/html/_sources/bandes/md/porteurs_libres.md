# Porteurs libres dans un semiconducteur

## Densité de porteurs libres
La densité de porteurs libres, c'est-à-dire d'électrons libres dans la bande de conduction et de trous dans la bande de valence s'exprime à partir de la densité d'états et de la distribution de Fermi-Dirac.
Par exemple, le nombre d'électrons dans la bande de conduction s'écrit :

$$
N = \int_{\mathcal{E}_C}^{\infty} g(\mathcal{E}) f_{FD}(\mathcal{E} \mathrm{d}\mathcal{E},\quad
g (\mathcal{E}) = \frac{V}{2\pi^2} \left( \frac{2m^*_e}{\hbar^2} \right)^{3/2} (\mathcal{E} - \mathcal{E}_C)^{1/2}
$$

A température ambiante, $k_BT \approx 26$ meV et $e^{(\mathcal{E}-\mathcal{E}_F)/k_BT}$ devient exponentiellement grand devant 1 pour des écarts d'énergie supérieurs à 0.1 eV.
Pour des bandes interdites de l'ordre de 1 eV, il est donc réaliste de substituer la distribution de Fermi-Dirac par son expression asymptotique :

$$
f_{FD} (\mathcal{E})\stackrel{\mathcal{E}-\mathcal{E}_F > k_BT}{\longrightarrow}e^{-(\mathcal{E}-\mathcal{E}_F)/k_BT}
$$

En utilisant le résultat $\int_0^{\infty} \sqrt{x}e^{-x} \mathrm{d}x = \frac{\sqrt{\pi}}{2}$, on obtient l'expression de la densité d'électrons dans la bande de conduction :

$$
n = N_C e^{-(\mathcal{E}_C-\mathcal{E}_F)/k_BT},\quad N_C = 2 \left( \frac{2\pi m^*_ek_BT}{h^2} \right)^{3/2}
$$

En considérant les trous comme des porteurs de charge positive et de masse $m_h^*$ dans la bande de valence dont le bord est $\mathcal{E}_V$, le raisonnement précédent produit l'expression des trous libres dans la bande de valence :

$$
p = N_V e^{(\mathcal{E}_V-\mathcal{E}_F)/k_BT},\quad N_V = 2 \left( \frac{2\pi m^*_hk_BT}{h^2} \right)^{3/2}
$$

## Neutralité du cristal

La neutralité du cristal impose $n = p$, c'est-à-dire
$$
\begin{align}
\frac{e^{-(\mathcal{E}_C-\mathcal{E}_F)/k_BT}}{e^{(\mathcal{E}_V-\mathcal{E}_F)/k_BT}} &= \frac{N_V}{N_C} \\
\Rightarrow 
\mathcal{E}_F &= \frac{\mathcal{E}_C + \mathcal{E}_V}{2} + \frac{3}{4} k_BT \log \left(\frac{m_h}{m_e}\right)
\end{align}
$$

*Remarque :* si la différence des masses effectives des électrons et des trous est négligeable, alors l'énergie de Fermi est au milieu de la bande de conduction.

## Semiconducteur intrinsèque

Les densités de porteurs libres sont déterminées par la structure électronique (densité d'états et bande interdite $\mathcal{E}_g$).

$$
np \equiv ni^2 = N_C N_V e^{-\mathcal{E}_g/k_BT}
$$
