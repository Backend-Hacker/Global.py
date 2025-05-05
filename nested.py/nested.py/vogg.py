# vom_1 = int(input("input the first number:"))
# vom_2 = int(input("input the second number:"))
# sum = vom_1 +vom_2
# print(sum)

# a = "kiran"
# a = 5
# a = 5.77
# print(type(a))


# Python allows you to assign values to multiple variables in one line:

# a , b , c , d = "dog", "frog", "apple" , "banana"
# print(a)
# print(b)
# print(c)
# print(d)

# you can assign the same value to multiple variables in one line:

# kiran = anjali = shrijana = "this is a lap where you can put anything"
# print(kiran)
# print(anjali)
# print(shrijana)

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
# kiran = ("apple", "banana", "horny")
# a, b, c = kiran
# print(a)
# print(b)
# print(c) # this is called inpacking list



# Global variance : create the variable outside function and  use inside the function.

# a = "hot"

# def myfunc():
#     print("she is " + a )


# myfunc()




# a = "of my own banking"

# def myfunc():
#     print("i have a detail " + a )


# myfunc()  




# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)


# myfunc()

# print("python is 

# x = "good"

# def myfunc():
#   global x
#   x = "delicious"

# myfunc()
# print("python is " + x)


# a = 1000
# b = 300 
# if a < b:
#     print("a is greater than b")
# else:
#     print(" a is  greater than b")


# a = []
# b = ()
# c = {}
# d = 0
# e = None
# f = False
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))#  some values are false in boolen

# top = [ " banana", "1", "0.33"]
# y = 3


# while y < len(top):
#     print(top[y])

#     y +=1

# top = ["banana"," apple", "car"]
# x = 0

# while x < len(top):
#   print(x)
#   break
#   x += 1
  
  

# for i in range(3):
#     for j in range(2):
#         print(f"i={i}, j={j}") # f string le string ma variable ko value add garna sakxa


# a = ["banana" , "chop" , "shop"]# Nested loop using while loop
# b = ["1" , "2", "3"]

# x = 0
# y = 0

# while x <len(a):
#   while y <len(b):
#     print(a[x] , b[y])

#     x +=1
#     y += 1




  
# range = {"name": "kiran", "product":"apple", "items": "4"}
# range["product"] = "nike"# dict is changable in this way
# print(range)



     
# cap = {"name":"kiran","address":"kathmandu", "age":"19"}

# for key, value in cap.items():
#     print(f"{key} : {value}")


# Device_info = {"brand":"apple", "model":"iphone14","storage":"128gb"}


# for key, value in Device_info:
#     print(Device_info["brand"] ["apple"])


# def miss_k(a,b):
#     text = a+b
#     print(text)
#     return(text)

# result = miss_k(10,2)   
# print(result) 
    



# def hang_out(a,b):
#     fog = a+str(b)
#     print(fog)
#     return(fog)# defination of function vanxau


# result = hang_out("ram ",1)   # function call and argument ko value parameter ma gayera store hunxa
# print(result) 




# def greet_user(name, color):
#     print(f"hello{name}! your favorite color is {color}.")

#     # take input from user

# user_name = input("what is your name?")
# user_color = input("what is your favorite color")


# # calling the fuction
# greet_user(user_name,user_color)




# def calculator(a,b,operator):
#     if operator == '+':
#         print(a+b)
#     elif operator == '-':
#         print(a-b)

# user_a = int(input("Enter the first number"))
# user_b = int(input("enter the second number"))
# user_op= input("Enter the operator (*,+,-,%):")

# calculator(user_a,user_b,user_op )


              
          
# def dragon_file(computer):
#     for x in computer:
#         print(x)


# computer = ["Cpu", "ram","rom"]

    
# dragon_file(computer)







# def honey_file(song):
#     index = 0
#     for x in song:
#         print(f"this is a song {x}")
        
#         index += 1
#         print("total number of song:", index)

# song = ["aparibhasit","mari jau", "sadhai sadhai"]

# honey_file(song)
     





# using input string formatting.abs

# def introduce_person():
#     name = input("Tapaiko naam bhannus: ")
#     age = input("Tapaiko umar kati ho: ")
#     place = input("Tapaiko thau ko naam: ")

#     print(f"Namaste! Mero naam {name} ho, ma {age} barsa ko hu, ra ma {place} bata aayeko ho.")

# introduce_person()





# def area_of_rectangle(length, breadth):
#     result = length*breadth
#     return result


# result = area_of_rectangle(5, 3)
# print(result)





# def check_even_odd():
#      number = int(input("Enter the even number"))
#      number = int(input("Enter the odd number"))

#      if number %2 == 0:
#         return "Even"
#      else:
#         return "odd"
     
# result = check_even_odd()
# print(result)

#result = check_even_odd()
#print(result2)

     



# def check_age(name , age):
#    if age>18:
#       print(f" Welcome {name}, you are eligible.")
#    else:
#       print(f" {name}, you are not eligible. ")   

# user_1 = input("Enter your name")
# user_2 = int(input("Enter your age"))

# check_age(user_1 ,user_2)





marks = 50
def myfunction():
   marks = 70
   print(marks)


   myfunction
   print(marks)