import random
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
# friends = ["အောင်အောင်", "ကျော်ကျော်", "စိုးစိုး", "မောင်မောင်", "သီဟ", "ဇေယျ"]
# print(friends)
# print(friends[2])
# print(friends[-3])
# print(friends[2:])
# print(friends[2:4])
# friends[2] = "မော်မော်"
# print(friends[2:])
# lucky_numbers = [2, 5, 9, 22, 23]
# friends.extend(lucky_numbers)
# print(friends)
# friends.append("မျိုးမျိုး")
# print(friends)
# friends.insert(2, "Ryan")
# print(friends)
# friends.remove("ကျော်ကျော်")
# print(friends)
# friends.pop()
# print(friends)
#
# print(friends.pop(2))
# print(friends)
# print(friends.index(22))
# friends.insert(0, "သီဟ")
# print(friends)
# print(friends.count("သီဟ"))
# # sort() can only work on same type, not str and int altogether
# print(friends.pop(-1))
# print(friends.pop(-1))
# print(friends.pop(-1))
# print(friends.pop(-1))
# print(friends.pop(-1))
# friends.sort()
# print(friends)
# lucky_numbers = [22, 5, 23, 9, 2]
# # lucky_numbers.sort()
# # lucky_numbers.reverse()
# copy_lucky_numbers = lucky_numbers.copy()
# print(copy_lucky_numbers)
# lucky_numbers.clear()
# print(lucky_numbers)

# Tuples
# coordinates = (2, 5)
# print(coordinates)
# print(coordinates[1])


# coordinates[1] = 4 // result in error as tuples are immutable

# functions
# def say_hi(name, age):
#     if name == "soe" and float(age) > 30:
#         print("Hey Ko Soe Paing! I know you. I thought you are under 30. Its really " + str(age) + "?")
#     else:
#         print("Hello " + name + ", you are " + str(age))
#
#
# name = input("What's your name? ")
# age = input("How old are you? ")
# say_hi(name, age)
# say_hi("soe", 38)
# say_hi("Myint", '95')


# def cube(number):
#     return number*number*number
#     # below doesn't work because return block
#     print("hi")
#
#
# result = cube(5)
# print(result)

# Dictionaries
# Key: Value pairs
# Keys are unique
# month_conversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "Jun",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
#     0: "Zero",
#     128: "One Hundred and Twenty Eight",
#     "Twenty": 20,
#     "Forty": 40
# }
#
# print(month_conversions["Aug"])
# print(month_conversions.get(0))
# print(month_conversions.get("No_Key"))  # result in None
# print(month_conversions.get("Not_Key", "This is not a valid Key"))
# Twenty = month_conversions.get("Twenty", "This is not a valid key")
# print(Twenty)
# Forty = month_conversions.get("Forty", "This is not a valid key")
# print(Forty)
# Sum = Twenty + Forty
# print(Sum)

# While Loops
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Finished!")

# import random
# next_possibles = ["ကရတ", "မဆရ", "၂/၃၀၀", "၂/၁၀၀၀"]
# secret_word = random.choice(next_possibles)
# guess = ""
# i = 0
# times = 5
# translate_myanmar = {
#     1: "တစ်",
#     2: "နှစ်",
#     3: "သုံး",
#     4: "လေး",
#     5: "ငါး"
# }
#
# while guess != secret_word and i < times:
#     left = times - i
#     guess = input("ကစားခွင့် " + translate_myanmar.get(left) + " ကြိမ်ကျန်ရှိပါသည်။ စကားဝှက်မှာ: ")
#     i += 1
# if guess == secret_word and i <= times:
#     print("သင်နိုင်ပါသည်။")
# else:
#     print("သင်ရှုံးပါသည်။")
# print("သင်ရောက်ရှိမည့် တပ်မှာ " + secret_word + " ဖြစ်ပါသည်။")

# def max_num(num1, num2, num3):
#     nums = [num1, num2, num3]
#     nums.sort()
#     return nums[2]
#
#
# result = max_num(55, 43, 222)
# print(result)

# def search(list, inputs):
#     for i in range(len(list)):
#         if list[i] == inputs:
#             return True
#     return False


# if search(done, inputs):
#     print("Platform is found")
# else:
#     print("Platform does not found")

# while not search(done, inputs):
#     inputs = input("Enter: ")
# else:
#     print("Found")

# nums = []
# done = ['d', 'done']
# inputs = ''
# print("Find maximum number")
# while inputs.lower() not in done:
#     inputs = input("Enter numbers one by one. When you done, enter (D/d/Done): ")
#     if inputs.isdigit():
#         inputs = int(inputs)
#         nums.append(inputs)
#         print("You entered: " + str(nums))
#         sorted_nums = sorted(nums)
#         print("From smallest to biggest: " + str(sorted_nums))
#         print("Biggest number you entered: " + str(sorted_nums[-1]))
#         inputs = str(inputs)
# else:
#     print("Done")

