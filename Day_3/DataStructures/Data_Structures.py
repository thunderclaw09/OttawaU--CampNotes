# ELISA LAM | 2 AUGUST 2023

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