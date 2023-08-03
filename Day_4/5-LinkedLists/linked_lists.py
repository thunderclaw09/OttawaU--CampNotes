# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    newlist = []

    while list1.next != None:
        while list2.next != None:
            if (list1.val > list2.val) or (list1.val == list2.val):
                newlist.append(list1.val)
                list1.val = list1.next
                print(newlist)
            else:
                newlist.append(list2.val)
                list2.val = list2.next
                print(newlist)

    return newlist

# This, like most of my projects now, does NOT work. :(
