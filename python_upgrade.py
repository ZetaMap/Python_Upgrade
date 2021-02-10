from ion import keydown,KEY_LEFT,KEY_RIGHT,KEY_UP,KEY_DOWN,KEY_EXE,KEY_OK
from time import sleep

def super_print(screen,list,page=1,fill=0,valid=0):
### v Testing fonction v ###
  try:
    len(list)
    list.reverse()
    list.reverse()
  except TypeError:
    print("super_print() : \n\tErreur : 'list = {}'. Le contenu n'est pas une liste.\n".format(list))
    return
  except AttributeError:
    print("super_print() : \n\tErreur : 'list = {}'. Le contenu n'est pas une liste.\n".format(list))
    return
  try:
    screen+1
    __screen__="auto"
  except TypeError:
    __temp__=screen.split("x")
    if len(__temp__) == 2 and __temp__[0].isdigit() and __temp__[1].isdigit():
      __screen__="perso"
    else:  
      print("super_print() : \n\tErreur : 'screen = {}' Le format de résolution n'est pas valide. (format à utiliser : '<lignes>x<lettres>')\n".format(screen))
      return
  try:
    page+fill+valid+1
  except TypeError:
    print("super_print() : \n\tErreur : Les paramètres passifs de la fonction ne sont pas valides.\n")
    return
  except UnboundLocalError:
    print("super_print() : \n\tErreur : Les paramètres passifs de la fonction ne sont pas valides.\n")
    return
### ^ Testing fonction ^ ###

  def __init__(screen,list,page,__screen__):
    if __screen__ == "perso":
      screen=screen.split("x")
      lines,letters=int(screen[0]),int(screen[1])
    if __screen__ == "auto":
      if screen == 0 or screen == False:
        letters=27
        lines=11
      if screen == 1 or screen == True:
        letters=40
        lines=14
    Nb,index,Nb_page=len(list),0,0
    if page == 1 or page == True:
      page=Nb//(lines-1)
      if Nb%(lines-1): page=page+1
    return letters,lines,index,Nb,Nb_page,page
  
  def printing(list,Nb,index,lines,letters):
    try:
      print("")
      for i in range(Nb):
        print(list[index])
        index,lines=index+1,lines-1
    except IndexError: None
    return lines,index

  def filling(fill,lines):
    if fill == 1 or fill == True:
      for i in range(lines): print("")

  def page_indexing(letters,page,Nb_page):
    letters_space="  "
    for i in range(letters-len(">EXE to exit"+"Page "+"/"+str(Nb_page)+str(page))):
      letters_space=str(letters_space)+" "
    print(">EXE to exit{}Page {}/{}".format(letters_space,Nb_page,page),end="")
    return page,Nb_page

  def print_scan(lines,left,Nb,index):
    if left == 1:
      for i in range(Nb):
        if not index%lines: break
        index=index+1
      index=index-lines*2
    return index

  def scanAndprint(list,page,fill,Nb,Nb_page,index,lines,letters,left):
    if page == 0 or page == False:
      lines,index=printing(list,Nb,index,lines,letters)
      filling(fill,lines)

    if page == 1 or page == True or page >=2:
      index=print_scan(lines,left,Nb,index)
      if Nb>lines: Nb=lines
      lines,index=printing(list,Nb,index,lines,letters)
      filling(1,lines)
      page,Nb_page=page_indexing(letters,page,Nb_page)

### v Test line v ###
#    print("Nb:{} lines:{} index:{}".format(Nb,lines,index))
### ^ Test line ^ ###
    return index

  def validation(valid):
    if valid == 1: input("-->          _|OK|_           ")
    if valid == 2: input("-->        _|Retour|_         ")
    if valid == 3: input("-->        _|Cancel|_         ")
    if valid == 96: input("--> _|LoL it's a Easter Egg|_ ")
    if valid == 97: input("-->   _|Morgan le caca !|_    ")
    if valid == 98: input("-->     _|Tina la BG !|_      ")
    if valid == 99: input("-->    _|Made by Zackari|_    ")
    if valid == 100: input("-->    _|It's my name XD|_    ")
    if valid == 0 or valid == False: return False
    else: return True

  letters,lines,index,Nb,Nb_page,page=__init__(screen,list,page,__screen__)
  Nb_page=Nb_page+1
  index=scanAndprint(list,page,fill,Nb,Nb_page,index,lines,letters,0)
  sleep(0.2)
  while (page == 1 or page >= 2):
    if keydown(KEY_LEFT) and Nb_page < page+1 and Nb_page > 1:
      Nb_page=Nb_page-1
      index=scanAndprint(list,page,fill,Nb,Nb_page,index,lines,letters,1)
      sleep(0.2)

    if keydown(KEY_RIGHT) and Nb_page < page and Nb_page > 0:
      Nb_page=Nb_page+1
      index=scanAndprint(list,page,fill,Nb,Nb_page,index,lines,letters,0)
      sleep(0.2)

    if keydown(KEY_EXE):
      break
  return validation(valid)

