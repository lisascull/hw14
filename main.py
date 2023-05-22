#1
A = {'Ivan', 'Stefan', 'Nasty', 'Ian'}
B = {'Nasty', 'Ian', 'Mykola', 'Lola'}

intersection = A.intersection(B)
print(intersection)

A = {'Ivan', 'Stefan', 'Nasty', 'Ian'}
B = {'Nasty', 'Ian', 'Mykola', 'Lola'}

difference = B.difference(A)
print(difference)
#2
def CamelCase_to_snakecase(strings):
    snakecase_strings = []
    for string in strings:
        snakecase = ""
        for i, srt in enumerate(string):
            if i and srt.isupper():
                snakecase += "_"
            snakecase += srt.lower()
        snakecase_strings.append(snakecase)
    return snakecase_strings

CamelCase = ["FirstItem", "FriendsList", "MyTuple"]
snakecase = CamelCase_to_snakecase(CamelCase)
print(snakecase)