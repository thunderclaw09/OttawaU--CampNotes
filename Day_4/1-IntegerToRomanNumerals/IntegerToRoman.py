# INTEGER TO ROMAN | 3 August 2023
# number is anything from 1 to 3999


# def RomanToDecimal(numeral):              IGNORE THIS, THIS IS THE WRONG THING
#     integer = 0
#     passNext = False
#     for i in range(0, len(numeral) - 1, 1):
#         if (passNext == True):
#             passNext = False
#             pass
#         if (numeral[i] == "M"):
#             integer += 1000
#         elif (numeral[i] == "D"):
#             integer += 500
#         elif (numeral[i] == "C"):
#             if (numeral[i + 1] == "M"):
#                 integer += 900
#                 passNext = True
#             elif (numeral[i + 1] == "D"):
#                 integer += 400
#                 passNext = True
#             else:
#                 integer += 100
#         elif (numeral[i] == "L"):
#             integer += 50
#         elif (numeral[i] == "X"):
#             if (numeral[i + 1] == "C"):
#                 integer += 90
#                 passNext = True
#             elif (numeral[i + 1] == "L"):
#                 integer += 40
#                 passNext = True
#             else:
#                 integer += 10
#         elif (numeral[i] == "V"):
#             integer += 5
#         elif (numeral[i] == "I"):
#             if (numeral[i + 1] == "X"):
#                 integer += 9
#                 passNext = True
#             elif (numeral[i + 1] == "V"):
#                 integer += 4
#                 passNext = True
#             else:
#                 integer += 1
#         else:
#             print("Invalid character detected: " + numeral[i])
    
#     return integer

numeral = input("Please input your roman numeral to be converted: ").upper()

def DecimalToRoman(dec):
    numeral = ""
    decimal = int(dec)
    if (decimal > 3999):
        return "Number too great"
    else:
        while decimal != 0:
            print("Decimal:", decimal)
            if (decimal >= 1000):
                numeral += "M"
                decimal -= 1000
            elif (decimal >= 900):
                numeral += "CM"
                decimal -= 900
            elif (decimal >= 500):
                numeral += "D"
                decimal -= 500
            elif (decimal >= 400):
                numeral += "CD"
                decimal -= 400
            elif (decimal >= 100):
                numeral += "C"
                decimal -= 100
            elif (decimal >= 90):
                numeral += "XC"
                decimal -= 90
            elif (decimal >= 50):
                numeral += "L"
                decimal -= 50
            elif (decimal >= 40):
                numeral += "XL"
                decimal -= 40
            elif (decimal >= 10):
                numeral += "X"
                decimal -= 10
            elif (decimal >= 9):
                numeral += "IX"
                decimal -= 9
            elif (decimal >= 5):
                numeral += "V"
                decimal -= 5
            elif (decimal >= 4):
                numeral += "IV"
                decimal -= 4
            elif (decimal >= 1):
                numeral += "I"
                decimal -= 1
            else:
                print("Reached zero")


                

        return numeral




print(DecimalToRoman(numeral))
# print(RomanToDecimal(numeral))