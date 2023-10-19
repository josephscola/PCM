# Dopage d'un semiconducteur

## Application numérique :
Le silicium cristallise dans un réseau c.f.c..
La maille conventionnelle contient 8 atomes et ses paramètres physiques sont les suivants :
- paramètre de maille cubique est $a = 5.431 020 511 \cdot 10^{-10}$ m
- bande interdite $ \mathcal{E}_g = 1.12$ eV
- masses effectives : 
    - $m^*_e = 1.05\,m_0$
    - $m^*_h = 1.15\,m_0$

On introduit dans le cristal une densité contrôlée $N_d$ d'impuretés de phosphore.
Les atomes de phosphore occupent des sites de l'élément majeur auquel il se substitue.
Le phosphore appartient à la colonne V du tableau périodique de sorte qu'après avoir construit les liaisons chimiques avec ses 4 voisins, il reste un électron non lié qui est "donné" à la population de porteurs libres.
En admettant que la température ambiante est suffisante pour que toutes les impuretés soient ionisées, la densité de électrons libres ainsi introduits dans le cristal est égale à $N_d$.
Le nombre total de d'électrons libres, intrinséques et issus du dopant, est donc maintenant :
$$ 
n = n_i + N_d
$$

En inversant l'expression de $n(\mathcal{E}_F)$ on obtient :

$$
\mathcal{E}_F = \mathcal{E}_C + k_BT \ln \left( \frac{n}{N_C} \right)
$$

et finalement, l'introduction des électrons libres donnés par les impuretés de phosphore décale l'énergie de Fermi de:

$$
\mathcal{E}_F - \mathcal{E}_{Fi} = k_BT \ln \left( \frac{n}{ni} \right)
$$

Dans le cas d'un dopage par un élément de la troisième colonne, _e.g._ le bore, ce sont des trous libres qui sont introduits dans la bande de valence.
Par conservation de la neutralité, la densité d'électrons libres s'en trouvent réduits (l'introduction de trous est en fait un déficit d'électrons libres) : $n = \frac{ni^2}{n_i + N_a}$ 

Densité de porteurs intrinsèque : 

$$ n_i = \sqrt {N_C N_V e^{-\mathcal{E}_g / K_BT}} $$



$n_i$ = 1e+10 cm$^{-3}$



La densité intrinsèque correspond à 1.8e-12 porteurs libres par maille, soit 1 porteur libre toutes les 8e+03 mailles.



|Dopage P (cm$^{-3}$)| Décalage de $\mathcal{E}_F$ (eV)|Dopage B (cm$^{-3}$)| Décalage de $\mathcal{E}_F$ (eV)|
|:-:|:-:|:-:|:-:|
|1e+16 | 0.02|1e+16 | -0.02|
|1e+18 | 0.12|1e+18 | -0.12|
|1e+20 | 0.23|1e+20 | -0.23|
|1e+22 | 0.35|1e+22 | -0.35|
|1e+24 | 0.47|1e+24 | -0.47|

