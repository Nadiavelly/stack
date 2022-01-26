line = "(((([{}]))))"


class Stack:

    stack = []

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[self.size() - 1]

    def pop(self):
        return self.stack.pop(self.size() - 1)

    def isEmpty(self):
        if self.size() != 0:
            return False
        else:
            return True

    def push(self, bracket):
        self.stack.append(bracket)


st = Stack()
if line[0] == ')' or line[0] == '}' or line[0] == ']':
    st.push(line[0])
else:
    for i in line:

        if i == '(' or i == '{' or i == '[':
            st.push(i)
        elif i == ')' and st.peek() == '(':
            st.pop()
        elif i == ']' and st.peek() == '[':
            st.pop()
        elif i == '}' and st.peek() == '{':
            st.pop()
        else:
            break

if st.size() == 0:
    print('Сбалансированно')
else:
    print('Несбалансированно')
