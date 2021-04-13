from ion import keydown,KEY_LEFT,KEY_RIGHT,KEY_UP,KEY_DOWN,KEY_EXE,KEY_OK
from time import sleep

def super_print(screen,list_,page=True,fill=False,valid=False):
### v Testing fonction v ###
  if not (type(screen) == bool or type(screen) ==  str): raise TypeError("\n\tParamètre 'screen' : Le contenu doit être un Booléen ou un Str.")
  if not type(list_) == list: raise TypeError("\n\tParamètre 'list_' : Le contenu n'est pas une liste.")
  if not(type(page) == int or type(page) == bool): raise TypeError("\n\tParamètre 'page' : Le contenu n'est pas valide.")
  if not type(fill) == bool: raise TypeError("\n\tParamètre 'fill' : Le contenu n'est un Booléen")
  if not(type(valid) == int or type(valid) == bool or valid == {"easter": 99}): raise TypeError("\n\tParamètre 'valid' : Le contenu n'est pas valide.")
### ^ Testing fonction ^ ###
  def __init__(screen,list_,page):
    try:
      screen+1
      if not screen: letters,lines=27,11
      if screen: letters,lines=40,14
    except TypeError:
      screen=screen.split("x")
      if len(screen) == 2 and screen[0].isdigit() and screen[1].isdigit(): lines,letters=int(screen[0]),int(screen[1])
      else: raise TypeError("\n\tParamètre 'screen' : Le format de résolution n'est pas valide. (format : '<lignes>x<lettres>')")
    Nb,index,Nb_page=len(list_),0,0
    if page:
      page=Nb//(lines-1)
      if Nb%(lines-1): page+=1
    return letters,lines,index,Nb,Nb_page,page
  
  def printing(list_,Nb,index,lines,letters):
    try:
      print()
      for i in range(Nb):
        print(list_[index])
        index+=1
        lines-=1
    except IndexError: ...
    return lines,index

  def filling(fill,lines):
    if fill:
      for i in range(lines): print()

  def page_indexing(letters,page,Nb_page):
    letters_space="  "
    for i in range(letters-len(">EXE to exit"+"Page "+"/"+str(Nb_page)+str(page))):
      letters_space=letters_space+" "
    print(">EXE to exit{}Page {}/{}".format(letters_space,Nb_page,page))
    return page,Nb_page

  def scanAndprint(list_,page,fill,Nb,Nb_page,index,lines,letters,left=False):
    if page == True:
      lines,index=printing(list_,Nb,index,lines,letters)
      filling(fill,lines)

    if page == True or page >=2:
      lines-=1
      if left:
        for i in range(Nb):
          if not index%lines: break
          index+=1
        index+=-lines*2
      if Nb>lines: Nb=lines
      lines,index=printing(list_,Nb,index,lines,letters)
      filling(True,lines)
      page,Nb_page=page_indexing(letters,page,Nb_page)
  ### v Debug line v ###
  #  print("Nb:{} lines:{} index:{}".format(Nb,lines,index))
  ### ^ Debug line ^ ###
    return index

  letters,lines,index,Nb,Nb_page,page=__init__(screen,list_,page)
  Nb_page+=1
  index=scanAndprint(list_,page,fill,Nb,Nb_page,index,lines,letters)
  sleep(0.2)
  while (page == True or page >= 2):
    if keydown(KEY_EXE): break
    if keydown(KEY_LEFT) and Nb_page < page+1 and Nb_page > 1:
      Nb_page-=1
      index=scanAndprint(list_,page,fill,Nb,Nb_page,index,lines,letters,True)
      sleep(0.2)

    if keydown(KEY_RIGHT) and Nb_page < page and Nb_page > 0:
      Nb_page+=1
      index=scanAndprint(list_,page,fill,Nb,Nb_page,index,lines,letters)
      sleep(0.2)

  if valid == False: return False
  else:  
    if valid == 1: input("-->          _|OK|_           ")
    if valid == 2: input("-->        _|Retour|_         ")
    if valid == 3: input("-->        _|Cancel|_         ")
    if valid == {"easter": 99}: input("--> _|LoL it's a Easter Egg|_ "); input("-->   _|Morgan le caca !|_    "); input("-->     _|Tina la BG !|_      "); input("-->    _|Made by Zackari|_    "); input("-->    _|It's my name XD|_    ")
    return True

######Fonction separator######

