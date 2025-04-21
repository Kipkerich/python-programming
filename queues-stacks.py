class Solution:
    
    def __init__(self):
        #Creates instance stack and queue
        self.stack = []
        self.queue = []
        
        
    def pushCharacter(self, ch):
        #Pushes character to the stack
        self.stack.append(ch)
        
    def enqueueCharacter(self,ch):
        #Enqueue character in the queue
        self.queue.insert(0,ch)
            
    def popCharacter(self):
        #Pop and return the character at the top of the stack instance
        return self.stack.pop()
            
    def dequeueCharacter(self):
        #Dequeue and return the first character in the queue
        return self.queue.pop()
            
            
            
        

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    