value=input("enter the value")
count=0
for i in range(0,len(value)):
    match(value[i]):
        case 'a'|'A'|'U'|'u'|'O'|'o'|'I'|'i'|'E'|'e':
            count+=1
print(count)