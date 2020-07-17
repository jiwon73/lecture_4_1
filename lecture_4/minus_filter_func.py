n_list=[1,20,-34,-20,10,100]
minus_arr=[]

for a in filter(lambda x: x<0, n_list):
    minus_arr.append(a)

print(minus_arr)

