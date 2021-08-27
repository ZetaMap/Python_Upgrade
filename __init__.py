from ion import keydown,KEY_LEFT,KEY_RIGHT,KEY_UP,KEY_DOWN,KEY_EXE,KEY_OK
from time import sleep

LARGE_FONT = (27,11)
SMALL_FONT = (40, 14)

def print_book(screen, text, wholeWords=True):
  ### v Testing fonction v ###
  type_test(screen, tuple)
  if len(screen) != 2: raise IndexError("invalid resolution format. (accepted: (letters, lines))")
  for i in screen:
    type_test(i, int)
    if i < 2: raise ValueError("invalid resolution values. (min values: 2)")
  type_test(text, [str, list])
  type_test(wholeWords, bool)
  ### ^ Testing fonction ^ ###

  def main():
    index = (page-1)*lines
    _list = text[index:index*2 if index != 0 else lines]
    rest = lines-len(_list)

    print()
    for i in _list: print(i)
    for i in range(rest): print()
    print(mjust("[EXE]: exit ", " p.{}/{}".format(page,pages), letters))

  letters, lines, page = screen[0], screen[1]-1, 1
  if type(text) == str: text = words_wrap(text, letters, wholeWords).splitlines()
  else:
    text = []
    for i in text:
      temp = words_wrap(i, letters, wholeWords).splitlines()
      for ii in range(lines-len(temp)): temp += ['']
      text += temp
  textSize = len(text)
  pages = textSize//(lines+1)
  if textSize%(lines-1): pages+=1

  main()
  sleep(0.2)
  while True:
    if keydown(KEY_EXE) or keydown(KEY_OK): break
    elif keydown(KEY_LEFT) and page > 1:
      page-=1
      main()
      sleep(0.2)

    elif keydown(KEY_RIGHT) and page < pages:
      page+=1
      main()
      sleep(0.2)

######Fonction separator######

def len2(_object):
  try: return len(_object)
  except TypeError: 
    if type(_object) == type: return len(_object.__name__)
    else: return len(str(_object))

######Fonction separator######

def words_wrap(text, width, wholeWords=True, breakLongWords=True, wrapper='\n', limit=None, end=" [...]"):
### v Testing fonction v ###
  type_test(text, str)
  type_test(width, int)
  type_test(wholeWords, bool)
  type_test(breakLongWords, bool)
  type_test(wrapper, str)
  type_test(limit, int, True)
  if limit != None: 
    if limit < 0: return text
    elif limit < len(end): return ''
    elif limit == len(end): return end
    elif limit > len(text): limit = len(text)
  type_test(end, str)
