from ion import keydown, KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, KEY_EXE, KEY_OK
from time import sleep

__all__ = [
  "print_book",
  "len2",
  "words_wrap",
  "print_list",
  "insert",
  "reverse",
  "mjust",
  "type_test",
  "cut"
]
# screen resolution of Numworks
LARGE_FONT = (29,11)
SMALL_FONT = (42, 14)


###############################

def print_book(text, screen=LARGE_FONT, wholeWords=True, onlyOnePage=None, printFooter=True):
  """Lay out a text ('text') with the given dimensions ('screen'), split the text by page, and start a loop to be able to circulate in it.
  \nIf 'text' is a list, each occurrence of this list will be considered a page.

  \tparameter 'wholeWords': If False, the function will just place a line break when screen width is exceeded. (default 'wholeWords'=True)
  \tparameter 'onlyOnePage': Will only display the indicated page without launching the loop. If 'onlyOnePage'>max_page or 'onlyOnePage'<-max_page: raise IndexError(). (default 'onlyOnePage'=None)
  \tparameter 'printFooter': If True, will use a line on the screen to display the footer. (default 'printFooter'=True)
  """
  ### v Testing fonction v ###
  type_test(screen, tuple)
  if len(screen) != 2: raise IndexError("invalid resolution format. (accepted: (letters, lines))")
  for i in screen:
    type_test(i, int)
    if i < 2: raise ValueError("invalid resolution values. (min values: 2)")
  type_test(text, [str, list])
  type_test(wholeWords, bool)
  type_test(onlyOnePage, int, True)
  type_test(printFooter, bool)
  ### ^ Testing fonction ^ ###

  def main():
    index = page*lines
    _list = text[index:index*2 if index != 0 else lines]

    print()
    for i in _list: print(i)
    for i in range(lines-len(_list)): print()
    if printFooter: print(mjust("[EXE]: exit ", " p.{}/{}".format(page+1,pages), letters))

  letters, lines, page = screen[0], screen[1]-1 if printFooter else screen[1], 0
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
  
  if onlyOnePage != None:
    if onlyOnePage >= 0: page = onlyOnePage
    else: page = pages-onlyOnePage
    if page < 0 or page >= pages: raise IndexError("'page' must be greater than 0 and lower than "+str(pages-1))

  main()
  if onlyOnePage == None:
    sleep(0.2)
    while True:
      if keydown(KEY_EXE) or keydown(KEY_OK): break
      elif keydown(KEY_LEFT) and page > 0:
        page-=1
        main()
        sleep(0.2)

      elif keydown(KEY_RIGHT) and page < pages-1:
        page+=1
        main()
        sleep(0.2)

######Fonction separator######

def len2(_object):
  """Returns the length of an object. Works with all types.
  \nExample: 1111111 -> 7 or 'abcde' -> 5
  """
  try: return len(_object)
  except TypeError: 
    if type(_object) == type: return len(_object.__name__)
    else: return len(str(_object))

######Fonction separator######

def words_wrap(text, width, wholeWords=True, wrapper=' ', limit=None, end=" [...]"):
  """This function allows to wrap/fill the text ('text') according to the width of a line ('width'). 

  \nThis function is less advanced than textwrap.TextWrapper() but compared to this function,
  this one allows to keep the structure of the text and to automatically cut the words which are larger than 'width'.

  \nIt is also possible to indicate to him if we want to keep the whole words ('wholeWords'). 
  If 'wholeWords' = False, the function will just place a line break when 'width' is exceeded.

  \tparameter 'wrapper': Tells the function what to consider a word. (default 'wrapper'=space character)
  \tparameter 'limit': Specifies the character limit of the text. If 'limit'=None, there is no character limit. (default 'limit'=None)
  \tparameter 'end': the string that ends the text if 'limit' is exceeded. Its length is taken into account in 'limit'.
  """
  ### v Testing fonction v ###
  type_test(text, str)
  type_test(width, int)
  type_test(wholeWords, bool)
  type_test(wrapper, str)
  type_test(limit, int, True)
  if limit != None: 
    if limit < 0: return text
    elif limit < len(end): return ''
    elif limit == len(end): return end
  type_test(end, str)
  ### ^ Testing fonction ^ ###

  output, wrapperSize, lines = "", len(wrapper), text.splitlines()
  
  for i, line in enumerate(lines):
    linesSize, line = len(lines), cut(line, width)
    
    if wholeWords:
      t = not (line[0].endswith(wrapper) or line[1].startswith(wrapper))
      if wrapper in line[0].lstrip(wrapper) and t and line[1] != '':
        line[0] = line[0].rstrip(wrapper)
        test = cut(line[0], line[0].rindex(wrapper))
        line[0], line[1] = test[0], test[1][0 if t else wrapperSize:]+line[1]
        
    output += line[0].rstrip(wrapper)+'\n'
    if line[1] != '':
      if i < linesSize: lines.insert(i+1, line[1][wrapperSize if line[1].startswith(wrapper) else 0:])
      else: lines.append(line[1][wrapperSize if line[1].startswith(wrapper) else 0:])

  if limit != None:
    output = cut(output, limit-len(end))

    if wholeWords and len(''.join(output)) > limit-wrapperSize: 
      return cut(output[0], output[0].rindex(wrapper) if wrapper in output[0] else 0)[0]+end
    
    else: return output[0].rstrip('\n'+wrapper)
  else: return output.rstrip('\n'+wrapper)