def len2(object):
  try: return len(object)
  except TypeError: 
    if type(object) == type: return len(str(object))-10
    else: return len(str(object))

######Fonction separator######

def AIsplit(letters,text,separator=" ",full=True):
### v Testing fonction v ###
  if not (type(letters) == int or type(letters) == bool): raise TypeError("\n\tParamètre 'letters' : Le contenu n'est pas un Int.")
  if letters < 1: raise ValueError("\n\tParamètre 'letters' : Le contenu doit être supérieur à 1.")
  if not type(text) == str: raise TypeError("\n\tParamètre 'text' : Le contenu n'est pas un Str.")
  if not type(separator) == str: raise TypeError("\n\tParamètre 'separator' : Le contenu n'est pas un Str.")
  if separator == "": raise ValueError("\n\tParamètre 'separator' : Le séparateur est vide.")
### ^ Testing fonction ^ ###
  def __main__(text,letters,separator):
    index,__temp__,back,worlds,cutter=0,"",separator,"","\n"
    worlds=insert(letters,text[index],cutter,True)
    while True:
      try:
        if not len(worlds+text[index+1]) >= letters:
          index+=1
          worlds=separator.join([worlds,text[index]])
          if separator == cutter: separator=back
        elif len(text[index+1]) >= letters:
          index+=1
          worlds=insert(letters,text[index],cutter)
          worlds=worlds.splitlines()
          try:
            text.insert(index+1,worlds[1])
            worlds.pop(1)
          except IndexError: ...
          worlds="".join(worlds)
        else:
          __temp__=cutter.join([__temp__,worlds])
          worlds,separator="",cutter 
  ### v Debug line v ###
  #      print(index,":",[worlds],":",((len(worlds+text[index]) >= letters) or worlds.endswith("\n")))
  ### ^ Debug line ^ ###
      except IndexError: break
    worlds="".join(worlds)
    if not worlds == "": __temp__=cutter.join([__temp__,worlds])
    return __temp__

  if letters == False: letters=27
  if letters == True: letters=42
  if separator == "\n": separator=" "
  if full: 
    text=text.split(separator)
    text=__main__(text,letters,separator)
  else: text=insert(letters, text,"\n",True)
  text=text.splitlines()
  for i in range(text.count("")): text.remove("")
  return text

######Fonction separator######

def list2print(list_,lines):
### v Testing fonction v ###
  if not type(list_) == list: raise TypeError("\n\tParamètre 'list_' : Le contenu n'est pas une liste.")
  if not type(lines) == int: raise TypeError("\n\tParamètre 'lines' : Le contenu n'est pas un Int.")
  if len(list_) < lines: raise IndexError("\n\tErreur : 'lines' doit être inférieur au nombre d'occurrences de 'list_'.")
### ^ Testing fonction ^ ###
  def printing(list_,index,lines):
    print()
    for i in range(lines):
      print(list_[index])
      index+=1
    return index

  def up(list_,index,lines):
    if index>lines+1:
      index+=-lines-1
      index=printing(list_,index-1,lines+1)
    sleep(0.2)
    return index

  def down(list_,index):
    if index<len(list_):
      print(list_[index])
      index+=1
    sleep(0.2)
    return index
  
  index=printing(list_,0,lines)
  sleep(0.2)
  while True:
    if keydown(KEY_EXE) or keydown(KEY_OK): break
    if keydown(KEY_UP): index=up(list_,index,lines)
    if keydown(KEY_DOWN): index=down(list_,index)
  return

######Fonction separator######

def insert(index,object,add,repeat=False):
### v Testing fonction v ###
  if not type(index) == int: raise TypeError("'index': string indices must be integers")
  if index < 1: raise ValueError("'index' must be greater than 1.")
  if type(object) == type: raise TypeError("cannot insert 'object' into a type")
  if not type(repeat) == bool: raise TypeError("'repeat' must be a boolean")
### ^ Testing fonction ^ ###
  __temp__,__save__='',index
  for i in range(len(object)+1):
    try:
      if i == index: 
        __temp__+=str(add)
        if repeat: index+=__save__
  ### v Debug line v ###
  #      print(index,":",i,":",__temp__)
  ### ^ Debug line ^ ###
      __temp__+=object[i]
    except IndexError: ...
  if (not len(object) % __save__) and repeat: __temp__+=str(add)
  return __temp__

######Fonction separator######