### ^ Testing fonction ^ ###

  index, output, textSize = 0, "", len(text)

  if wholeWords:
    for i in range(textSize if limit == None or limit >= textSize else limit-len(end)):
      if index == width:
        if text[i] == ' ': 
          output += ' '
          continue
        elif text[i] == wrapper: continue

        try: test = cut(output, output.rindex(' '))
        except ValueError: 
          if breakLongWords: 
            test = cut(output, i)
            output = test[0]+wrapper+test[1]
          index = 0
          continue
        
        output = test[0].rstrip(' ')+wrapper+test[1][1:]
        index = len(test[1][1:])
      
      elif text[i] == wrapper: 
        if i > 1 and text[i-1] == ' ': output = output.rstrip(' ')
        if textSize-1 > i and text[i+1] == ' ': 
          output += ' '
          continue
        index = 0

      output += text[i]
      index += 1

    if limit != None and limit < textSize:
      if textSize-1 > i and text[i+1] != ' ': 
        try: output = cut(output, output.rindex(' '))[0]
        except ValueError: return end

      output += end
      test = output.rsplit(wrapper, 1)

      try: return insert(output, output.rindex(' '), wrapper) if len(test[1] if len(test) != 1 else test[0]) > width else output
      except ValueError:
        if breakLongWords: return insert(output, width, wrapper)
  
  else: 
    output = insert(text, width, wrapper, True)
    if limit != None: 
      output = cut(output, limit-len(end))[0]+end
      return insert(output, len(output)-len(output)//width, wrapper)
  
  return output.rstrip(wrapper)

######Fonction separator######

def print_list(screen, text, wholeWords=True, justTheList=False):
  ### v Testing fonction v ###
  type_test(screen, tuple)
  if len(screen) != 2: raise IndexError("invalid resolution format. (accepted: (letters, lines))")
  for i in screen:
    if i < 2: raise ValueError("invalid resolution values. (min values: 2)")
  type_test(text, [str, list])
  type_test(wholeWords, bool)
  type_test(justTheList, bool)
  ### ^ Testing fonction ^ ###

  def main():
    _list, loop = text[index:index+lines], min(lines, len(text))
    c =  ['^']

    for i in range(loop-2): 
      c += ['|']
    c += ['v']

    print()
    for i in range(loop): 
      print(_list[i].ljust(letters+1)+c[i])

  letters, lines, index = screen[0] if justTheList else screen[0]-2, screen[1], 0
  if type(text) == str: text = words_wrap(text, letters, wholeWords).splitlines()
  else: text = words_wrap('\n'.join(text), letters, wholeWords).splitlines()
  textSize = len(text)

  if justTheList: [print(i) for i in text]
  else:
    main()

    sleep(0.2)
    while True:
      if keydown(KEY_EXE) or keydown(KEY_OK): break
      elif keydown(KEY_UP) and index > 0:
        index-=1
        main()
        sleep(0.2)

      elif keydown(KEY_DOWN) and index < textSize-lines:
        index+=1
        main()
        sleep(0.2)

######Fonction separator######

def insert(_object, index, add, repeat=False):
### v Testing fonction v ###
  type_test(index, int)
  objectType = type_test(_object, [str, list, tuple])
  type_test(repeat, bool)
### ^ Testing fonction ^ ###

  _object, __temp__, save = list(_object), [], index
  for i in range(len(_object)):
    try:
      if i == index: 
        __temp__.append(str(add) if objectType == str else add)
        if repeat: index += save
  ### v Debug line v ###
  #    print(index, ':', i, ':', _object[i], ':', __temp__)
  ### ^ Debug line ^ ###
      __temp__.append(_object[i])
    except IndexError: ...
  if (not len(_object) % (save if save != 0 else 1)) and repeat == True: __temp__.append(str(add) if objectType == str else add)
  return ''.join(__temp__) if objectType == str else objectType(__temp__)

######Fonction separator######

def reverse(_object):
  if type(_object) == bool: return not _object
  
  elif type(_object) == str:
    output, index = "", len(_object)
    for i in range(index):
      output += _object[index-i-1]
    return output
  
  elif type(_object) == int:
    _object = str(_object)
    output, index = "", len(_object)
    for i in range(index):
      output += _object[index-i-1]
    return int(output)

  elif type(_object) == float:
    _object = str(_object)
    output, index = "", len(_object)
    for i in range(index):
      output += _object[index-i-1]
    return float(output)

  elif type(_object) == list: 
    output = _object.copy()
    output.reverse()
    return output

  elif type(_object) == dict:
    output = {}
    for (key, value) in _object.items():
      output.update({str(value): key})
    return output

  elif type(_object) == tuple:
    output, index = (), len(_object)
    for i in range(index):
      output += (_object[index-i-1],)
    return output
  
  else: raise TypeError("type '{}' isn't accepted".format(type(_object)))

######Fonction separator######

def mjust(left, right, lenght, fill=' '):
  ### v Testing fonction v ###
  type_test(left, str)
  type_test(right, str)
  type_test(lenght, int)
  type_test(fill, str)
  if len(fill) != 1: raise TypeError('The fill character must be exactly one character long')
  ### ^ Testing fonction ^ ###

  while len(left+right) < lenght: left += fill
  return left+right

######Fonction separator######

def type_test(_object, _type, canBeNone=False, withError=True, contentException=None):
  ### v Testing fonction v ###  
  if not callable(_type) and type(_type) == list:
    if len(_type) == 0: raise IndexError("the type list must have at least one occurrence")
    for i in _type: 
      if not callable(i): raise TypeError("the list must only contain types")
  else: _type = [_type]
  ### ^ Testing fonction ^ ###

  if canBeNone:
    for i in _type:
      if _object == None or type(_object) == i or _object == contentException: 
        correct = i
        break
      else: correct = False
  else:
    for i in _type:
      if type(_object) == i or (contentException != None and _object == contentException): 
        correct = i
        break
      else: correct = False

  if withError: 
    if correct != False: return correct
    else:
      typeList = ""
      for i in range(len(_type)): typeList += "'"+_type[i].__name__+("', " if i != len(_type)-2 else "' or ")
      error = "'{}' is not valid as type argument {}".format(type(_object).__name__, typeList.rstrip(" ,"))
      raise TypeError(error)
  else:
    if correct: return True
    else: return False

######Fonction separator######

def cut(string, index, repeat=False):
  ### v Testing fonction v ###
  type_test(string, str)
  type_test(index, int)
  type_test(repeat, bool)
  ### ^ Testing fonction ^ ###

  if repeat:
    output = []

    if index > 0:
      while len(string) != 0:
        output += [string[:index]]
        string = string[index:]
    else:
      while len(string) != 0:
        output += [string[index:]]
        string = string[:index]
      output.reverse()

    return output
  else: return [string[:index], string[index:]]

######Fonction separator######
