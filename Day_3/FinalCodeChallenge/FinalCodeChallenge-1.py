# EASY CODE CHALLENGE
def isPalindrome(inputInt):
    original = str(inputInt)
    new = original[::-1]

    if (original == new):
        return True
    else:
        return False


print(isPalindrome(121))
