#  def fizzBuzz(n):
#     # Write your code here
#     for i in n:
#      if i == 3 :
#         print(fizz)
#      elif i * 3 != 0 :
#         print(fizzBuzz)
#      elif i * 5 == 0:
#         print(fizzBuzz)
#      elif 3 * 5 != i:
#         print(fizzBuzz)

# if __name__ == '__main__':
#     n = int(input().strip())

#     fizzBuzz(15)

# def fizzBuzz(n):
#     for i in fizzBuzz(0,15):
#         print(i)
        
# fizzBuzz(15)

# for x in range(0,16):
#     if x == 3 :
#         print("fizz")
#     elif x * 3 != 0 :
#         print("fizzBuzz")
#     elif x * 5 == 0:
#         print("fizzBuzz")
#     elif 3 * 5 == 15 :
#         print("fizzBuzz")
#     print(x)


# def myfunc(n):
#     return lambda a : a * n

# mydoubler = myfunc (2)
# print(mydoubler(5))


# def myfunc(n):
#     return lambda a : a * n

# mdouble = myfunc(3)
# print(mdouble(5))

# def func(n):
#     return lambda a: a * n

# double = func(2)
# triple = func(3)
# multiple = func(4)

# print(double(5))
# print(triple(5))
# print(multiple(5))

# food = ["Mango", "Jackfruit", "Banana","Pinaple", "Apple"]
# print(food.index("Apple"))
# food[0] = "Strawbarry"
# food.append("Mango")
# print(len(food))
# print(food)
# food.pop(3)

# for x in food:
#     print(x)

# class myClass:
#     x = 6
# p1 = myClass()
# print(p1.x)

# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = student ("Raju",21)
# print(p1.name)
# print(p1.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# print(p1.myfunc())     

# class Man:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def func(self):
#         print("Hello " + self.name)
#         print("you are only " , self.age , "Year's old")

# m1 = Man ("Raju", 21)
# m1.func()


# class student:
#     def __init__(self,name,roll,Class,age):
#         self.name = name
#         self.roll = roll
#         self.Class = Class
#         self.age = age
#     def func(sel):
#         print("Your Name is " + sel.name)
#         print("your roll numeber is " , sel.roll , )
#         print("You are in Class " + sel.Class)
#         print("Youre" , sel.age , "year's old")

# s1 = student("Raju",1,"Diploma",21)
# s1.func()


# class stu:
#     def __init__(self,name,roll):
#      self.name = name
#      self.roll = roll

#     def inf(st):
#          print("You're " + st.name)
#          print("old is ", st.roll)

# s1 = stu("Raju", 1)   
# s1.roll = 21
# s1.inf()

# class raj:
#     def __init__(self,name,roll):
#         self.name = name
#         self.roll = roll

#     def king(rj):
#         print("My name is " + rj.name)
#         print("My roll number is ", rj.roll,)

# first = raj("Raju", 484201)
# first.king()

# saarc = ["Bangladesh","Afganistan","bhutan","Nepal","India","Pakistan","Srilanka"]

# country = input("Enter the Name of the country: ")
# if country in saarc:
#     print("The " + country + " an member of saarc")
# else:
#     print("No it's not!")

# from_user = int(input("Enter an integer: "))
# if from_user % 2 == 0:
#     print("it's an odd")
# else:
#     print("It's even!")




# python program to check if year is a leap year or not

# user_input = int(input("Enter the year: "))
# if user_input % 4 == 0:
#     if user_input % 100 == 0:
#         if user_input % 400 == 0:
#             print(user_input, " is a leap year")
#         else:
#             print("it's not a leap year!")
#     else:
#         print("it's a leap year!")
# else:
#     print("it's not a leap year!")



# love = ("I Love Bangladesh")
# for i in range (10):
#     print(love)

# result = 0
# for i in range(50):
#     result = result + 2
# print(result)

# result = 0
# for i in range(50):
#     result = result + i
    

# print(result)

# num = 0
# for i in range(50):
#     num = num + i

# print(num)


# sam = 0
# for num in range(101):
#     if num % 5 ==0:
#         print(num)
#         sam += num
# print("sum is ",sam)

# for i in range(8):
#     print("I Try my best")


# result = 0
# for i in range(50):
#     result = result + 2
# print(result)

# result = 0
# for i in range(51):
#     result = result + i
# print(result)

# num = 0
# for i in range(101):
#     num = num + i
# print(num)

# sum = 0
# for num in range(51):
#     sum = sum + num
# print(sum)

# for i in range(0,51,5):
#     print(i)

# for i in range(1,51,2):
#     print(i)

# result = 0
# for num in range(101):
#     if num % 5 == 0:
#         print(num)
#         result = result + num

# print(result)

