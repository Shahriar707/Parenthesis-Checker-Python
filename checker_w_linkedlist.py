class Node:
    def __init__(self, element, position):
        self.element = element
        self.position = position
        self.next = None

class Stack_Parenthesis:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, element, position):
        if self.head == None:
            self.head = Node(element, position)
        else:
            newNode = Node(element, position)
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.is_empty():
            return "Stack Under Flow"
        else:
            delete = self.head
            self.head = self.head.next
            delete.next = None
            return delete

    def peek(self):
        if self.is_empty():
            return "Stack Under Flow"
        else:
            return self.head.element, self.head.position


def parenthesis(opening, closing):
    if opening == "(" and closing == ")":
        return True
    if opening == "{" and closing == "}":
        return True
    if opening == "[" and closing == "]":
        return True
    else:
        return False

def validation(expression):
    bracket_list = Stack_Parenthesis()
    for i, index in enumerate(expression):
        if index in ["(", "{", "["]:
            bracket_list.push(i, index)

        if index in [")", "}", "]"]:
            if bracket_list.is_empty():
                return i+1, index, "opened"
        last = bracket_list.peek()
        last_position = bracket_list.peek()
        if parenthesis(index, last):
            bracket_list.pop()
        else:
            return last_position+1, last, "closed"

    return -1, None, None

def output():
    expression = input()
    index, bracket, mistake = validation(expression)
    if index == -1:
        print("The expression is correct")
    else:
        print("The expression is NOT correct")
        print("Error at character #{} '{}' -not {}".format(index, bracket, mistake))

if __name__ == "__main__":
    output()

list1 = Stack_Parenthesis()