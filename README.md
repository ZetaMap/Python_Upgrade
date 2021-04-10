Python_Upgrade (v23.4)
Création : 21/01/2021
Dernière mise à jour : 10/04/2021 - 20:15
###————
⚠️Programme en cours de développement !⚠️
Ce programme contient des fonctions python plus avancés et peut-être utilisé comme un module python à importer dans votre programme

---------- 
Fonctions :

    super_print(screen , list_ , page , fill , valid)

    len2(object)

    AIsplit(letters , text , separator , full)

    list2print(list_ , lines)

    insert(index , object , add , repeat)

---------- 
Dépendances :

    super_print() :

        ion module

        time module

    len2() :

        Pas de dépendances.

    AIsplit() :

        insert()

    list2print() :

        ion module

        time module

    insert() :

        Pas de dépendances.

---------- 
Descriptions :

    super_print() : Une fonction print() extrêmement avancé et modulable qui peut créer des livres, si vous le voulez XD. La fonction peut aussi renvoyer "True" si un message du paramètre "valid" est accepté sinon "False".

        "screen" (obligatoire) demande la résolution de votre écran (format : "lignes"x"lettres"). (uniquement sur les calculettes Numworks : "False" ou "True", si vous ne savez pas la résolution.). False = Grande police d'écriture ; True = Petite police d'écriture ; 00x00 = résolution désirée

        "list_" (obligatoire) vous demande de fournir au programme une liste contenant votre texte. (⚠️chaque séparation dans la liste désigne une ligne à l'écran⚠️)

        "page" (passif) désigne si vous voulez faire des pages à votre texte (par défaut : page=True). False | 0 = pas de page ; True | 1 = automatique ; >1 = nombre de pages désiré.

        "fill" (passif) demande si vous souhaitez remplir l'écran, s'il n'y a pas assez de texte pour le faire (par défaut : fill=False). False = pas de remplissage ; True = remplissage.(⚠️Le remplissage sera automatique si le paramètre "page" est à 1 ou >1 ⚠️).

        "valid" (passif) indique si vous souhaitez mettre un petit message dans la zone d'input (comme : OK, ou retour, ...)(par défaut : valid=False). False = rien ; 1 = OK ; 2 = Retour ; 3 = Cancel.


    len2() : Une fonction presque pareil à len(). Mais grâce à cette fonction, vous pouvez lire absolument tout (chaine de nombre, caractère ou des listes).


    AIsplit() : Une fonction split() très avancée, qui vous retournera une liste avec chaque occurrence correspondant à une ligne de votre écran. Vous pouvez aussi changer le séparateur qui servira de découpe, et lui dire si vous voulez que les mots soient entiers ou pas.

        "letters" (obligatoire) vous demande le nombre de lettres sur laquelle la découpe contera comme une ligne. (uniquement sur les calculettes Numworks : "0" ou "1", si vous ne savez pas.). 0 = grande police ; 1 = petite police ; >2 = nombre de lettres désirées.

        "text" (obligatoire) vous demande de fournir au programme une chaine de caractères contenant votre texte.

        "separator" (passif) dit au programme ce qu'il doit considérer comme un mot (par défaut : separator=" ").

        "full" (passif) dit au programme si vous voulez que les mots soient entiers ou pas lors de la découpe (par défaut : full=True).


    list2print() : Une fonction un peu plus avancées que print(). Une fonction vous permettant de circuler dans une liste affichée à l'écran avec ↑ ou ↓.

        "list_" (obligatoire) demande de fournir à la fonction une liste à afficher. (⚠️chaque séparation dans la liste désigne une ligne à l'écran⚠️)

        "lines" (obligatoire) vous demande nombre de lignes que votre écran peut afficher.


    insert() : Une fonction comme : list.insert(). Mais celle-ci peut introduire une chaine de caractères dans une autre à l'index donné.

        "index" (obligatoire) vous demande de lui fournir un index au quel il va venir introduire la chaine de caractères.

        "object" (obligatoire) donne au programme une chaine de caractères dans lequel il introduira l'autre.

        "add" (obligatoire) est la chaine de caractères qui sera introduite.

        "repeat" (passif) dit au programme si vous voulez que l'opération soit répété jusqu'au bout de la chaine de caractères.

---------- 
Concernant toute demande, problème ou suggestion avec ce script, veuillez me contacter sur mon Discord : BTA_Susideur#5093.
