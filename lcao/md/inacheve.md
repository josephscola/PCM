![](./figures/C_hybridation.png)

![](./figures/pi-bonds.png)

## Densité d'états

A partir de la relation de dispersion, peuvent être dérivés la densité d'états et la masse effective.

$$
g(\mathcal{E}) = \frac{ N}{\pi t} \left[ 1 - \left(\frac{\mathcal{E} - \mathcal{E}_0}{2t} \right)^2 \right]^{-1/2}
$$

$$
m^* = \frac{-\hbar^2}{a^2} \frac{1}{\mathcal{E} - \mathcal{E}_0}
$$

    /tmp/ipykernel_45729/4093420301.py:4: RuntimeWarning: invalid value encountered in power
      gE = (1 - (E/0.2)**2) ** (-0.5)





    [<matplotlib.lines.Line2D at 0x7fb57ea79160>]




    
![png](inacheve_files/inacheve_3_2.png)
    


## Description du potentiel du réseau

La fonction $V (\vec{r})$ possède par construction la périodicité du réseau.
Elle peut donc s'exprimer comme la superposition de fonctions périodiques dans chaque direction ($x$, $y$, $z$) de l'espace :

$$
V (x) = \sum_{n\ge 1} g_n \cos \left( n\frac{2\pi}{a}x \right).
$$

En effet, en première approximation, le potentiel périodique considéré comme une oscillation sinusoïdale de période $a$.
Les termes d'ordre supérieurs ($n\ge 2$) sont périodique de période $a/n$, ce qui conserve la périodicité de période $a$. 
Ces termes apportent des corrections de plus en plus fines à cette approximation jusqu'à faire tendre la série vers la fonction originale, éventuellement à la limite $n\rightarrow \infty$ (c'est la *décomposition en série de Fourier*).

Dans sa version complexe (décomposition en ondes planes), cette série prend la forme suivante :

$$
V (x) = \sum_{n\in \mathbb{Z}} G_n e^ { in\frac{2\pi}{a}x }.
$$
