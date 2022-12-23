# Little tool that crawls through directories/subdirectories

import os
import re
import sys

total = 0.0
count = 0

def check(module):
  '''
  apply pylint to the file specified if it is a *.py file
  '''
  global total, count

  if module[-3:] == ".py":

    print "CHECKING ", module
    pout = os.popen('pylint --rcfile=.pylintrc %s'% module, 'r')
    for line in pout:
      if  re.match("E....:.", line):
        print line
      if "Your code has been rated at" in line:
        print line
        score = re.findall("\d+.\d\d", line)[0]
        total += float(score)
        count += 1
  
if __name__ == "__main__":
  try:
    print sys.argv   
    BASE_DIRECTORY = sys.argv[1]
  except IndexError:
    print "no directory specified, defaulting to current working directory"
    BASE_DIRECTORY = os.getcwd()

  print "looking for *.py scripts in subdirectories of ", BASE_DIRECTORY 
  for root, dirs, files in os.walk(BASE_DIRECTORY):
    for name in files:
      filepath = os.path.join(root, name)
      list_of_ignore = ['migrations', 'movies']
      #skip any directories if they're contained in the list
      if any(word in root for word in list_of_ignore):
        continue
      check(filepath)
      
  print "==" * 50
  print "%d modules found"% count
  print "AVERAGE SCORE = %.02f"% (total / count)