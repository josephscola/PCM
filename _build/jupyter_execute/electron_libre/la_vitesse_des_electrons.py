#!/usr/bin/env python
# coding: utf-8

# Bonjour Elzéar,
# 
# Tu as beaucoup changé, je ne t'ai pas reconnu au téléphone. L'espace d'un instant, j'ai même imaginé que c'était un de mes étudiants qui m'appelait !
# C'était un plaisir de réfléchir à ta question et d'y répondre.

# # A quelle vitesse les électrons vont-ils ?

# La réponse dépend beaucoup des circonstances.
# Les électrons sont des particules portant une masse $m = 9.109 383 7015 \cdot 10^{-31}$ kg et une charge électrique $e = 1.602 176 634\cdot 10^{-19}$ C.
# Dans la plupart des contextes, l'effet de la masse (poids, inertie, $\dots$) est ridiculement faible en comparaison avec celui de la répulsion par les autres objets chargés négativement (ou l'attraction par les objets chargés positivement). 
# La vitesse de l'électron va donc être principalement déterminé par son environnement.

# ## Dans le vide

# Dans l'atmosphère et si on les laisse évoluer librement, les électrons réagir à la moindre attraction : en général, il se recombine avec une des premières molécules de l'atmosphère qu'il rencontre. 
# Une telle recombinaison est susceptible de générer une autre particule (électron ou photon) mais la suite de l'histoire devient celle de la nouvelle particule.
# Un électron libéré dans l'atmosphère ne va donc presque nulle part.
# 
# Des dispositifs de type "canons à électrons" ont été conçus pour générer des bombardements d'électrons destinés à une grande variété d'applications (irradiation, imagerie, microscopie, luminescence, $\dots$).
# Le fonctionnement de ces canons procède en deux temps : 
# - l'_extraction_ : les électrons sont naturellement confinés dans la matière et il faut apporter une énergie minimum à celle-ci pour que soient libérés des électrons
# - l'_accélération_ : les électrons extraits sont dirigés dans la direction souhaitée par la force électrostatique créée par une accumulation de charge (par exemple positive) produite à cette fin. Cette mise en mouvement doit se faire dans le vide, sinon l'électron se recombinera très vite sur la première molécule qu'il rencontrera.
# 
# On peut ainsi piloter le mouvement des électrons dans le vide en choisissant la force qui guidera les électrons.
# En pratique - parce qu'il n'existe pas de "radar" pour les électrons - on mesure l'énergie d'impact des électrons, qui est reliée à leur vitesse de la façon suivante :
# $$
# \mathcal{E} = \frac{1}{2} m v^2.
# $$
# Dans un équipement de laboratoire, les énergies accessibles sont de l'ordre de 0.1 à 10 keV

# In[1]:


from IPython.display import display, Markdown
import numpy as np
m = 9.1093837015e-31
e = 1.602176634e-19
E = np.array ((0.1, 10)) * 1e3 * e
v = np.sqrt (2*E/m)
texte_a_afficher  = f"Cela correspond à des vitesses de ${v[0]/1e3:.0f}$ à ${v[1]/1e3:.0f}$ km/s, "
texte_a_afficher += f"c'est à dire ${v[0]*3.6:.0f}$ à ${v[1]*3.6:.0f}$ km/h"
display (Markdown (texte_a_afficher))


# Dans des synchrotrons, qui sont de grands instruments dédiés à la recherche scientifique (comme [SOLEIL](https://www.synchrotron-soleil.fr/fr), en région parisienne), des électrons sont emmenés dans des anneaux d'accélération jusqu'à des vitesses voisines de la vitesse de la lumière.
# A ces vitesses, il se produit un phénomène d'émission de lumière lorsque les électrons prennent un virage : ce phénomène est décrit par une loi de la relativité qui nous informe comment l'électron se départit d'une partie de son énergie sous la forme d'une photon lorsqu'il change de direction.

# ## Dans la matière

# ### Electrons de coeur
# Dans la matière, les électrons sont soumis à un très grand nombre de forces créées par tous les objets électriques de son environnement, comme les noyaux atomiques et les autres électrons.
# A l'échelle de l'électron, ces forces sont gigantesques et, depuis l'extérieur, on ne peut presque jamais produire de forces qui puissent rivaliser.
# Presque jamais, mais parfois oui. 
# Les forces les plus grandes sont celles qui lient les électrons avec leur noyaux : la présence des nombreuses charges positives des protons du noyau exercent une force considérable sur les électrons. Ceux-ci sont piégés _au coeur_ de l'atome où ils orbitent sans cesse autour de leur noyaux, à la façon des planètes autour d'une étoile.
# 
# ### Electrons de liaison
# Seulement, leur présence réduit d'autant la charge positive des noyau et, vu de l'extérieur, l'attraction d'un noyau entouré de ses électrons est plus faible que celle d'un noyau nu.
# C'est la raison pour laquelle certains électrons, les "derniers", sont moins liés à leur atome est peuvent être influencés par leur voisinage.
# Dans de nombreux cas, ces électrons sont mis en commun avec un atome voisin pour former une _liaison chimique_ tellement stable qu'aucune influence extérieure ne pourra, cette fois encore, agir avec assez d'intensité pour rompre la liaison.
# Les électrons de liaisons, comme ceux de coeur, sont immobiles.
# A la limite, de très fortes tensions sont susceptibles de conduire les électrons à sauter de laison en liaison : ils sont alors en mouvement pendant la brève durée des sauts et immobiles la majeure partie du temps.
# En moyenne, la vitesse est plutôt faible, et sa valeur exacte est déterminée par les conditions de l'expérience.

