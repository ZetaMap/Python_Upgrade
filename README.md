Python_Upgrade (v6.1)<br />
Création : 21/01/2021<br />
Dernière mise à jour : 26/05/2021 - 17:40<br />
————<br />
<strong>⚠️Programme en cours de développement !⚠️</strong><br />
Ce programme contient des fonctions python plus avancés et peut-être utilisé comme un module python à importer dans votre programme.
<ul></ul>----------
Fonctions :<br>
<ul>
<li>super_print(screen , list_ , page , fill , valid)</li></ul>
<ul>
 <li>len2(object)</li></ul>
<ul>
<li>AIsplit(letters , text , separator , full)</li></ul>
 <ul>
<li>list2print(list_ , lines)</li></ul>
<ul>
<li>insert(index , object , add , repeat)</li></ul>
<ul>
<li>reverse(object)</li></ul>
<ul></ul>----------
Dépendances :<br>
<ul>
<li>ion module</li></ul>
<ul>
<li>time module</li></ul>
<ul></ul>----------
Descriptions :<br>
<ul>
<li><strong>super_print() :</strong> Une fonction print() extrêmement avancé et modulable qui peut créer des livres, si vous le voulez XD. La fonction peut aussi renvoyer "True" si un message du paramètre "valid" est accepté sinon "False".</li></ul>
<ul>
<ul><li>"screen" <strong>(obligatoire)</strong> demande la résolution de votre écran (format : "lignes"x"lettres"). (uniquement sur les calculettes Numworks : "False" ou "True", si vous ne savez pas la résolution.). False = Grande police d'écriture ; True = Petite police d'écriture ; 00x00 = résolution désirée</li></ul></ul>
<ul>
<ul><li>"list_" <strong>(obligatoire)</strong> vous demande de fournir au programme une liste contenant votre texte. <strong>(⚠️chaque séparation dans la liste désigne une ligne à l'écran⚠️)</strong></li></ul></ul>
<ul>
<ul><li>"page" <strong>(passif)</strong> désigne si vous voulez faire des pages à votre texte (par défaut : page=True). False | 0 = pas de page ; True | 1 = automatique ; >1 = nombre de pages désiré.</li></ul></ul>
<ul>
<ul><li>"fill" <strong>(passif)</strong> demande si vous souhaitez remplir l'écran, s'il n'y a pas assez de texte pour le faire (par défaut : fill=False). False = pas de remplissage ; True = remplissage.<strong>(⚠️Le remplissage sera automatique si le paramètre "page" est à 1 ou >1 ⚠️)</strong>.</li></ul></ul>
<ul>
<ul><li>"valid" <strong>(passif)</strong> indique si vous souhaitez mettre un petit message dans la zone d'input (comme : OK, ou retour, ...)(par défaut : valid=False). False = rien ; 1 = OK ; 2 = Retour ; 3 = Cancel.</li></ul></ul><br>
<ul>
<li><strong>len2() :</strong> Une fonction presque pareil à len(). Mais grâce à cette fonction, vous pouvez lire absolument tout (chaine de nombre, caractère ou des listes).</li></ul><br>
<ul>
<li><strong>AIsplit() :</strong> Une fonction split() très avancée, qui vous retournera une liste avec chaque occurrence correspondant à une ligne de votre écran. Vous pouvez aussi changer le séparateur qui servira de découpe, et lui dire si vous voulez que les mots soient entiers ou pas.</li></ul>
<ul>
<ul><li>"letters" <strong>(obligatoire)</strong> vous demande le nombre de lettres sur laquelle la découpe contera comme une ligne. (uniquement sur les calculettes Numworks : "0" ou "1", si vous ne savez pas.). 0 = grande police ; 1 = petite police ; >2 = nombre de lettres désirées.</li></ul></ul>
<ul>
<ul><li>"text" <strong>(obligatoire)</strong> vous demande de fournir au programme une chaine de caractères contenant votre texte.</li></ul></ul>
<ul>
<ul><li>"separator" <strong>(passif)</strong> dit au programme ce qu'il doit considérer comme un mot (par défaut : separator=" ").</li></ul></ul>
<ul>
<ul><li>"full" <strong>(passif)</strong> dit au programme si vous voulez que les mots soient entiers ou pas lors de la découpe, sauf si il est obligé de couper. (par défaut : full=True)</li></ul></ul><br>
<ul>
<li><strong>list2print() :</strong> Une fonction un peu plus avancées que print(). Une fonction vous permettant de circuler dans une liste affichée à l'écran avec &uarr; ou &darr;.</li></ul>
<ul>
<ul><li>"list_" <strong>(obligatoire)</strong> demande de fournir à la fonction une liste à afficher. <strong>(⚠️chaque séparation dans la liste désigne une ligne à l'écran⚠️)</strong></li></ul></ul>
<ul>
<ul><li>"lines" <strong>(obligatoire)</strong> vous demande nombre de lignes que votre écran peut afficher.</li></ul></ul><br>
<ul>
<li><strong>insert() :</strong> Une fonction comme : list.insert(). Mais celle-ci peut introduire une chaine de caractères dans une autre à l'index donné.</li></ul>
<ul>
<ul><li>"index" <strong>(obligatoire)</strong> vous demande de lui fournir un index au quel il va venir introduire la chaine de caractères.</li></ul></ul>
<ul>
<ul><li>"object" <strong>(obligatoire)</strong> donne au programme une chaine de caractères dans lequel il introduira l'autre.</li></ul></ul>
<ul>
<ul><li>"add" <strong>(obligatoire)</strong> est la chaine de caractères qui sera introduite.</li></ul></ul>
<ul>
<ul><li>"repeat" <strong>(passif)</strong> dit au programme si vous voulez que l'opération soit répété jusqu'au bout de la chaine de caractères.</li></ul></ul><br>
<ul>
<li><strong>reverse() :</strong> Une fonction plus avancer que sont original. Elle peut inverser des objets dans presque tous les types (str, list, dict, tuple).</li></ul>
<ul></ul>----------
<strong>Concernant toute demande, problème ou suggestion avec ce script, veuillez me contacter sur mon Discord : BTA_Susideur#5093.</strong>
