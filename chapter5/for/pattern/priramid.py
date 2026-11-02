numbers = [12, 5, 27, 9, 18, 27]
largest=numbers[0]
secondlarge=None
lenght=len(numbers)
for i in range(0,lenght):
     if(largest<numbers[i]):
          secondlarge=largest
          largest=numbers[i]
 
     if(numbers[i]>secondlarge and numbers[i]!=largest and numbers[i]<largest ):
          secondlarge=numbers[i]
print(largest)
print(secondlarge)