cards = list(range(52))
print(cards)
shuffle_cards = cards.copy()
random.shuffle(shuffle_cards)
print(shuffle_cards)
cards_dict = {
    1: "BLACK|SPADE|2",
    2: "BLACK|SPADE|3",
    3: "BLACK|SPADE|4",
    4: "BLACK|SPADE|5",
    5: "BLACK|SPADE|6",
    6: "BLACK|SPADE|7",
    7: "BLACK|SPADE|8",
    8: "BLACK|SPADE|9",
    9: "BLACK|SPADE|10",
    10: "BLACK|SPADE|J",
    11: "BLACK|SPADE|Q",
    12: "BLACK|SPADE|K",
    13: "BLACK|SPADE|A",
    14: "BLACK|CLUB|2",
    15: "BLACK|CLUB|3",
    16: "BLACK|CLUB|4",
    17: "BLACK|CLUB|5",
    18: "BLACK|CLUB|6",
    19: "BLACK|CLUB|7",
    20: "BLACK|CLUB|8",
    21: "BLACK|CLUB|9",
    22: "BLACK|CLUB|10",
    23: "BLACK|CLUB|J",
    24: "BLACK|CLUB|Q",
    25: "BLACK|CLUB|K",
    26: "BLACK|CLUB|A",
    27: "RED|DIAMOND|2",
    28: "RED|DIAMOND|3",
    29: "RED|DIAMOND|4",
    30: "RED|DIAMOND|5",
    31: "RED|DIAMOND|6",
    32: "RED|DIAMOND|7",
    33: "RED|DIAMOND|8",
    34: "RED|DIAMOND|9",
    35: "RED|DIAMOND|10",
    36: "RED|DIAMOND|J",
    37: "RED|DIAMOND|Q",
    38: "RED|DIAMOND|K",
    39: "RED|DIAMOND|A",
    40: "RED|HEART|2",
    41: "RED|HEART|3",
    42: "RED|HEART|4",
    43: "RED|HEART|5",
    44: "RED|HEART|6",
    45: "RED|HEART|7",
    46: "RED|HEART|8",
    47: "RED|HEART|9",
    48: "RED|HEART|10",
    49: "RED|HEART|J",
    50: "RED|HEART|Q",
    51: "RED|HEART|K",
    52: "RED|HEART|A"
}
# first = shuffle_cards[0]
print("Player 1: " + cards_dict[shuffle_cards[0]] + " and " + cards_dict[shuffle_cards[2]])
print("Player 2: " + cards_dict[shuffle_cards[1]] + " and " + cards_dict[shuffle_cards[3]])

if input("Player 1 need a card? (\"y\" for yes others for no): ") == "y":
    print("Player 1: " + cards_dict[shuffle_cards[0]] + " and " + cards_dict[shuffle_cards[2]] + " and " + cards_dict[
        shuffle_cards[4]])
    print("Player 2: " + cards_dict[shuffle_cards[1]] + " and " + cards_dict[shuffle_cards[3]])
    if input("Player 2 need a card? (\"y\" for yes others for no): ") == "y":
        print(
            "Player 1: " + cards_dict[shuffle_cards[0]] + " and " + cards_dict[shuffle_cards[2]] + " and " + cards_dict[
                shuffle_cards[4]])
        print(
            "Player 2: " + cards_dict[shuffle_cards[1]] + " and " + cards_dict[shuffle_cards[3]] + " and " + cards_dict[
                shuffle_cards[5]])
    else:
        print(
            "Player 1: " + cards_dict[shuffle_cards[0]] + " and " + cards_dict[shuffle_cards[2]] + " and " + cards_dict[
                shuffle_cards[4]])
        print("Player 2: " + cards_dict[shuffle_cards[1]] + " and " + cards_dict[shuffle_cards[3]])
else:
    if input("Player 2 need a card? (\"y\" for yes others for no): ") == "y":
        print("Player 1: " + cards_dict[shuffle_cards[0]] + " and " + cards_dict[shuffle_cards[2]])
        print(
            "Player 2: " + cards_dict[shuffle_cards[1]] + " and " + cards_dict[shuffle_cards[3]] + " and " + cards_dict[
                shuffle_cards[4]])
    else:
        print("Player 1: " + cards_dict[shuffle_cards[0]] + " and " + cards_dict[shuffle_cards[2]])
        print("Player 2: " + cards_dict[shuffle_cards[1]] + " and " + cards_dict[shuffle_cards[3]])
