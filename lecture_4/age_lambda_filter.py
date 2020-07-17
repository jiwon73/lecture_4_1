ages=[34,25,17,13,54]

print('성년리스트')

for a in filter(lambda x: x>=19, ages): #filter는 t/f를 반환하는 함수를 만들어서 사용
    print(a)
