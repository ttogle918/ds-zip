from posixpath import split


def added_word(test_str1, test_str2):
    splited1 = test_str1.split(' ')
    splited2 = test_str2.split(' ')
    
    if len(splited1) < len(splited2) and splited1 == splited2[:len(splited1)] :
      return ' '.join(splited2[len(splited1):])
    return None

    # case 1
    # length_1 = len(test_str1)
    # length_2 = len(test_str2)
    # if length_1 > length_2 :
    #   return None
    
    # if test_str1[:length_1] == test_str2[:length_1] :
    #   return test_str2[length_1:]
    # return None
