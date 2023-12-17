import re
def solution(my_string):
    answer=0
    for i in my_string:
      if i.isdigit():
        pass
      else:
        my_string=my_string.replace(i,' ')
    
    return sum(list(map(int,my_string.split())))