######Fonction separator######

def print_list(text, screen=LARGE_FONT, wholeWords=True, onlyOneIndex=None, printScrollbar=True):
  """Cut the lines of a text ('text') into a list, print this list vertically, and start a loop to be able to circulate in it.
  \nIf 'text' is a list, each occurrence of this list will be considered as a line.
 
  \tparameter 'wholeWords': If False, the function will just place a line break when screen width is exceeded. (default 'wholeWords'=True)
  \tparameter 'onlyOneIndex': Will only display the text at the given index without start the loop. If 'onlyOneIndex'>max_index or 'onlyOneIndex'<-max_index: raise IndexError().
  \tparameter 'printScrollbar': If True, will use 2 letters per line on the screen to display the scrollbar. (default 'printScrollbar'=True)
  """
  ### v Testing fonction v ###
  type_test(screen, tuple)
  if len(screen) != 2: raise IndexError("invalid resolution format. (accepted: (letters, lines))")
  for i in screen:
    if i < 2: raise ValueError("invalid resolution values. (min values: 2)")
  type_test(text, [str, list])
  type_test(wholeWords, bool)
  type_test(onlyOneIndex, int, True)
  type_test(printScrollbar, bool)
  ### ^ Testing fonction ^ ###

  def main():
    _list = text[index:index+lines]
    scrollbar = ['^']

    # I don't finish this part
    if printScrollbar:
      for i in range(lines-2): scrollbar += ['#'] if False else ['|']
      scrollbar += ['v']
    ##########################

    print()
    if printScrollbar:
      for i in range(lines): 
        try: print(_list[i].ljust(letters+1)+scrollbar[i])
        except IndexError: print(''.ljust(letters+1)+scrollbar[i])    
    else:
      for i in range(lines): 
        try: print(_list[i])
        except IndexError: print()  

  letters, lines, index = screen[0]-2 if printScrollbar else screen[0], screen[1], 0
  if type(text) == str: text = words_wrap(text, letters, wholeWords).splitlines()
  else: text = words_wrap('\n'.join(text), letters, wholeWords).splitlines()
  textSize = len(text)

  if onlyOneIndex != None:
    if onlyOneIndex >= 0: index = onlyOneIndex
    else: index = textSize-onlyOneIndex
    if index < 0 or index >= textSize: raise IndexError("'index' must be greater than 0 and lower than "+str(textSize-1))
  
  main()
  if onlyOneIndex == None:
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
  """Allows you to insert an object ('add') into another object ('_object') at a given index ('index').
  \nThe 'repeat' parameter allows you to repeat this action.
  \tif 'repeat' is True: repeat along the entire length 
  \tif 'repeat' is type int: repeat the number of times indicated
  """
  ### v Testing fonction v ###
  _type = type(_object)
  isnum = _type == float or _type == int
  if isnum and type(add) != int:
    raise TypeError("if '_object' is a type int or float, 'add' must be type int")
  elif _type == dict and type(add) != dict: 
    raise TypeError("if '_object' is a type dict, 'add' must be type dict")
  else: iter(_object)
  type_test(index, int)
  type_test(repeat, [bool, int])
  if type(repeat) == int and repeat <= 0: return _object
  ### ^ Testing fonction ^ ###
  
  if isnum: 
    if index > len(str(_object)) or index*-1 > len(str(_object)): return _object
    return _type(str(add).join(cut(str(_object), index, repeat)))
  
  else:
    cuted = cut(_object, index, repeat)
    if _type == dict:
      output = {}

      output.update(cuted[0])
      for i in range(1, len(cuted)):
        output.update(add) 
        output.update(cuted[i])
      
    else: 
      output = []
      for i in cuted:
        for ii in i: output.append(ii)
        output.append(add)
      output.pop()

    if _type == str:
      for i in range(len(output)): output[i] = str(output[i])
      return ''.join(output)
    else: 
      try: return _type(output)
      except TypeError as e: raise TypeError("parameter 'add': "+str(e))

######Fonction separator######

