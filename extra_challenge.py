         #app to find missing numbers in the given string
my_list = [ 1, 2, 3, 5, 6, 7, 9, ]

final_list = []

        #using function to find the missing numbers
for x in range(1,10):
    if x not in my_list:
       final_list.append(x)
        
print(final_list)

    
