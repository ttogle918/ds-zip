def selectionSort(li) :
    length = len(li)
    for i in range(length-1) :
      max_idx = i
      for j in range(i+1, length) :
        if li[max_idx] < li[j] :
          max_idx = j
      
      li[i], li[max_idx] = li[max_idx], li[i]
    return li


def bubbleSort(li) :
    length = len(li)
    for i in range(length-1) :
      for j in range(i+1, length) :
        if li[i] < li[j] :
          li[i], li[j] = li[j], li[i]
    return li

def insertionSort(li):
    for i in range(1, len(li)) :
      current = li[i]
      j = i-1
      
      while j >= 0 and li[j] < current :
        if current <= li[j] :
          break
        li[j+1] = li[j]
        j -= 1
        
      li[j+1] = current

    return li