def reverse(_object):
  """Returns the inverse of the given object. Works with almost all types.
  \nExample: 1234 -> 4321   or   {'a': 1234} -> {1234: 'a'}
  """
  try: iter(object)
  except TypeError: iterable = False
  else: iterable = True
  ref = type(_object)
  
  if type(_object) == bool: return not _object
  
  elif type(_object) == str or type(_object) == int or type(_object) == float:
    if type(_object) != str: _object = str(_object) 
    output, index = "", len(_object)
    for i in range(index):
      output += _object[index-i-1]
    return output if ref == str else ref(output)

  elif type(_object) == complex:
    output = str(_object)[1:-2].split('+')
    return complex(int(output[1]), int(output[0]))

  elif type(_object) == dict:
    output = {}
    for (key, value) in _object.items():
      try: output.update({value: key})
      except TypeError: output.update({str(value): key})
    return output
  
  elif iterable: 
    if type(_object) != list: _object = list(_object) 
    _object.reverse()
    return _object if ref == list else ref(_object)

  else: raise TypeError("type '{}' isn't accepted or iterable".format(type(_object)))

######Fonction separator######

def mjust(left, right, width, fill=' '):
  """Return a middle-justified string of length 'width'.
  \nPadding is done using the specified fill character (default is a space).
  """
  ### v Testing fonction v ###
  type_test(left, str)
  type_test(right, str)
  type_test(width, int)
  type_test(fill, str)
  if len(fill) != 1: raise TypeError("The fill character must be exactly one character long")
  ### ^ Testing fonction ^ ###

  while len(left+right) < width: left += fill
  return left+right

######Fonction separator######

def type_test(_object, _type, canBeNone=False, withError=True, contentException=None):
  """Allows you to test an object ('_object') with a type or a type list ('_type'), 
  and tell it if we want it to return an error or the correct type ('withError'), by default 'withError' = True.

  \nIt is also possible to tell it if the object can be None ('canBeNone') 
  and/or if you want to ignore a content ('contentException').
  """
  ### v Testing fonction v ###  
  if not callable(_type) and (type(_type) == list or type(_type) == tuple):
    if len(_type) == 0: raise IndexError("the type list must have at least one occurrence")
    for i in _type: 
      if not callable(i): raise TypeError("the list must only contain types")
  else: _type = [_type]
  ### ^ Testing fonction ^ ###

  if canBeNone:
    for i in _type:
      if _object == None or type(_object) == i: 
        correct = i
        break
      elif _object == contentException: 
        correct = True
        break
      else: correct = False
  else:
    for i in _type:
      if type(_object) == i: 
        correct = i
        break
      elif contentException != None and _object == contentException:
        correct = True
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

def cut(_object, index, repeat=False):
  """This function cut a object to a given index and always returns a list with at least 2 occurrences.
  \nShe's especially useful when one wants to repeat this action several times, it is the purpose of the 'repeat' parameter.
  \tif 'repeat' is True: repeat along the entire length 
  \tif 'repeat' is type int: repeat the number of times indicated
  """
  ### v Testing fonction v ###
  _type, state = type(_object), index < 0
  isnum = _type == float or _type == int
  if isnum: _object = str(_object)
  type_test(index, int)
  repeatIsInt = type_test(repeat, [bool, int]) == int
  if repeatIsInt and repeat <= 0:
    if state: return [float("nan") if isnum else _type(), _object]
    else: return [_object, float("nan") if isnum else _type()]
  ### ^ Testing fonction ^ ###

  if repeatIsInt: repeat -= 1
  if state: index *= -1
  output, save, n = [], index, 0

  if _type == dict:
    output.append({})
    keys = list(_object.keys())
    if state: keys.reverse()
      
    for i in range(len(_object)):
      if i == index:
        n += 1
        output.append({})
        if repeat:
          if repeatIsInt: repeat -= 1
          index += save
      output[n].update({keys[i]: _object[keys[i]]})

    if state:
      for i in range(len(output)):
        items = list(output[i].items())
        items.reverse()
        output[i] = dict(items)
      output.reverse()

  else:
    output.append([])
    content = list(iter(_object))
    if state: content.reverse()
    
    for i, value in enumerate(content): 
      if i == index:
        n += 1
        output.append([])
        if repeat:
          if repeatIsInt: repeat -= 1
          index += save
      output[n].append(value)
    
    if state: output.reverse()
    for i in range(len(output)):
      if state: output[i].reverse()

      if _type == str: output[i] = ''.join(output[i])
      elif isnum: 
        test = ''.join(output[i])
        output[i] = float("nan") if test == '' else _type(test)
      else: output[i] = _type(output[i])
    
  if len(output) == 1: 
    if state: output.insert(0, float("nan") if isnum else _type())
    else: output.append(float("nan") if isnum else _type())
  return output

######Fonction separator######