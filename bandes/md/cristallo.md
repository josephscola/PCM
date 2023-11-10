## Réseau direct, réseau réciproque (rappels)

### Définition minimale

#### Réseau direct
Un édifice cristallin infini se caractérise par la répétition à l'identique d'un motif atomique dans toutes les directions de l'espace.

> Cristal = Réseau + Motif

Un motif peut contenir 1 atome ou plusieurs, de même espèce ou d'espèces différentes.
L'ensemble des positions occupées par un motif constitue un maillage régulier de l'espace, c'est le *réseau*.
Les n\oeuds du réseau sont repérés par leur vecteur position à partir de l'origine du réseau :

$$
\mathrm{R\acute{e}seau} = \left\{ \vec {T} = n \vec{a} + m \vec {b} + p \vec {c}, (n,m,p) \in \mathbb{Z}^3 \right\}
$$

Les vecteurs $(\vec{a},\vec{b},\vec{c})$ constituent la *base du réseau direct* et définissent la *maille* du réseau.

Dans certains cas de figure, il est commode de définir une maille contenant plus d'un motif; la maille est alors dite multiple.
C'est le cas du cubique centré par exemple dont la multiplicité est 2, ou encore du cubique face centrée dont la multiplicité est quadruple.
On qualifie de *conventionnelle* la maille multiplie qu'on choisit d'utiliser pour faciliter sa réprésentation en comparaison avec la *maille primitive* ne contenant qu'un seul motif.
Celle-ci n'étant ni cubique, ni orthogonale, sa manipulation est malaisée.

Le cristal, et de ce fait toutes ses propriétés locales $f$ (densité électronique, potnetiel électrostatique, \cdots), sont invariants par translation de vecteur $\vec{T}$^:

$$
f (\vec{r} + \vec{T} ) = f (\vec{r}),\qquad \forall\, \mathrm{propri\acute{e}t\acute{e}s\,locales}.
$$

#### Réseau réciproque
Le réseau réciproque est une représentation équivalente du réseau direct. 
Elle consiste à le décrire non plus par les distances qui séparent les n\oeuds dans chaque direction de l'espace mais par le nombre de n\oeuds par unité de longueur dans chaque direction de l'espace.
Le réseau réciproque est ainsi une version en fréquence spatiale de l'édifice.

La position des n\oeuds du réseau réciproque est définie par une combinaison linéaire $\vec{g}$ des vecteurs de base :

$$
\vec{g} = g_1 \vec{A} + g_2 \vec{B} + g_3 \vec{C}, \qquad (g_1, g_2, g_3) \in \mathbb {Z}^3
$$

où les vecteurs de base du réseau réciproque sont liés aux vecteurs de base du réseau direct :

$$
\begin{align}
\vec{A} &= 2\pi \frac{\vec{b}_1\wedge \vec{c}_1}{V_1} \\
\vec{B} &= 2\pi \frac{\vec{c}_1\wedge \vec{a}_1}{V_1} \\
\vec{C} &= 2\pi \frac{\vec{a}_1\wedge \vec{b}_1}{V_1}
\end{align}
$$

où $V_1 = \vec{a}_1 \cdot \vec{b}_1\wedge \vec{c}_1$ est le volume de la maille primitive.

La norme des vecteurs réciproques s'exprime en $Å^{-1}$, si les paramètres de mailles sont donnés en $Å$



> Propriété importante : 

$$
\begin{align}
\vec{a}\cdot \vec{A} &= 2\pi,\\
\vec{a} \cdot \vec{B} &= \vec{a} \cdot \vec{C} = 0
\end{align}
$$

#### Zone de Brillouin

La zone de Brillouin est le volume de l'espace réciproque délimité par les plan médiateurs des segments joignant 2 noeuds voisins du réseau réciproque.
Par construction, son volume est celui de la maille primitive du réseau réciproque et elle contient toutes les symétries du réseau.


