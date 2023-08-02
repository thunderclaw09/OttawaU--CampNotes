# **Day 3 - 2 August 2023**

## **ACTIVITY 1: Data Structures**

- A **STACK** works "last in, first out."
- A **QUEUE** works "first in, first out."
- **NOTES** work with pointers pointing two and fro. 

*Given an array of intregers **nums** and an integer **target**, return indices of the two numbers suc that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twie. You can return the answer in any order.*

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
<br></br>
<br></br>

## **ACTIVITY 2: (PLACEMENT TEXT)**