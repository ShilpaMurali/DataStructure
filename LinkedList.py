from test.support import temp_cwd
class Node:
    'Create a node class and a constructor init. Assign Data and the next field to none'
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    'Create a LnkedList class that contains the head of the LinkedList'
    def __init__(self):
        self.head=None
    'Traversing through the LinkedList'
    def printList(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
            
    def addANodeAtTheFront(self,data):
        if(self.head==None):
            'If the head is Null then we make the head point to the new node to be added'
            self.head=Node(data)
        else:
            'Creating a new element'
            newElement=Node(data) 
            'Assign the element pointed by head as the next of the new element'
            newElement.next=self.head
            'Make the Head point to the new element'
            self.head=newElement   
    
    def addANodeAfterAGivenNode(self,data,pos):
        if(self.head==None):
            print('The Node will be added at the head since no other element exists')
            self.head=Node(data)
            return
        else:
            p=0
            'Create a new element'
            newElement=Node(data)
            'Store the head in temp'
            temp=self.head
            'Iterate till the previous position of data insertion'
            while(p<pos):
                temp=temp.next
                p+=1
            'Once the prev element is found store its next as the next of the New Element'
            newElement.next=temp.next  
            'Once the prev element is found set its next as the New Element'
            temp.next=newElement          
                     
    def addANodeAtTheEnd(self,data):
        if(self.head==None):
            print('The Node will be added at the head since no other element exists')   
            self.head=Node(data)
            return
        else:
            'Store the head in temp'
            temp=self.head
            'We traverse through the list until the next node is Null. We stop at the prev node temp'
            while(temp.next):
                    temp=temp.next
            'NewNode is made as the Next of the current last node'
            temp.next=Node(data)   
    
    def deleteANodeInTheList(self,data):
        if(self.head==None):
            print('The list is empty. Deletion cannot be performed') 
            return
        else:
            temp=self.head
            flag=False
            while(temp):
                'Data o be deleted is found'
                if(temp.data==data):
                    'Set flag as true and break'
                    flag=True
                    break
                'Keep a previous pointer that holds temp in order to change address when the ke matches'              
                prev=temp                    
                temp=temp.next 
            'The data to be deleted is not Found'  
            if(flag==False):
                print('The data you requested to delete was not found')
                return
            else:
                prev.next=temp.next
    
    def deleteNodeAtAPosition(self,pos):
        if(self.head==None):
            print('There is no element in the list')
            return
        temp=self.head
        p=0
        while(temp.next):
            temp=temp.next
            p+=1        
        if(p<pos):
            print('The position requested to delete does not exist in the list')    
        else:
            temp1=self.head
            p1=0
            while(p1<pos):
                prev=temp1
                temp1=temp1.next
                p1+=1
            prev.next=temp1.next
                
    def lengthOfALinkedListIterative(self):
        if(self.head==None):
            print("Length of the list is 0")
            return
        else:
            temp=self.head
            length=0
            while(temp):
                length+=1;
                temp=temp.next
            print("Length of the list is %d"%length)
            return
        
    def lengthOfALinkedListRecursive(self,node):
        if(node==None):
            return 0
        else:
            'Add 1 and recursively call the function to calculate the length'
            return 1+self.lengthOfALinkedListRecursive(node.next)
        
    'Creating a constructor function that passes the head as the initial node'    
    def lengthOfALinkedListRec(self):
        return self.lengthOfALinkedListRecursive(self.head) 
    
    'Search an  element in a LinkedList:Iterative'
    def searchAnElementInALinkedList(self,data):
        if(self.head==None):
            return False
        else:
            temp=self.head
            flag=False
            while(temp):
                if(temp.data==data):
                    flag=True
                    return True
                temp=temp.next
            if(flag==False):
                return False
    'Search an element in a LinkedList:Recursive'
    def recSearch(self,data,node):
        if(node==None):
            return False
        elif(node.data==data):
            return True
        else:
            return self.recSearch(data,node.next)
    def searchAnElementInALinkedListRec(self,data):
        return self.recSearch(data,self.head)
    
    def swapNodeaInALinkedList(self,x,y):
        if(self.head==None):
            print('The list is empty and there are no nodes to swap')
            return
        elif(x==y):
            print('The elements to be swapped are the same. So nothing is done')
            return
        
        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
 
        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
 
        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        # If x is not head of linked list
        if prevX != None:
            prevX.next = currY
        else: #make y the new head
            self.head = currY
 
        # If y is not head of linked list
        if prevY != None:
            prevY.next = currX
        else: # make x the new head
            self.head = currX
 
        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp
    def middleOfALinkedList(self):
        if(self.head==None):
            print('The list is empty')
            return
        fastPtr=self.head
        slowPtr=self.head
        'Keep two pointers fast and slow and assign it to head'
        'Increase the fast ptr by 2 and slow ptr by 1'
        'When the fastPtr reaches Null, The slow Ptr will give the position of the middle element'
        while(fastPtr!=None and fastPtr.next!=None):
            
            temp=fastPtr.next
            fastPtr=temp.next
            slowPtr=slowPtr.next
        print(slowPtr.data)
        return
    
    def printNthNodeFromTheEndOfALinkedList(self,n):
        if(self.head==None):
            print('The list is empty')
            return
        'Take two pointers and set them to head. Ref and Main Ptr'
        refPtr=self.head
        mainPtr=self.head
        N=0
        'Loop until the ref pointer reaches the nth node of linked list'
        while(N<n and refPtr!=None):
            refPtr=refPtr.next
            N+=1
        'Loop until the ref ptr reaches the null and increment the main ptr'
        while(refPtr!=None):
            mainPtr=mainPtr.next
            refPtr=refPtr.next
        print(mainPtr.data)
        return
    
    def deleteTheEntireLinkedList(self):
        temp=self.head
        temp1=self.head
        while(temp!=None):
            temp1=temp.next;
            temp=None
            temp=temp1
        self.head=None 
    
    def countNoOfTimesAGivenElementOccurs(self,element):
        if(self.head==None):
            print('List is empty')
            return
        count=0
        temp=self.head
        while(temp):
            if(temp.data==element):
                count+=1
            temp=temp.next
        print("The element occurs %d times"%count)
    
    def reverseLinkedList(self):
        if(self.head==None):
            print('The list is empty')
            return
        else:
            prev=None
            current=self.head
            while(current!=None):
                next=current.next
                current.next=prev
                prev=current
                current=next
            self.head=prev
    
    def cycleDetection(self):
        if(self.head==None):
            print('The list is empty')
            return
        else:
            fastPtr=self.head
            slowPtr=self.head
            while(fastPtr!=None and fastPtr.next!=None):
                #temp=fastPtr.next
                fastPtr=fastPtr.next.next
                slowPtr=slowPtr.next
                if(fastPtr==slowPtr):
                    return True
            return False
        
    def mergeSortedLinkedList(self,head1,head2):
        if(head1==None and head2==None):
            return
        if(head1==None):
            return head2 
        elif(head2==None):
            return head1
        if(head1.data<=head2.data):
            smallerNode=head1
            smallerNode.next=self.mergeSortedLinkedList(head1.next, head2)
        else:
            smallerNode=head2
            smallerNode.next=self.mergeSortedLinkedList(head1, head2.next)
        return smallerNode
    
    def insertNodeInASortedList(self,data):
        newNode=Node(data)
        temp=self.head
        if(self.head==None):
            self.head=newNode
            return
        elif(temp.data>=data):
            'If the element to be inserted is smaller than the head, then make that element the head'
            self.head=newNode
            newNode.next=temp
        else:
            while(temp!=None and temp.data<data):
                'Keep track of prev and next node'
                prev=temp
                temp=temp.next 
            'Make changes to point properly'
            newNode.next=temp
            prev.next=newNode       
'''Main function starts from here'''
if __name__=='__main__':
    
    'Object for LinkedList'
    llist=LinkedList()
    ''' 'Object for Node1'
    first=Node(1)
    llist.head=first
    'Object for Node1'
    second=Node(2)
    llist.head.next=second
    'Object for Node1'
    third=Node(3)
    second.next=third'''
    'llist.addANodeAfterAGivenNode(1, 0)'
    llist.addANodeAtTheFront(4)
    llist.addANodeAtTheFront(2)
    llist.addANodeAtTheFront(1)
    llist.addANodeAfterAGivenNode(3, 2)
    llist.addANodeAtTheEnd(45)
    llist.addANodeAtTheFront(15)
    llist.addANodeAtTheEnd(90)
    llist.deleteANodeInTheList(789)
    llist.deleteANodeInTheList(2)
    llist.deleteNodeAtAPosition(2)
    llist.deleteNodeAtAPosition(5)
    llist.deleteNodeAtAPosition(4)
    llist.lengthOfALinkedListIterative()
    print('List length recursively',llist.lengthOfALinkedListRec())
    if(llist.searchAnElementInALinkedList(908)):
        print("True")
    else:
        print("False")
    if(llist.searchAnElementInALinkedListRec(1)):
        print("True")
    else:
        print("False")
    llist.swapNodeaInALinkedList(15, 45)
    llist.swapNodeaInALinkedList(1, 15)
    
    'Print the LinkedList'
    
    #llist.addANodeAtTheFront(23)
    #llist.middleOfALinkedList()
    #llist.printList()
    #llist.printNthNodeFromTheEndOfALinkedList(3)
    #llist.deleteTheEntireLinkedList()
    #print('List after Deleting')
    #llist.addANodeAtTheFront(23)
    #llist.addANodeAtTheFront(23)
    #llist.addANodeAtTheFront(23)
    llist.printList()
    #llist.countNoOfTimesAGivenElementOccurs(23)
    print('After reversing the Linked List')
    llist.reverseLinkedList()
    llist.printList()
    '''#Creating a loop for testing
    llist.head.next.next.next.next.next = llist.head
    print(llist.cycleDetection())
    llist1=LinkedList()
    llist1.addANodeAtTheEnd(5)
    llist1.addANodeAtTheFront(10)
    llist1.addANodeAtTheEnd(15)
    llist2=LinkedList()
    llist2.addANodeAtTheEnd(2)
    llist2.addANodeAtTheFront(3)
    llist2.addANodeAtTheEnd(20)
    #head=llist1.mergeSortedLinkedList(llist1.head,llist2.head)
    llist1.printList()'''
    llist.insertNodeInASortedList(-1)
    print('After inserting in a sorted order the Linked List')
    llist.printList()
        