class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None    

class Stack:
    def __init__(self):
        self.head = Node("head")  
        self.size = 0
        self.height = 0           

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + " "
            cur = cur.next
        return out.strip()

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next 
        self.head.next = node     
        self.size += 1
        self.height += value        

    def pop(self):
        if self.is_empty():
            return 0
        removed = self.head.next
        self.head.next = self.head.next.next  
        self.size -= 1
        self.height -= removed.value          
        return removed.value

    def get_elements(self):
        cur = self.head.next
        values = []
        while cur:
            values.append(cur.value)
            cur = cur.next
        return values[::-1] 

    def copy(self):
        new_stack = Stack()
        elements = self.get_elements()          
        for element in reversed(elements):     
            new_stack.push(element)
        return new_stack

def stack_from_input(input_str):
    stack = Stack()
    try:
        elements = list(map(int, input_str.strip().split()))
        for element in reversed(elements):  
            stack.push(element)
    except ValueError:
        print("Invalid input! Only integers are allowed.")
    return stack

def find_equal_height(s1, s2, s3):
    stack1 = s1.copy()
    stack2 = s2.copy()
    stack3 = s3.copy()

    while not (stack1.height == stack2.height == stack3.height):
        if stack1.is_empty() or stack2.is_empty() or stack3.is_empty():
            return False, None, None, None 
            
        max_height = max(stack1.height, stack2.height, stack3.height)
        if stack1.height == max_height:
            stack1.pop()
        elif stack2.height == max_height:
            stack2.pop()
        elif stack3.height == max_height:
            stack3.pop()

    return True, stack1, stack2, stack3

def main():
    while True:
        print("\n----------------------------------------------")
        s1_input = input("Enter elements of Stack 1: ")
        s2_input = input("Enter elements of Stack 2: ")
        s3_input = input("Enter elements of Stack 3: ")

        stack1 = stack_from_input(s1_input)
        stack2 = stack_from_input(s2_input)
        stack3 = stack_from_input(s3_input)

        print("\n----------------------------------------------")
        print(f"Stack 1 total height: {stack1.height}")
        print(f"Stack 2 total height: {stack2.height}")
        print(f"Stack 3 total height: {stack3.height}")

        print("\n----------------------------------------------")
        result, s1_result, s2_result, s3_result = find_equal_height(stack1, stack2, stack3)
        
        if result:
            print(f"All stacks are equal at Height: {s1_result.height}")
            print("Stack 1:", " ".join(map(str, s1_result.get_elements())))
            print("Stack 2:", " ".join(map(str, s2_result.get_elements())))
            print("Stack 3:", " ".join(map(str, s3_result.get_elements())))
        else:
            print("Stack heights will never be equal.")

        print("\n----------------------------------------------")
        while True:
            cont = input("\nContinue? Y or N? ").strip()
            if cont == 'Y':
                break 
            elif cont == 'N':
                print("\nThank you!")
                return
            else:
                print("Invalid input! Please enter Y or N only.")

if __name__ == "__main__":
    main()