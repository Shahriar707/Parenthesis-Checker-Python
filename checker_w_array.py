class Stack_Parenthesis():

    list1 = []
    pointer = -1

    def push(self, e):
        self.list1.append(e)
        self.pointer = self.pointer + 1

    def peek(self):
        return self.list1[self.pointer]

    def pop(self):
        if self.pointer == -1:
            raise Exception("Stack Under Flow")
        else:
            delete = self.list1[self.pointer]
            self.list1 = self.list1[:-1]
            self.pointer = self.pointer - 1
            return delete

    def is_full(self):
        if self.pointer == len(self.list1):
            print("The Stack is full")

    def is_empty(self):
        if self.pointer == -1:
            print("The Stack is Empty")
            return True

    def show_Stack(self):
        print(self.list1)


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
    bracket_list = []
    bracket_position = []
    for i, index in enumerate(expression):
        if index in ["(", "{", "["]:
            bracket_list.append(index)
            bracket_position.append(i)

        if index in [")", "}", "]"]:
            if not bracket_list:
                return i+1, index, "opened"

            last = bracket_list[-1]
            last_position = bracket_position[-1]
            if parenthesis(last, index):
                bracket_list.pop()
                bracket_position.pop()
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