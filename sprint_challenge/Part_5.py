def part5(score_list):
    person = [0 for i in range(0, 11)]
    
    for score in score_list :
      try :
        if (score < 0) :
          continue
        person[int(score / 10)] += 1
      except:  # if score < 0 or 100 < score:
        print(person[int(score / 10)])
    
    print(f"{0} 점대 - : {person[0]} 명")
    for i in range(1, 11) :
      print(f"{i}0 점대 - : {person[i]} 명")