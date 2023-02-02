# c=int(input("enter the number of row :"))
# x = range(c)
# print(x)
#
# for n in x:
#     print("")
#     for y in x:
#         if (y <= n):
#             print("*", end='')

#
# c = int(input("enter the number of row :"))
# for n in range(1, c + 1):
#     for y in range(1, (c - n) + 1):
#         print(" ", end='')
#
#     for y in range(1, (n + 1)):
#         print("*", end="")
#     print()
###########################################################################################################
# string = input("inter the string :")
#
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# result = ""
#
# for i in range(len(string)):
#     if string[i] not in vowels:
#         result = result + string[i]
#
# print("\nAfter removing Vowels: ", result)
##########################################################################################################
# numberOfString=int(input("Enter the number of string list itemes :"))
# stringList=[]
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# for i in range(0,numberOfString):
#     stringList.append(input("Enter the sting : "))
# def my_function():
#     for r in stringList:
#         result=""
#         for z in r:
#             if (z not in vowels):
#                 result += z
#         print(result)
#
# my_function()
###############################################################################################################
# def calculate_area(name,dim1,dim2=1):
#     name = name.lower()
#
#     if name == "rectangle":
#         rect_area = dim1 * dim2
#         print(f"The area of rectangle is{rect_area}.")
#     elif name == "square":
#         sqt_area = dim1 * dim1
#         print(f"The area of square is{sqt_area}.")
#     elif name == "triangle":
#         tri_area = 0.5 * dim1 * dim2
#         print(f"The area of triangle is{tri_area}.")
#     elif name == "circle":
#         pi = 3.14
#         circ_area = pi * dim1 * dim1
#         print(f"The area of circle is{circ_area}.")
#     elif name == 'parallelogram':
#         para_area = dim1 * dim2
#         print(f"The area of parallelogram is{para_area}.")
#     else:
#         print("Sorry! This shape is not available")
#
#
# print("Calculate Shape Area")
# shape_name = input("Enter the name of shape whose area you want to find: ")
# dim1 = int(input("Enter the dim1 of shape whose area you want to find: "))
# dim2 = int(input("Enter the dim2 of shape whose area you want to find: "))
# # function calling
# calculate_area(shape_name, dim1, dim2)
