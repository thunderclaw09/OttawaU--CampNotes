# **Day 4 - 3 August 2023**

## **Activity 1: Integers to Roman Numerals**

A **GREEDY ALGORITHM** is an algorithm that finds a solution to problems in the shortest time possible. 

MY CODE FOR CONVERTING FROM INTEGER TO ROMAN NUMERAL (GOES UP TO 3999):
```python
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
```
----

TEACHER'S SOLUTION (IN JAVA):
```java
import java.util.LinkedHashMap;

class Solution
{
    private final LinkedHashMap<Integer, String> romanNumerals;
    public Solution()
    {
        romanNumerals = new LinkedHashMap<>();
        romanNumerals.put(1000, "M");
        romanNumerals.put(1000, "CM");
        romanNumerals.put(1000, "D");
        romanNumerals.put(1000, "CD");
        romanNumerals.put(1000, "C");
        romanNumerals.put(1000, "XC");
        romanNumerals.put(1000, "L");
        romanNumerals.put(1000, "XL");
        romanNumerals.put(1000, "X");
        romanNumerals.put(1000, "IX");
        romanNumerals.put(1000, "V");
        romanNumerals.put(1000, "I");

    }

    public String intToRoman(int integer)
    {
        StringBuilder romanString = new StringBuilder();
        for (int i: romanNumerals.keySet())
        {
            while (i <= integer)
            {
                integer -= i;
                romanString.append(romanNumerals.get(i));
            }
        }
        return romanString.toString();
    }
}
```

**He used a HASH MAP in order to keep it organized. (Why didn't I think of that??? XD)**
<br></br>
<br></br>
<br></br>

## **Activity 2: Very Basic Server**

**SERVERS** hold data for us and allow us to access the files and programs from the client side. 

There are two parts: **SERVER SIDE** and **CLIENT SIDE**.
- Client side is for us, what we see. 
- Server side is the *backend*. It does all the "behind the scenes" stuff. 

**FUNCTION CHAINING** is when you attach multiple functions to each other. (Like doing .then().then or something like that.)

An **EVENT LISTENER** is kinda like a button click event. You add the ID and the program will be constantly looking for it in the background. 
<br></br>
<br></br>
<br></br>

## **Activity 3: APIs and API Keys**

An **API** is some kind of program we use to fetch data or something like that. ChatGPT has it's own API, for example, which allows us to connect ChatGPT to another app and access all that information. You would need your own **API KEY** that is specific to you. 

*OBJECTIVE: Coding something that will grab weather information and display it in the console.*

**JSON** stands for "Java Script Object Notation." 

    When Python uses the json object, it treats it like a DICTIONARY. 
<br></br>
<br></br>
<br></br>

## **Activity 4: Turtle Maze**

The way he solved it: he "put one hand on the left wall and followed it". Basically, it semms that he just folowed a specific wall. He faces the left of the turtle and follows it. 

If there's a wall to the left, it continues forward. If there is a wall on the left and in front, it changes direction to the right and continues as normal. 
<br></br>
<br></br>
<br></br>

## **Activity 5: Challenge - Merging Two Sorted Lists**

A **LINKED LIST** is a list that has two pieces of information: the data and something that points to the next node. Each node is the same. The last node points to null. 

**TEACHER'S SOLUTION**
```c++
class Solution
{
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2)
    {
        if (list1 == nullptr) return list2;
        if (list2 == nullptr) return list1;

        if (list1->val >= list2 ->val)
        {
            list2->next = mergeTwoLists(list1, list2->next);
            return list2;
        }else
        {
            list1->next = mergeTwoLists(list1->next, list2);
            return list1;
        }
    }
};

// this is a RECURSIVE function

```