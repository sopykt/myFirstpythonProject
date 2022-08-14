from math import *
my_name = "Soe Paing"
# print(len(my_name))
# print(my_name[0]+my_name[1])
# print(my_name.index("o"))
# print(my_name.index("in"))
# print(my_name.upper())
# print(my_name.isupper())
# print(my_name.upper().isupper())
# my_name = my_name.upper()
# print(my_name)
num = 456
# print(type(num))
# print(my_name.replace("PAING", "Paing"))
# print(-3.903)
# print(3 * 4 + 5)
# print(3 * (4 + 5))
# print(3 * 4 / 2)
# print((3 * 4) / 2)
# print(3 % 3)
# print(3.0 % 3)
# print(str(num) + " is now string and can concatenate with string.\nOtherwise it shows error.")
float_num = -3.5
# print(abs(float_num))
# print(pow(3, 2))
# print(max(3, 2))
# print(min(3, 2))
# print(round(float_num))

# below need from math import *

# print(floor(3.5), ceil(3.5), floor(float_num), ceil(float_num))
# print(sqrt(4), sqrt(9), sqrt(16))
# print(bin(num))
# print(bytes(9 + 1))
# print(bytearray(2+2))
# print(chr(11119))

# hash changing to an unpredictable random value.
# Although they remain constant within an individual Python process,
# they are not predictable between repeated invocations of Python.

# print(hash(my_name))
# new_name = "SOE PAING"
# if hash(my_name) == hash(new_name):
#     print('true')
# else:
#     print('false')
# print(hex(28))
# print(id(num))
# user_name = input("Enter your name: ")
# print("Hi, " + user_name + "!")
# place = input("Where do you live, " + user_name + "?")
# print(place + " is a good place.")

# input always gets string, so if you want int you must convert it
# int() cannot accept float. so you use float() to accept decimal as well.

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num2) + float(num1)
# print(result)

# funny mad lib game

# shape = input("သင်ကြိုက်တဲ့ ပုံစံတစ်ခု (စက်ဝိုင်းပုံ၊ လေးထောင့်ပုံ၊ တြိဂံပုံ) - ")
# length = input("သင်ကြိုက်နှစ်သက်ရာ အရှည်ပမာဏ - ")
# name = input("သင်သိတဲ့ လူနာမည် တစ်ခု - ")
# print("နာမည်က " + name)
# print("မျက်နှာက " + shape)
# print("အရပ်က " + length)

# Lists
#               0           1        2         3
#                                    -4       -3       -2      -1
friends = ["အောင်အောင်", "ကျော်ကျော်", "စိုးစိုး", "မောင်မောင်", "သီဟ", "ဇေယျ"]
print(friends)
print(friends[2])
print(friends[-3])
print(friends[2:])
print(friends[2:4])
friends[2] = "မော်မော်"
print(friends[2:])
lucky_numbers = [2, 5, 9, 22, 23]
friends.extend(lucky_numbers)
print(friends)
friends.append("မျိုးမျိုး")
print(friends)
friends.insert(2, "Ryan")
print(friends)
friends.remove("ကျော်ကျော်")
print(friends)
friends.pop()
print(friends)

print(friends.pop(2))
print(friends)
print(friends.index(22))
friends.insert(0, "သီဟ")
print(friends)
print(friends.count("သီဟ"))