# result = 0
# for i in range(5,101,5):
#     if i % 5 == 0:
#         print(i)
#         result += i
# print("The sums is" , result)

# fnd_list = ["rahim", "raju", "robin", "roki", "rahi"]
# for fnd in fnd_list:
#     print(fnd, "is my fnd")

# odd_list = list(range(2,21,2))
# print(odd_list)

# for i in range(2,21,2):
#     print(i)

# n = int(input("Enter an integer: "))
# m = 1
# while m <= 10:
#     print(n,"x", m,"=", n*m)
#     m = m + 1


# odd = int(input("Enter a number:"))
# m = 1
# while m <= 10:
#     print(odd, "x", m,"=",odd*m)
#     m += 1


# n = int(input("Enter the number: "))
# m = 1
# while m <= 10:
#     print(n, "x", m,"=",n*m)
#     m += 1

# result = 0
# for i in range(20):
#     result += i
#     print(result)

# for i in range(0,21):
#     print(i)
#     if i % 3 == 0:
#         continue
#         print("fezz")
#     elif 3 * 5 == 0:
#         continue
#         print("feex")

# while True:
#     n = input("Please enter a positive number (0 to exit): ")
#     n = int(n)
#     if n < 0:
#         print("We only allow positive number. Please try again.")
#         continue
#     if n == 0:
#         break
#     print("Square of", n, "is", n*n)
    
# while True:
#     n = int(input("enter a numbr (0 to exit): "))
#     if n < 0:
#         print("we only allow positive number.try again")
#         continue
#     if n == 0:
#         break
#     print("square of" ,n , "is", n*n)

# terminate_program = False
# while not terminate_program:
#     number1 = int(input("Please enter a number: "))
#     number2 = int(input("Please enter another number: "))
    
#     while True:
#         operation = input("Please enter add/sub or quit to exit: ")
#         if operation == "quit":
#             terminate_program = True
#             break
#         if operation not in ["add", "sub"]:
#             print("Unknown operation!")
#             continue
#         if operation == "add":
#             print("Result is", number1 + number2)
#             break
#         if operation == "sub":
#             print("Result is", number1 - number2)
#             break
# def hello():
#     print("hello world")

# hello()

# def make_sum(*args):
#     sum = 0
#     for num in args:
#         sum = sum + num
#     return sum
# print(make_sum(10,20,20,50))


# def sum(*args):
#     num = 0
#     for i in args:
#         num = num + i
#     return num
# print(sum(10,20,30,40))

# def dict(**kwargs):
#     print(kwargs)

# dict(a=1, b=2, c=40)


# def dict(**dicti):
#     print(dicti)
# dict(a=1, n=4, v=9, c=2)

# def print_all(a, *args, **kwargs):
#     print(a)
#     print(args)
#     print(kwargs)


# print_all(10, 20, 30, 50, b=5, c=10)



# def dic(**args):
#     for arg in args:
#         print("{0} : {1}".format(arg, args[arg]))
# dict(a=1, b=2, c=3, d=4)


# dict = {"set": "python setting", "name":"raju", "king":"dream", "dream":"raju"}
# inp = input("Enter what you want: ")
# if inp in dict:
#     print(dict.get(inp))

# n = 9
# inp = int(input("Guess the number: "))


# while inp == n:
#     print("Congrgulation! You won")
#         break
# if inp > n:
#     print("Pleas Enter Lower number")
# elif inp < n:
#     print("Please enter higher number")
# else:
#     print("Try again!")

# def func(n, m):
#     return n + m

# sum = func(5, 10)
# print(sum)

# def myfunc(x):
#     print("inside myfnc", x)
#     x = 10
#     print("inside myfnc", x)

# myfunc(20)

# try: 
#     def func(y):
#         print("y = ", y)
#         print("x = ", x)
#     func(20)
# except NameError:
#     print("please define the x variable")

# def mfunc(y = 10):
#     print("y = ", y)

# x = 12
# mfunc(x)
# mfunc()


# def mfnc(x, y = 10, z = 13):
#     print("x =", x, "y = ", y, "z = ", z)
# x = 10
# y = 20
# z = 12
# mfnc(x,y,z)

# def mfc(x, z, y = 10):
#     print("x = ", x, "y = ", y, "z = ", z)

# mfc(x = 1, y = 2, z = 5)
# a = 5
# b = 6
# mfc(x = a, z = b)
# a = 3
# b = 1
# c = 2
# mfc(x = a, y = b, z = c)

# def num_sum(numbers):
#     result = 0
#     for num in numbers:
#         result +=  num
#     print(result)

# num_sum([10,20,30,40])


# def test_ind(my_list):
#     my_list[0] = 44

# li = [1,2,4,5]
# print("Before function call", li)
# test_ind(li)
# print("After function call", li)
