class node:
    def __init__(self, value, nextNode = None):
        self.val = value
        self.next = nextNode

def createList(lst):
    anode = node(lst[0],None)
    head = anode
    for i in range(1,len(lst)):
        anode.next = node(lst[i],None)
        anode= anode.next
    return head

def printLinkedList(head):
    while head != None:
        print(head.val, end="->")
        head= head.next
    print(" ")


def rotate(nums: list[int], k: int) -> None:
    nums[:k:] ,nums[k::] =nums[-k::] , nums[:-k:]

def isUnique(sent:str) -> bool:
    dic = {}
    for ch in sent:
        if ch in dic:
            return False
        dic[ch]=True
    return True


def deleteMiddle(anode:node)->None: # O(n) Time complex. O(1) Space complex
    if anode == None or anode.next == None:
        return
    anode.val=anode.next.val
    anode.next= anode.next.next

def CheckPermutation(a:str, b:str)->bool: # O(n). just for ASCII. not unicode
    if len(a) != len(b):
        return False
    a.lower()
    b.lower()
    buck= [0]*256
    for i in range(len(a)):
        buck[ord(a[i])]+=1
        buck[ord(b[i])]-=1
    for num in buck:
        if num != 0:
            return False
    return True

def partition(head:node, pivot:int)->None:  # O(n) time complex, O(1) space complex
    slow=head
    while slow!=None:
        if slow.val < pivot:
            slow=slow.next
            continue
        fast=slow.next
        while fast != None and fast.val >= pivot :    # fast runner tries to find a small value
            fast = fast.next
        if fast == None:   # No smaller numbers left
            break
        slow.val,fast.val=fast.val,slow.val # Switch the values if a smaller one is found
        slow = slow.next


    


linked= createList([1,9,3,2,5,6,4,8])
printLinkedList(linked)
partition(linked, 7)
printLinkedList(linked)
