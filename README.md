# Python_Upgrade (v10.3)

## Création : 21/01/2021 
## Dernière mise à jour : 29/10/2021 - 17:20
### **⚠️Programme en cours de développement !⚠️** 
### Ce programme contient des fonctions python plus avancés et peut-être utilisé comme un module python à importer dans votre programme.

### Installation
Pour installer ce programme il vous suffira de taper ``pip install python_upgrade`` dans une console, et pour le mettre à jour, tapez ``pip install --upgrade python_upgrade``. <br>
Une fois fait il vous suffit d'écrire ``import python_upgrade`` ou ``from python_upgrade import *``, dans votre programme, pour importer la librairie.

### Fonctions :
* **print_book**(text, screen ,  wholeWords , onlyOnePage , printFooter)
* **len2**(_object)
* **words_wrap**(text , width , wholeWords , wrapper , limit , end)
* **print_list**(text, screen, wholeWords , onlyOneIndex , printScrollbar)
* **insert**(_object , index , add , repeat)
* **reverse**(_object)
* **mjust**(left , right , width , fill)
* **type_test**(_object , _type , canBeNone, withError , contentException)
* **cut**(string , index , repeat)

### Dépendances :
* ion module
* time module

### Descriptions :
* **print_book() :**
  * Met en forme un texte aux dimensions donné, coupe le texte par page, et lance une boucle pour pouvoir y circuler. <br>Si 'text' est une liste, chaque occurrence de cette liste sera considérée comme une page.
  * paramètre **'wholeWords'** : Si False, la fonction placera juste un retour à la ligne si la largeur de la ligne est dépassé. (par défaut 'wholeWords'=True)
  * paramètre **'onlyOnePage'** : Affichera uniquement la page indiqué sans lancer la boucle. (par défaut 'onlyOnePage'=None)
  * paramètre **'printFooter'** : Si True, utilisera une ligne de l'écran pour afficher le bas de page. (par défaut 'printFooter'=True)

* **len2() :**
  * Retourne la longeur d'un objet. Fonctionne dans tout les type.
  * Exemple : 1111111 -> 7 ou 'abcde' -> 5

* **words_wrap() :**
  * Cette fonction permet d'envelopper/remplir le texte selon la largeur d'une ligne. <br>Cette fonction est moins avancée que **textwrap.TextWrapper()** mais comparée à cette fonction, celui-ci permet de garder la structure du texte et de couper automatiquement les mots qui sont plus long que 'width'.
  * Il est aussi possible de lui indiquer si on veut garder les mots entiers ("wholeWords"). Si False, la fonction placera simplement un saut de ligne lorsque 'width' est dépassé. 
  * paramètre **'wrapper'** : Indique à la fonction ce qu'elle doit considérer comme un mot. (par défaut 'wrapper'=espace)
  * paramètre **'limit'** : Spécifie la limite de caractères du texte. Si None, il n'y a pas de limite de caractères. (par défaut 'limit'=None)
  * paramètre **'end'** : La chaîne de caractère qui termine le texte si 'limit' est dépassé. Sa longueur est prise en compte dans 'limit'. 

* **print_list() :**
  * Découpe les lignes d'un texte en liste, imprime cette liste verticalement, et démarre une boucle pour pouvoir y circuler. <br>Si 'text' est une liste, chaque occurrence de cette liste sera considérée comme une ligne. 
  * paramètre **'wholeWords'** : Si False, la fonction placera simplement un saut de ligne lorsque la largeur de l'écran est dépassée. (par défaut 'wholeWords'=True)
  * paramètre **'onlyOneIndex'** : Affichera uniquement le texte à l'index donné sans démarrer la boucle. (par défaut 'onlyOneIndex'=None)
  * paramètre **'printScrollbar'** : Si True, utilisera 2 lettres par ligne à l'écran pour afficher la barre de défilement. (par défaut 'printScrollbar'=True) 

* **insert() :**
  * Permet d'insérer un objet dans un autre à un index donné. Le paramètre 'repeat' vous permet de répéter cette action. <br>Si 'repeat' est True : répétera sur toute la longueur<br>Si 'repeat' est un int : répétera le nombre de fois indiqué 

* **reverse() :**
  * Renvoie l'inverse de l'objet donné. Fonctionne avec presque tous les types.
  * Exemple : 1234 -> 4321 ou {'a': 1234} -> {1234: 'a'} 

* **mjust() :**
  * Renvoie une chaîne justifiée au milieu de longueur 'width'. <br>Le remplissage est effectué à l'aide du caractère de remplissage spécifié (par défaut, un espace).

* **type_test() :**
  * Permet de tester un objet avec un type ou une liste de types, et lui dire si elle doit renvoyer une erreur ou le type correct, par défaut 'withError'=True.
  * Il est également possible de lui dire si l'objet peut être None et/ou si vous souhaitez ignorer si l'objet est égale au contenu spécifié. 

* **cut() :**
  * Cette fonction coupe un objet à un index donné et retourne toujours une liste avec au moins 2 occurrences.
  * Elle est particulièrement utile lorsque l'on veut répéter cette action plusieurs fois, c'est le but du paramètre 'repeat'. <br>Si 'repeat' est True : répétera sur toute la longueur<br>Si 'repeat' est un int : répétera le nombre de fois indiqué 

**Concernant toute demande, problème ou suggestion avec ce script, c'est [ici](https://github.com/ZetaMap/Python_Upgrade/issues/new).**
