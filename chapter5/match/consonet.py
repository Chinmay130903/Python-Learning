n=input("enter a sigle charatcter")

match n:
    case 'a'|'e'|'i'|'o'|'u'|'A'|'E'|'I'|'O'|'U':
        print("vowel")
    case _:
        print("consont")
        