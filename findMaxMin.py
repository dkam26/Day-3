def find_max_min(numbers):
  max_number=numbers[0]
  min_number=numbers[0]
  num=[]
  count=0
  counter=0
  le=len(numbers)
  for i in range(len(numbers)):
      if min_number is numbers[i]:
          count=count+1
  if count is le:
         num.append(count)
         counter=counter+1
  if counter is 1:
      return num
  else:
      for i in numbers:
         if i < min_number:
          min_number=i
         elif i > max_number:
          max_number=i
      if min_number is max_number:
            num.append(min_number)
      else:
           num.append(min_number)
           num.append(max_number)    
  return num
     
  
print(find_max_min([4,4,4,4]))