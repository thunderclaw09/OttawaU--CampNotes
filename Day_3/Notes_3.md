# **Day 3 - 2 August 2023**

## **ACTIVITY 1: Data Structures**

- A **STACK** works "last in, first out."
- A **QUEUE** works "first in, first out."
- **NOTES** work with pointers pointing two and fro. 

*Given an array of intregers **nums** and an integer **target**, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.*

Example:

    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]

*(I DID THIS USING TWO LANGUAGES)*
<br></br>

**EXAMPLE 1: PYTHON**
```python
def myFunc(nums, target):
    # Splitting the numbers
    numsList = nums.split()
            
    # Converting the target into an integer
    target = int(target)

    # Loop that checks if it's the same
    for i in range(0, len(numsList), 1):
        for j in range(i, len(numsList), 1): 
            if (i != j):
                if ((int(numsList[i]) + int(numsList[j])) == target):
                    return (i, j) # Ends function
                
    # If there was nothing found:
    return "faulty input / faulty code"

nums = input("Please enter the list: ")
target = input("Please enter the target: ")

output = myFunc(nums, target)

print("FINAL OUTPUT:", output)
```
<br></br>

**EXAMPLE 2: JAVA**
```java
public class Data_Structures {
    public static void myFunc(int[] nums, int target)
    {
        for (int i = 0; i < nums.length; i++)
        {
            for (int j = i; j < nums.length; j++)
            {
                if (i != j)
                {
                    if (nums[i] + nums[j] == target)
                    {
                        System.out.println("(" + Integer.toString(i) + ", " + Integer.toString(j) + ")");
                    }
                }
            }
        }
    }


    public static void main(String[] args) 
    {
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        myFunc(nums, target);
    }
}
```
<br></br>

**EXAMPLE 3: TEACHER'S SOLUTION**
```java
class Solution
{
    public int[] twoSum(int[] nums, int target)
    {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++)
        {
            if (map.containsKey(nums[i]))
            {
                return new int[]{map.get(nums[i]), i}
            }else
            {
                map.put(target - nums[i], i)
            }
        }
    }
}
```
- A **HASHMAP** is like a dictionary in python in which each element is a pair of values.
- **TIME COMPLEXITY** is how many operations it takes to complete the program. 
    - **Big O notation** is represented like this: **O(n)**. Its equation seems to have a power of one and does not appear to be a quadratic equation. 
    - There is also **Omega notation** and **Feta notation**
    - **Big O of N** can be represented by equations such as ***[t = n]*** and ***[t = log(n)]***, but NOT by ***[t = n^2]***. 
    - **Big Omega of N** can be represented by equations such as ***[t = n^2]*** and ***[t = n]***, but NOT by ***[t = log(n)]***
    - When inserting something into a chain, don't just plop something in and point the first part to it, because you'd lose track of the latter part. You have to also point the new object to the latter part. 

<br></br>
<br></br>
<br></br>

## **ACTIVITY 2: WEB DEV**

HTML has different headers and tags. Google it for a full list.

There are two ways to identify elements:
- **ID**: This is useful for impacting small objects.
- **Class**: This is more useful for impacting multiple, general items, like the apples on a tree. 

**WARNING:** Do NOT use "clear()" as a function name in JavaScript. It's a built-in function, which means that you may not be able to override it properly. This could also apply to a variety of other built-in functions, so be careful what you name your functions. 

**The === sign means that it has to be this EXACTLY. It's more strict than the double equal sign. (==)**

```javascript
// This built-in JavaScript function takes a string and solves the equation.
return eval(equationInString);
```