def is_anagram(str1,str2):

   if len(str1)==len(str2) and sorted(str1)==sorted(str2):
      return True
   else:
    return False
#print(is_anagram('listen','silent'))
