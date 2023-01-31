# import random

# from faker import Faker

# fake = Faker()

# users = {}

# for i in range(10):
#    name = fake

# import random

# num = random.sample(range(10, 35), 5)

# print(num)



# task 3

# arr = [True, 1,1.3,3.3, 'str', 'qale']
# b = []
# num = []
# fl = []
# s = []
# for i in arr:
#    if type(i) == bool:
#       b.append(i) 
#    if type(i) == str:
#       s.append(i) 
#    if type(i) == int:
#       num.append(i) 
#    if type(i) == float:
#       fl.append(i) 
# print(b)
# print(num)
# print(fl)
# print(s)

# d = dict()

# d = {"pod": 1}

# d = list(range(1,42,3))
# pod1 = []
# [pod1.append(i) for i in d if i % 2 == 1]
# user = 25
# if pod1[0] < user and pod1[1] > user:
#    print('1 etaj')
# if pod1[1] < user and pod1[2] > user:
#    print('2 etaj')
# if pod1[2] < user and pod1[3] > user:
#    print('3 etaj')
# if pod1[3] < user and pod1[4] > user:
#    print('4 etaj')
# if pod1[4] < user and pod1[5] > user:
#    print('5 etaj')
# if pod1[5] < user and pod1[6] > user:
#    print('6 etaj')
# if pod1[6] < user and pod1[7] > user:
#    print('7 etaj')

# d = dict(name="John Doe", age=30)
# print(d) #{'name': 'John Doe', 'age': 30}

# d = {
#     "name":"John",
#     "surname":"Doe",
#     "age":20
# }
# print(d) #{'name': 'John', 'surname': 'Doe', 'age': 20}

# print(d["name"]) # John
# print(d["money"]) # KeyError: 'money'
# print(d.get("name")) # John - get_object_or_404 >> get or None
# print(d.get("money")) #  None
# k = ["monkey", "elephant"]
# v = [12,5]

# print(dict(zip(k,v))) # {'monkey': 12, 'elephant': 5}
# import random
# from faker import Faker as fake

# fake = fake()

# users = {}

# for i in range(30):
#     users = fake.name().split()
    
#     temp = {
#         f'{name.split(" ")[0].lower()}': random.randint(18,30)
#     }
#     users.update(temp)
#     if name.count('a') >= 2:
#       d_use.update(temp)
# print(users)

# task 1

# d = '12.30.2002'
# s_int = []
# da = d.split('.')
# for i in da:
#    if i[0] == 0:
#       del(i[0])
#    s_int.append(int(i))
# if s_int[0] == 2 and s_int[1] <= 28:
#    print(True)
# elif s_int[0] <= 12 and s_int[1] <= 31 and s_int[2] >= 1970 and s_int[2] <= 2023:
#    print(True)
# else:
#    print('Sanani to\'g\'ri kiriting')

# sl = 9
# clo = 24
# user = 22
# a = (clo - user) + sl
# print(a)

















