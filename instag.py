# a, b= 1>2, 2>3
# my_list= [a,b,a==b];print(my_list)

my_list = [[10,20,30],[40,50,60],[70,80,90]]
flattened = [x for temp in my_list for x in temp]


# output => [10, 20, 30, 40, 50, 60, 70, 80, 90]