# In[2]:


# conductivité typique d'un polymère 1e-12 S/cm.
# 1 cm d'un morceau de polymère de section 0.5 x 0.5 mm²
# sous 1 Volt est traversé par un courant
S = 1e-12 # S/cm
R = 1/S * 1e-2 * 1e-2 / (5e-3 * 5e-3)
V = 1
courant = V / R
distance_saut = 1e-9
nb_chaines_paralleles = 1e6
vitesse = (courant * duree) / nb_chaines_paralleles / distance_saut
texte_a_afficher  = "Par exemple, pour un mince morceau de plastique (chaines de polymères) de 1 cm, "
texte_a_afficher += "aux extrémités duquel on applique une une tension de 1 V, "
texte_a_afficher += f"la vitesse des électrons est de l'ordre de {vitesse*1e9:.2f} nm/s"
display (Markdown (texte_a_afficher))


# ### Electrons libres
# Il reste une dernière possibilite : après la formation des liaisons, il reste encore des électrons qui ne sont pas très liés à leur atome.
# Ces électrons sont alors libres de leur mouvement dans la matière, à condition toutefois qu'elle soit bien ordonnée : il se trouve en effet que les irrégularités de la matière sont susceptibles de dévier les électrons de leur trajectoire, de la même façon que des rochers émergés de l'océan brisent des vagues.
# Cette condition est vérifiée dans les métaux où les atomes sont ordonnés dans l'espace avec une très grande régularité (mieux que 0.1 % de la distance inter-atomique) dans les trois directions de l'espace.
# Dans ce cas, les électrons libres peuvent atteindre des vitesses assez grandes pour ne plus distinguer les particules chargées séparément mais seulement un paysage flou, et neutre.
# Les vitesses que peuvent atteindre ces électrons sont gigantesques, par exemple 1280 km/s dans un cristal de lithium.
# Il faut préciser qu'aucune intervention n'est nécessaire pour que les électrons libres des métaux atteignent ces vitesses : c'est leur état spontané, même sans appliquer une tension, même à basse température, ils vont dans tous les sens.
# Mais ces vitesses sont si élevées que les défauts susceptibles de dévier les électrons sont rencontrés très souvent, même s'ils sont très peu nombreux.
# Ainsi, sous l'effet d'une tension, les électrons sont mis en mouvement dans une direction particulière, ils se déplacent chacun à une vitesse énorme, sont déviés de leur trajectoire un nombre de fois non moins énorme, de sorte que le bilan net du mouvement s'en trouve considérablement réduit : en somme l'électron qui se trouve à l'entrée se déplace très vite, est conduit vers la sortie par la force électromotrice due à la tension extérieure mais subit tellement de déviations qu'il va mettre un temps très important à atteindre la sortie.
# On peut définir une autre vitesse associé à ce processus, celle de l'_écoulement moyen_ des électrons.
# Par exemple, on peut calculer que pour un barreau lithium de 1 cm de long, soumis à une tension de 10 V, la vitesse d'écoulement n'est que de 1.35 mm/s.
# 
# En toute rigueur, on ne peut pas vraiment comparer la très grande vitesse des électrons libres avec celle d'écoulement moyen ni celle de l'électron dans le vide dans la mesure où il s'agit, pour les électrons libres, de la vitesse de propagation de l'onde sous la forme de laquelle les électrons se trouvent dans la matière.
# 
# C'est la limite de la question de la vitesse d'un électron : pour y répondre, il faut se poser la question de ce qu'est un électron. En physique, la nature d'un objet est déterminée par la façon la plus fidèle de décrire son comportement.
# En l'occurrence, il se comporte comme un projectile dans le vide et quand on parle d'écoulement moyen; lorsqu'on observe son comportement dans la matière à l'échelle microscopique l'image du projectile ne fonctionne pas
# Au contraire, c'est en considérant l'électron comme une onde, une vague, qu'on peut décrire et comprendre l'ensemble des phénomènes où il intervient.

# A mon avis, il était très difficile de fournir une réponse brève à ta question...
# 
# Joseph
