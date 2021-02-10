Python_Upgrade (v19)
Création : 21/01/2021
Dernière mise à jour : 09/02/2021 - 19:24
————
⚠️Script toujours en cours de développement ! ⚠️
Ce programme contient des fonctions python plus avancés et peut-être utilisées comme un module python à importer dans votre programme.

-----------------------------------------------------

Fonctions :


    super_print(screen , list , page , fill , valid)
    len2(object)
    AIsplit(letters , text , separator)
    list2print(list , lines)
    
-----------------------------------------------------

Dépendances :


    super_print() :
        ion module
        time module

    len2() :
        Pas de dépendances.

    AIsplit() :
        Pas de dépendances.

    list2print() :
        ion module
        time module
        
-----------------------------------------------------

Descriptions :


    super_print() : Une fonction print() extrêmement avancé et modulable. Une fonction qui peut créer des livres, si vous le voulez XD.
    Le paramètre "screen" (obligatoire) demande la résolution de votre écran (format : "lignes"x"lettres"). Si vous ne savez pas, indiquez juste si vous avez mis la police d'écriture Python par "0" ou "1" (uniquement sur les calculettes Numworks). False | 0 = Grande police d'écriture ; True | 1 = Petite police d'écriture ; 00x00 = résolution désirée
    Le paramètre "list" (obligatoire) vous demande de fournir au programme une liste contenant votre texte. (⚠️chaque séparation dans la liste désigne une ligne à l'écran⚠️).
    Le paramètre "page" (passif) désigne si vous voulez faire des pages à votre texte (par défaut "page=0"). False | 0 = pas de page ; 1 = automatique ; >1 = nombre de pages désiré.
    Le paramètre "fill" (passif) demande si vous souhaitez remplir l'écran, s'il n'y a pas assez de texte pour le faire (par défaut "fill=0"). False | 0 = pas de remplissage ; True | 1 = remplissage.(⚠️Le remplissage sera automatique si le paramètre "page" est à 1 ou >1 ⚠️).
    Le paramètre "valid" (passif) indique si vous souhaitez mettre un petit message dans la zone d'input (comme : OK, ou retour, ...)(par défaut "valid=0"). False | 0 = pas de message ; 1 = OK ; 2 = Retour ; 3 = Cancel.
    La fonction peut aussi renvoyer "True" si un message du paramètre "valid" est accepté sinon "False".

    len2() : Une fonction presque pareil à len(). Mais grâce à cette fonction vous pouvez lire absolument tout (chaine de nombre, caractère, ou des listes).

    AIsplit() : Une fonction split() très avancée. Une fonction qui vous retournera une liste avec chaque occurrence correspondant à une ligne de votre écran, et sans coupure de mot. Vous pouvez aussi changer le séparateur qui servira de découpe.
    Le paramètre "letters" (obligatoire) vous demande le nombre de lettres sur laquelle la découpe contera comme une ligne. Si vous ne le savez pas, indiquez juste si vous avez mis la police python en petit ou en grand (uniquement sur les calculettes Numworks) par "0" ou "1". 0 = grande police ; 1 = petite police ; >2 = nombre de lettres désirées.
    Le paramètre "text" (obligatoire) vous demande de fournir au programme une chaine de caractères contenant votre texte (⚠️Si vous avez des "\n" dans votre texte, veuillez les isolées d'espaces, pour un meilleur affichage⚠️).
    Le paramètre "separator" (passif) dit au programme ce qu'il doit considérer comme un mot (par défaut separator=" "), n'accepte pas separator="\n".

    list2print() : Une fonction un peu plus avancées que print(). Une fonction vous permettant de circuler dans une liste affichée à l'écran avec ↑ ou ↓.
    Le paramètre "list" demande de fournir à la fonction une liste à afficher.
    Le paramètre "lines" vous demande nombre de lignes de votre écran (pour ne pas voir le trucage).
    
-----------------------------------------------------

Concernant toute demande, problème, ou suggestion avec ce script, veuillez me contacter sur mon Discord : BTA_Susideur#5093.
