# ~ Area4 Package by RDIL ~ 

# Package info variables:
name = "area4"
author = "https://github.com/RDIL"
author_email = "contactspaceboom@gmail.com"
description = "Dividers in Python, the easy way! Multiple different divider looks."

# Divider variables:
divider1 = str("------------------------")
divider2 = str("________________________")
divider3 = str("........................")
divider4 = str("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
divider5 = str("⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️")
divider6 = str("⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️")
divider7 = str("========================")
divider8 = str("########################")
divider9 = str("************************")
divider10 = str(",,,,,,,,,,,,,,,,,,,,,,,,")
divider11 = str("////////////////////////")
divider12 = str("||||||||||||||||||||||||")
divider13 = str("~~~~~~~~~~~~~~~~~~~~~~~~")
divider14 = str("\\\\\\\\\\\\\\\\\\\\\\\\")
divider15 = str("☕ ☕ ☕ ☕ ☕ ☕ ☕ ☕ ☕ ☕ ☕ ☕")
divider16 = str("++++++++++++++++++++++++")
divider17 = str("r(`,,,`)r r(`,,,`)r r(`,,,`)r ")
custom_div = str("")

# Functions:
def div1():
    return divider1

def div2():
    return divider2

def div3():
    return divider3

def div4():
    return divider4

def div5():
    return divider5

def div6():
    return divider6

def div7():
    return divider7

def div8():
    return divider8

def div9():
    return divider9

def div10():
    return divider10

def div11():
    return divider11

def div12():
    return divider12
	
def div13():
    return divider13

def div14():
    return divider14

def div15():
    return divider15

def div16():
    return divider16

def div17():
    return divider17
  
def customdiv():
    return custom_div

def make_div(div, length=24):
    repeats = length//len(div)
    return (div*repeats)[0:length]

def area4info():
    info = f"Name: {name}"
    info += f"\nAuthor: {author}"
    info += f"\nAuthor Email: {author_email}"
    info += f"\nDescription: {description}"
    return info
