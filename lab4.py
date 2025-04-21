# #prgrm 1
# class stack:
#     def __init__(self):
#         self.stack=[]
    
#     def push(self,element):
#         self.stack.append(element)
    
#     def pop(self):
#         return self.stack.pop() 
    
#     def peek(self):
#         return self.stack[-1]
    
#     def isempty(self):
#         return len(self.stack)==0
    
#     def size(self):
#         return len(self.stack)
    

# myStack= stack()
# myStack.push('a')
# myStack.push('b')
# myStack.push('c')

# print("Stack: ", myStack.stack)
# myStack.pop()
# print("Stack: ", myStack.stack)
# print(myStack.peek())


#prgrm 2

# class Queue:
#     def __init__(self):
#         self.queue=[]
    
#     def enqueue(self,element):
#         self.queue.append(element)
    
#     def dequeue(self):
#        return self.queue.pop(0)
    
#     def isEmpty(self):
#         return len(self.queue)==0
    
#     def size(self):
#         return len(self.queue)
    
# myqueue = Queue()
# myqueue.enqueue('a')
# myqueue.enqueue('b')
# myqueue.enqueue('c')
# print(myqueue.queue)
# myqueue.dequeue()
# print(myqueue.queue)

        

# prgrm 3

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

if __name__ == "__main__":
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    targets = [23, 5, 91, 100]
    
    for target in targets:
        result = binary_search(sorted_array, target)
        if result != -1:
            print(f"Element {target} found at index {result}")
        else:
            print(f"Element {target} not found in the array")
    
    print("\nStep-by-step demonstration for target = 23:")
    arr = sorted_array
    target = 23
    left = 0
    right = len(arr) - 1
    
    step = 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"Found target {target} at index {mid}")
            break
        elif arr[mid] < target:
            print(f"arr[mid]={arr[mid]} < target={target}, search right half")
            left = mid + 1
        else:
            print(f"arr[mid]={arr[mid]} > target={target}, search left half")
            right = mid - 1
        
        step += 1