######Fonction separator######

def len2(ocject):
  try:
    return len(object)
  except TypeError:
    return len(str("")+str(object)+str(""))

######Fonction separator######

def AIsplit(letters,text,separator=" "):
### v Testing fonction v ###
  try:
    letters+1
    text.isalpha()
  except TypeError:
    print("AIsplit() : \n\tErreur : 'letters = {}'. Le contenu n'est pas une chaine de nombres.\n".format(letters))
    return  
  except AttributeError:
    print("AIsplit() : \n\tErreur : 'text = {'. Le contenu n'est pas une chaine de caractères.\n".format(text))
    return
  try:
    len(separator)
    if separator == "":
      print("AIsplit() : \n\tErreur : 'separator = {}'. Le séparateur est vide.\n".format(separator))
      return
    if separator == "\n":
      print("AIsplit() : \n\tErreur : 'separator = \\n'. Le paramètre n'accepte pas le retour à la ligne ('\\n').\n")
      return
  except TypeError:
    print("AIsplit() : \n\tErreur : 'separator = {}'. Le contenu n'est pas une chaine de caractères.\n".format(separator))
    return
### ^ Testing fonction ^ ###

  def __init__(letters,text):
    if letters == 0: letters=27
    if letters == 1: letters=42
    index,Nb,__temp__,__cache__,__cutter__=0,len(text),"",separator,"\n"
    return letters,index,Nb,__temp__,__cache__,__cutter__
  
  def spliting(text,separator): return text.split(separator)

  def joining(text,letters,separator,index,Nb,__temp__,__cache__,__cutter__):
    worlds=text[index]
    for i in range(Nb):
      try:
        if (len(worlds+text[index+1]) >= letters) or  worlds.endswith("\n"):
          __temp__=__cutter__.join([__temp__,worlds])
          worlds,separator="",__cutter__       
        else:          
          index=index+1
          worlds=separator.join([worlds,text[index]])
          if separator == __cutter__: separator=__cache__
#        print(worlds)
      except IndexError: None
    if not  worlds == "": __temp__=__cutter__.join([__temp__,worlds])
    return __temp__,__cutter__
  
  letters,index,Nb,__temp__,__cache__,__cutter__=__init__(letters,text)
  text=spliting(text,separator)
  text,separator=joining(text,letters,separator,index,Nb,__temp__,__cache__,__cutter__)
  text=spliting(text,separator)
#  print(text)
  for i in range(text.count("")): text.remove("")
  return text

######Fonction separator######

def list2print(list,lines):
### v Testing fonction v ###
  try:
    lines+1
    list.reverse()
    list.reverse()
    if len(list) < lines:
      print("list2print() : \n\tErreur : 'lines = {}'. Le nombre de lignes doit être inférieur au nombre d'occurrences de la liste.\n".format(lines))
      return
  except TypeError:
    print("list2print() : \n\tErreur : 'lines = {}'. Le contenu n'est pas une chaine de nombres.\n".format(lines))
    return
  except AttributeError:
    print("list2print() : \n\tErreur : 'list = {}'. Le contenu n'est pas une chaine de nombres.\n".format(list))
    return
### ^ Testing fonction ^ ###

  def printing(list,index,lines):
    print("")
    for i in range(lines):
      print(list[index])
      index=index+1
    return index

  def up(list,index,lines):
    if index>lines:
      index=index-lines-1
      index=printing(list,index,lines)
    else: index=lines+1
    sleep(0.2)
    return index

  def down(list,index):
    if index<len(list):
      print(list[index])
      index=index+1
    sleep(0.2)
    return index
  
  index=printing(list,0,len(list))
  sleep(0.2)
  while True:
    if keydown(KEY_EXE) or keydown(KEY_OK): break
    if keydown(KEY_UP): index=up(list,index,lines)
    if keydown(KEY_DOWN): index=down(list,index)
  return

######Fonction separator######
